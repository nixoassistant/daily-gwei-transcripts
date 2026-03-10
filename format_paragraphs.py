#!/usr/bin/env python3
"""
Format transcript paragraphs - hybrid LLM + heuristic approach.
"""

import os
import sys
import json
import re
from pathlib import Path
import urllib.request
import urllib.error

EFAI_URL = "https://automation-testing.ethereum.foundation/gateway/inference/v1/chat/completions"
EFAI_MODEL = "openai/gpt-oss-120b"

# Heuristic break patterns
BREAK_PATTERNS = [
    r'\.\s+(All right|Alright|Okay|OK|So,|Now,|Moving on|Next up|Speaking of|But yeah|Anyway|On top of that)',
    r'\.\s+(The first|The second|The third|First off|Secondly|Lastly|Last up|Finally)',
    r'\.\s+(Another thing|Another big|One more thing|Something else)',
    r'\.\s+(But|However|That said|That being said|On the other hand)',
    r'\.\s+(So yeah|But yeah|Anyway|Anyways|Regardless)',
    r'\.\s+(Let me|I want to|I\'m going to|I\'ll)',
]

def heuristic_format(text: str) -> str:
    """Add paragraph breaks using heuristic patterns."""
    result = text
    
    for pattern in BREAK_PATTERNS:
        # Add double newline before the matching phrase
        result = re.sub(
            pattern,
            lambda m: '.\n\n' + m.group(1),
            result,
            flags=re.IGNORECASE
        )
    
    # Also break on very long sentences (>500 chars without a break)
    lines = result.split('\n\n')
    formatted_lines = []
    for line in lines:
        if len(line) > 2000:
            # Split at sentence boundaries roughly every 500-800 chars
            sentences = re.split(r'(?<=[.!?])\s+', line)
            current_para = []
            current_len = 0
            for sent in sentences:
                current_para.append(sent)
                current_len += len(sent)
                if current_len > 600:
                    formatted_lines.append(' '.join(current_para))
                    current_para = []
                    current_len = 0
            if current_para:
                formatted_lines.append(' '.join(current_para))
        else:
            formatted_lines.append(line)
    
    return '\n\n'.join(formatted_lines)

def call_efai(text: str, api_key: str, timeout: int = 60) -> str:
    """Call EFAI API to format paragraphs."""
    
    prompt = f"""Add paragraph breaks to this podcast transcript at natural topic transitions. 
Keep text EXACTLY the same - only add blank lines between paragraphs.
Return ONLY the formatted text, nothing else.

{text}"""

    payload = {
        "model": EFAI_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 8000,
        "temperature": 0.1
    }
    
    req = urllib.request.Request(
        EFAI_URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            return result["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"    LLM failed ({e}), using heuristics")
        return None

def process_file(filepath: Path, api_key: str = None, dry_run: bool = False) -> bool:
    """Process a single transcript file."""
    content = filepath.read_text()
    
    # Split into header and body
    parts = content.split("---\n\n", 1)
    if len(parts) != 2:
        print(f"  Skipping {filepath.name}: unexpected format")
        return False
    
    header, body = parts[0] + "---\n\n", parts[1]
    
    # Skip if already has multiple paragraphs
    if body.count("\n\n") > 5:
        print(f"  Skipping {filepath.name}: already formatted")
        return False
    
    print(f"  Formatting {filepath.name}...")
    
    # Try LLM on smaller chunks, fallback to heuristics
    if api_key and len(body) < 15000:
        formatted = call_efai(body, api_key)
        if formatted:
            body = formatted
        else:
            body = heuristic_format(body)
    else:
        print(f"    Using heuristics (text too long for LLM)")
        body = heuristic_format(body)
    
    if not dry_run:
        filepath.write_text(header + body)
        print(f"    Done: {body.count(chr(10)+chr(10))} paragraphs")
    
    return True

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Format transcript paragraphs")
    parser.add_argument("files", nargs="*", help="Files to process")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--heuristics-only", action="store_true", help="Skip LLM, use heuristics only")
    args = parser.parse_args()
    
    api_key = None if args.heuristics_only else os.environ.get("EFAI_API_KEY")
    
    files = args.files
    if not files:
        files = list(Path(__file__).parent.glob("transcripts/*.md"))
    else:
        files = [Path(f) for f in files]
    
    processed = 0
    for f in files:
        try:
            if process_file(f, api_key, args.dry_run):
                processed += 1
        except Exception as e:
            print(f"  Error: {e}")
    
    print(f"\nFormatted {processed} files")

if __name__ == "__main__":
    main()
