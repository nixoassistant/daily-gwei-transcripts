# Podcast Transcripts

Auto-generated transcripts of Ethereum podcasts using Whisper.

## Podcasts

- **Daily Gwei Refuel** — Anthony Sassano's daily Ethereum news
- **Bankless** — Ethereum and crypto deep dives

## Structure

```
transcripts/
├── daily-gwei/
│   ├── manifest.json
│   └── YYYY-MM-DD-title.md
└── bankless/
    ├── manifest.json
    └── YYYY-MM-DD-title.md
```

## How it works

- GitHub Actions runs daily at 12:00 UTC
- Downloads new episodes from RSS feeds
- Transcribes with Whisper (medium model)
- Applies ETH terminology corrections
- Formats into readable paragraphs
