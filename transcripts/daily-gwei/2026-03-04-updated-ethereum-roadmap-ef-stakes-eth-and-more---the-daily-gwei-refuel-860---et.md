# Updated Ethereum roadmap, EF stakes ETH and more - The Daily Gwei Refuel #860 - Ethereum Updates

**Date:** 2026-03-04
**Source:** Transcribed with faster-whisper (small model)

---

Hello, everyone. Welcome to another episode of Daily Gwei Refuel, where I capture the latest news in the Ethereum ecosystem. I'm your host, Anthony Sassano, it's the 4th of March, 2026.

All right, everyone, let's get into it. So apologies for missing the last two days. Obviously, I'm supposed to do a refuel on Monday.

But the last two days have just been quite busy for me. So I've only gotten around to doing one today.

But there is a lot to talk about. Actually, I was going back and getting all the content to record today's episode just before. And I was like, wow, a lot happened. And that's probably because it's been a week and a half since the last refuel.

But regardless, I'm excited to dive in. So first things first, the roadmap update that I was or the protocol roadmap update that I was teasing, I think the last two refuels was finally published. So Justin Drake put together a nice tweet going over what this is, which you can read a link in the YouTube description below.

But there is a website for it called strawmap.org. And you can go here and you can see the roadmap. Basically, I guess as a high level overview here, it's essentially a roadmap from I guess this year, 2026 to 2030 and beyond.

Now, I expect this to continuously be updated. It's not going to be like, I guess the roadmap of old, which was Vitalik's diagrams that he would update every so often and put on Twitter. This is a website that is maintained by the EF architecture team, which includes Justin Drake, Ansgar, Barnabé and Francesco. And they're going to be updating this as time goes on.

Now, I'm not going to go through everything on obviously this roadmap here, but if you go to the website yourself, you'll be able to see that a lot of it is stuff that I've spoken about on the refuel before and a lot of it is stuff that just gets spoken about in the community generally. Nothing on this roadmap, at least from what I could tell, is like net new. Like it's nothing on this that we haven't already kind of had posts about or discussions about in the past.

But there are, I guess, like some differences between how we've discussed them in the past. I think the biggest thing, and the thing that made me kind of go, okay, that's new and interesting, is this kind of thinking emoji face.

Now, you probably can't see it on my screen because it's quite small. Maybe I can zoom in here. No, zooming in doesn't really work. It just zooms in the everything else except the map here.

But you'll see it if you go to the website. There's like a thinking emoji on a few different things on the roadmap here.

Now, they've kind of put this at the bottom here what this means. It means there's uncertainty about this ever shipping. Like so it's something that's there, but it may not ever make it into the Ethereum protocol itself. In terms of things that you may have heard of before and things that, I guess, have been on the roadmap for maybe a little while now that has this thinking face on it, APS. So APS has been talked about a lot in the context of, I guess, things like attestors and what powers or duties they have within the Ethereum protocol. So APS might have been something that you've kind of heard about there.

But most of the other stuff, I think, is very kind of, I guess, exotic research. And that's why it's got the thinking face here. Because it's like, well, we don't even know if we either want this or if it's even possible to do in line with everything else. Because you got to obviously remember that everything has to work with everything. Everything has to be compatible with everything. We can't ship something if it's just going to break something else without either modifying that something else or removing it. And then obviously we would want it to be a net benefit here. And that falls into the three different categories of the roadmap, which is a nice segue into the three different categories here. So as you guys know, we have the consensus layer and the execution layer. That's been around for a while now, obviously, since the merge.

But even before that, we had a separate consensus layer and a separate execution layer with the beacon chain and with the normal Ethereum chain.

But the normal kind of E1 chain had a consensus engine of itself, obviously, with the proof of work.

But now we have just the one unified chain and it's the CL and EL there.

The third layer that is kind of, I mean, this is already a thing, like this is not a new layer, but it's kind of been split out into its own layer here, is the data layer. And now this encompasses things like blobs, which obviously we know a lot about already. It encompasses things like call data, which is, I guess, like, which was the precursor to blobs and is still around today and is still used today. And it covers everything in between. And it kind of relates to the other layers like the consensus and execution layer here.

So yeah, this is a huge roadmap, guys. There's a bunch of items on here. I don't know how many items there are on here.

But like each of these items in of itself is a huge lift, I think. You know, we've got things like everyone's favorite, like shortening slot times, we've got fast finality, we've got improved, obviously PeerDAS, we've got Giga gas or Terra gas, sorry, Giga gas L1. We've got, and I'm just, I'm just reading off here, we've got like account abstraction stuff, we've got binary trees. There's so much stuff here, guys. And like, I wouldn't even claim to understand half of it in depth. Like I understand high level, a lot of these things, but I wouldn't claim to understand half of it in depth here. And of course, as I said at the beginning, this roadmap is from this year to 2030 plus. And then at the top here underneath the years, you can actually see where these upgrades are, I guess, like speculatively slotted in or where these kind of EIPs, well, they'll eventually become EIPs, if they're not already, are slotted in into each upgrade.

Now, we can only really ever look maybe two upgrades in advance with relative certainty, maybe three in terms of like we look at the first two that are upcoming, like Glamsterdam and Hegota, for example, and we have a general idea of what's going to go in those.

But then once you start getting, you know, past that with iStar, jStar and so on and so forth, it becomes a lot more speculative as we've seen in the past, things can get dropped, things can get added, you know, and things can change quite dramatically there.

But under each of these, I guess like headlines here, I shouldn't say headlines headings, such as iStar, jStar, kStar, all the way to mStar. And then after that, it's labeled as longer term, there are these different upgrades underneath each of them. And again, I would say this is just a speculative thing here, because I guarantee you that it's not going to be like this. There's going to be some that go in later, some that come in sooner.

But still, it's a good little roadmap here that shows us what's coming, regardless of where it goes, which is really, really cool. So you can also see down the bottom there, they've got like a color coding happening across the entire roadmap, and they're explaining it here, explaining which upgrades would be north stars for the consensus layer. Well, for each layer, I should say which ones will be headliners, and which ones are on chain versus off chain. So this is a pretty comprehensive roadmap here, guys. And also, some of these have kind of links. So if I clicked on FOCIL, for example, it opens up the EIP for FOCIL. So you've already got kind of explanations of what these things do embedded here.

But you can always go to the forecast website for a lot of information on this stuff too.

But it's just great to have like a single repository here, a single kind of resource here to see what's happening across the board in terms of the protocol roadmap.

Now, obviously, this is layer one. This is the layer one protocol. This is everything happening at layer one. This doesn't include all the stuff happening at the layer two still, because that's all managed by their own respective teams, all the stuff happening with the apps, you know, the infrastructure, everything else around the Ethereum ecosystem. This is just the core protocol.

But of course, the core protocol touches everything. So it's good that we have this very transparent, very cool, in my opinion, roadmap here. So I'm going to give Justin Drake's tweet a read. It gives a lot more context around this, which, you know, I got really bullish reading it, to be honest. Justin Drake always manages to bull me up.

So yeah, I definitely recommend going, giving that a read.

I'll link it in the YouTube description below.

But on top of that as well, Vitalik has been on a massive posting spree lately again, which I always love seeing about some of the core points of each of these kind of roadmap items. So he put out a tweet about the block building pipeline, execution layer changes, account obstruction, scaling, quantum resistance roadmap. And yeah, I think that was the after Justin put this tweet out. He put out all those tweet threads there. I'm not going to link them all. I'm just going to, you know, tell you to go to Vitalik's profile and you'll be able to find them there. It's really great that Vitalik is there explaining these things because obviously, as we know, Vitalik has more reach than anyone else, right? On Twitter, on, you know, in the ecosystem and beyond the ecosystem, because whenever Vitalik talks about something, sometimes I'll like Google it. And then there'll be all these media organizations that report on Vitalik talking about it, even though it's nothing new, right? It's not something that, like it may actually be really old. Like a lot of the stuff that Vitalik actually talks about in these tweets are very old things. Like they've been around for many, many years. Like some of them have been around for four or five years.

But because Vitalik is talking about it, the media picks up on it, the rest of the ecosystem picks up on it, and it gets a lot more traction. So I really appreciate whenever Vitalik does this, because it makes my job a lot easier as an educator, because it means that I come across more people who are already aware of these things. And then I can kind of, you know, maybe educate them a bit further on that, but they can say, oh yeah, I heard it from Vitalik and so on and so forth, which is great there.

So yeah, a bunch of reading for you guys to do, if you're interested, if you've missed it, I'm sure a lot of you have probably already seen it, but I figured I'd give the shout out there for you guys. You can go check that out there.

Moving on from that, the Ethereum Foundation has finally begun staking a portion of its Treasury. Now this was announced a while ago, I believe, maybe even a year ago, that the Ethereum Foundation would be putting their ETH to work in staking. So on February 24th, they made a deposit of 2016 ETH with the plans for approximately 70,000 ETH to be staked with rewards directed back to the ETH Treasury. The ETH is being conducted with open source software options like a Dirk and Vouch by a testant. And I've spoken about Dirk and Vouch before. This is really great for client diversity and client health across the board here, which is really great to see.

But yeah, that's an enormous amount of ETH guys. And obviously, the Ethereum Foundation has changed a lot in the last 18 or so months, I would say, even less than that, right? Substantial amount. I have not seen the EF change this much since I got into Ethereum in 2017. And I think that there's the biggest change they've undergone since the inception, essentially, of the Ethereum Foundation, which would have been early 2014, I think, or even late 2013, when Vitalik Buterin first published that White Paper all those years ago.

But yeah, there's just another kind of big change that they're having here, where they're basically saying that, you know what, credible neutrality is great, and we want to keep that. And that was their reason for not staking their ETH before. They didn't want to be in the decision making process directly or be a kind of centralizing force there.

But 70,000 ETH guys, that's literally a drop in the bucket when it comes to the amount of validators they will have on the network. I would argue, obviously, that their social power trumps their economic power here by a lot, because they're the Ethereum Foundation. They have a lot more social credibility than any other, I guess, Ethereum participant, Ethereum entity. So them staking 70,000 ETH is literally meaningless in the kind of context of their control over the network or any kind of control they could kind of put on the network here. Because, you know, if they stake this 70,000 ETH, which they plan to do, I mean, if I go to Hill Dobby's ETH 2 staking dashboard here and I'll bring it up for you guys on my screen, you'll see here the total ETH stake is 37,533,000. 70,000 as a percentage of that is nothing, right? 70,000 as a percentage. I'm not going to do the math like live, I'm just going to Google it on my other screen here. 70,000 as a percentage of 37 million is 0.18%, right? That's nothing. It's a rounding error. I know we would all love to have 70,000 ETH, mind you, but I meant in the context of how much ETH is staked, it is an absolute rounding error, guys. And obviously, what's really nice is that this ETH is being staked, not with LIDO, not with Binance, not with any of these major profites here, but on, you know, on their own, with their own setup here. So that's really great to see. And if you were to go on the kind of rankings in terms of like where the EF would be with the amount of ETH staked rankings, there would be number 27, I believe, or sorry, 28. So they'd be 28th on the leaderboard. That's, again, it's just, it's not even worth considering given that the Ethereum Foundation has a substantial more social kind of clout and social power than they do economic power. So definitely not worth kind of discussing that there, but still great to see Kudos to the EF for that there.

All right, moving on, the Ethereum protocol, or sorry, I should say Ethereum Foundation protocol support team now has its own website, which is great to see. I remember I shouted out to you guys that they have a Twitter account that you can go follow. It is criminally under follow. It's 776 followers. That's pathetic. Like this team is awesome. They're the team behind forecasts, guys. Like you have to go give them a follow, do that, and then also check out their website. You know, I'll bring it up on the screen for you guys to see.

But this team is really critical for Ethereum kind of protocol development and the Ethereum ecosystem more widely. They do a lot in the background, guys. Like I know they've got forecasts, which is obviously something that we're all well aware of. We all are kind of looking at and we're all kind of using as a resource, but they do so much more in the background. And they detail that on this website here. They basically run through everything that they're doing. So you don't have to take my word for it. You can actually just go here and learn about them for yourself. And you can also learn about how to contribute as well, because this is not just their team. You can also contribute to this if you want as well. So they've got a page for that. And of course, they've also got a page for the team here. So you can see their team members. There's currently six core team members of this team here.

But at the same time, as I said, you can contribute as just a regular person. Like you don't have to be part of the team to contribute. We're all about open source here, guys. We're all about having everything open and everything being able to be contributed to by anyone.

But now that I've got the team in front of me, I'm just going to give them a huge shout out, because I use forecast all the time, as you guys know. So Nickso, Josh Davies, Mark Gorea, hopefully I pronounced the surname right there. Mario Havel, Buda, and Dionysus. I pronounced that wrong.

But these six people, huge kudos to you, huge thanks to you for putting together the forecast website, of course.

But everything else that you're doing, just great to have you guys helping out and doing all the great work there.

But yeah, you guys can check out the website. If you haven't yet, I'll link it in the YouTube description below for you to do so.

All right, something that I didn't cover on the last refuel, which I should have covered because I don't know how I missed this, but like it happened on February 18th, there is a new team that the Ethereum Foundation put together called the Platform Team, which I believe is being headed up by Josh Rudolph here.

Now, as you guys know, Josh Rudolph has been involved with Ethereum for quite a while. I've been covering his tweets for quite a while. He's been quite involved with the stuff around the user interface experience and the user experience with regards to Ethereum, like things like account abstraction, stuff like that. So essentially what this team does, or what it's kind of, I guess, like core goal is, is to deliver the strongest possible Ethereum platform where L1 and L2 are best positioned to support users, apps, and all groups building on Ethereum. There's a little thread here about this as well as a blog post about what these guys are going to be doing.

But this is also another team I think has needed to exist for a little while now. And if there's one criticism of Ethereum that I see kind of pop up a lot, and I also somewhat resonate with, I have my own reservations about this argument, but I somewhat resonate with this kind of argument or criticism, whatever you want to call it. Ethereum is really good at building infrastructure, right? It's really good at building things that are stable, secure.

But when it comes to building, I guess, like user experiences and building something that's more like, I guess, product focused, it's definitely an area that the Ethereum ecosystem lacks in.

Now, I would say that there's a lot of apps on Ethereum that have filled kind of this role and built out these things.

But the problem is that like, if they don't get the relevant support or I guess like relevant upgrades happening on the Ethereum core side or the Ethereum protocol side, it becomes hard for them to do their job. And account abstraction is the biggest thing here, right? Like, I think that, you know, to me, it's not a huge issue, especially when gas fees are low, that you have to like, prove a token for transfer for all the protocols you interact with. So it's like, instead of one click to swap, it's like two clicks to swap or something like that. To me, that's not a huge issue because like, I don't like, honestly, it really doesn't matter to me that much. Like, I'm a power user, I guess it really doesn't matter.

But for like the average user, it's definitely a huge friction point. And that's what we've been trying to solve for a while. And there's a bunch of different reasons why this friction point exists. And why it actually exists for real reasons, like security reasons, right? But also why it's been so hard to kind of remove that. I think that it's a mixture of kind of technical difficulties and technical kind of considerations, but also social and coordination issues that hopefully the platform team can kind of work on and resolve so that we can improve the user experience of Ethereum across the board. And I'm talking about, I guess, like Ethereum L1 here, like the L2s, they are responsible for their own experience a lot of the time. And they've solved one, I guess, side of it, which is the speed of transactions. Obviously Ethereum L1 has its own roadmap for that with faster slots.

But even if we get to four second slots, I think that's going to be the lowest we get. It's never going to be as fast as the L2s, which is, I guess, fine. And the whole point. And we're also going to have like things like pre-confirmations on L1, but we do need to make those things easier to use as well, right? So when you take all that together and you kind of think about it as a holistic thing, you do realize that we need a team like this. So I'm glad the EF has put this team together. I'm glad it's headed up by people who have a lot of experience with this stuff. And I wish them all the best with this. I wish them luck with this. So I just wanted to cover that there for you guys.

Now, next on the agenda, speaking of teams that the EF is putting together, they have a, I believe this is a new team focused on DeFi within the Ethereum Foundation. So Charles St. Louis, who is someone who's worked in DeFi for quite a while. So he worked since, you know, MakerDAO and then went into working on Delfia, which I believe wound down recently. I just didn't find product market fit, but he has a lot of experience within DeFi, has joined the Ethereum Foundation alongside, I think a couple of other people to head up their, oh, alongside one other person, sorry, to lead their DeFi initiative.

Now, this is some, Evangby, I think that's how you say it. I'm pretty mispronouncing it again, of Gearbox protocol. So he co-founded Gearbox protocol, not GearFox protocol. And yeah, he's been in DeFi for a long time as well. So I think this is a really great initiative from the Ethereum Foundation as well, because again, the Ethereum Foundation has come under a lot of criticism in the past for not caring enough about DeFi or not focusing enough on DeFi. Well, I think that tune has changed a lot in the last 12 months. And with this new team going forward, I think that DeFi is going to be deeply embedded within the Ethereum Foundation, and also be deeply embedded across everything that Ethereum Foundation is doing, and as it should be.

I think that DeFi is, as you guys know, in my opinion, is like the thing. It's not the only thing, but it is the thing. It's the biggest thing. It's the thing that drives the value to these ecosystems. And it's what enables us to do more of the other things that Vitalik tweets about, right? Like all the self-sovereign kind of identity stuff, the privacy stuff, the decentralized document kind of editing, like file verse that he shared before, like all that sorts of stuff, right? Things that empower the individual. In my opinion, they're only possible because of the financial stuff, because of the financial side of things.

Because the financial side of things drives the activity, right? It drives the interest, it drives the investment in these things. The extreme example of this is the ZK stuff, right? And I've gone through this a lot before, but I just figured I'd bring up this up, because it's a pretty good example. ZK only came so quickly because of the fact that the ZK teams were basically all L2 teams, and they were able to raise a lot of money from VCs, because VCs wanted to get a token and expected a return from it. And they were like, okay, we'll fund you guys. And then the L2 teams went ahead and worked on all the ZK stuff.

And now we have ZK stuff that is so much farther along than it otherwise would have been. So again, we need the DeFi, we need the finance, we need the money, right? We need that stuff to drive the other things.

Now, there's different ways of thinking about DeFi. And in this post, it stated that the Ethereum Foundation believes in something called DeFi Punk, which is not finance that's marginally better than TradFi, but finance that couldn't exist without Ethereum. That's, in my opinion, probably the best approach that the Ethereum Foundation could take here. Because it's really not just finance that's better than TradFi, even though that's a huge thing. And obviously, TradFi is heavily involved with Ethereum these days.

But finance that couldn't exist without Ethereum, because that is the unique value prop, right? If you have something that literally can't exist without Ethereum, then you have something that is unique to Ethereum, and then you have product market fit for Ethereum. I think that the most obvious example of this is ETH. ETH couldn't exist without Ethereum, right? ETH as an asset, as the asset that it is with all the properties that it has, could not exist without Ethereum. It could exist as an asset on some centralized ledger, right? I could spin up a centralized company and say, okay, well, people investing in me, you're investing in ETH shares.

But that's not ETH, right? That's not the real ETH, but I could say that.

But then it's a very different thing. It's a centralized kind of equity in my business, and its value is reliant on the profits that I generate or the revenues that I generate in my business, and how far it grows, and what the business does, and so on and so forth, right? Whereas ETH on Ethereum, and the reason why it can only exist because of Ethereum, is because Ethereum gives ETH all of its nice properties. It gives it its censorship-resistant properties, gives it its secure properties, its decentralization properties, its economic policy properties, right? It gives all of those nice properties to ETH the asset, so ETH could not exist without Ethereum. That's, in my opinion, the most obvious one.

But then obviously, there's a lot of other things that fall off of that, right? A lot of DeFi things like flash loans that can't exist in TradFi, like agentic commerce, AI commerce, that can't exist in TradFi, but can exist on Ethereum. So those sorts of things is what, I guess, the Ethereum Foundation wants to target, wants to see thrive, wants to help belong. The TradFi stuff is going to happen regardless of what the EAF does, I think. I think that the protocol upgrades are going to help the TradFi stuff, but the TradFi's going to come in regardless of if the EAF wants them to or not, because obviously it's a credibly neutral layer. TradFi's going to get a lot of value out of it, so they're going to come in. And I think that's the right approach here. I don't think the EAF should be interfacing with TradFi directly. There's other teams that do that, like Etherealize.

So, yeah, that's my view on that.

But you can go give this blog post a read about the DeFi team at the Ethereum Foundation.

I'll link it in the YouTube description below for you to do so.

All right, another thing that I didn't cover was Rocket Pool's latest upgrade.

So, Saturn I is the name of the upgrade. This is their biggest upgrade ever, and it's been successfully deployed on Mainnet. It carries with it a bunch of features like an RPL fee switch, four ETH validators, megapools, and more, which are now all active. And then they say here in 2026, Rocket Pool is still the only fully permissionless staking protocol, no reliance on AWS or a select few trusted professionals.

So, Rocket Pool was all the rage while ago, right? Like during, I guess, like the restaking era and like when everyone was talking about staking, Rocket Pool was front and center, naturally, like alongside a few other protocols out there.

But they are right when they say that Rocket Pool is still only the fully permissionless staking protocol. I had hopes for other protocols out there like other LSTs that, you know, that I, it both invested in and advised and also just like promoted.

But some of them didn't work out at all. Some of them have just like completely, I guess, not found product market fit. Some of them haven't done what they said they were going to do, whether that's because they don't plan to ever do it, or they plan to one day do it. And some of them evolved to look more, I guess, like Lido than Rocket Pool, which is not necessarily a bad thing because Lido itself is also decentralized over time, which has been great to see.

But if we're talking about fully permissionless staking protocols on Ethereum, besides solar staking, obviously, that's, that's completely different, right? That's like solar staking with the protocol itself. That's, that's the gold standard.

But we're talking about getting as close as you can to that. Rocket Pool is it. And I've been a Rocket Pool note operator for a while now and I'm part of the ODOW still. And, you know, I would actually argue that it's easier to set up a Rocket Pool kind of service, be a Rocket Pool note operator, that it needs to set up a solar staking service, which is kind of funny.

But I mean, in my experience, it is.

But on top of that, as is stated here, it's the only fully permissionless staking protocol on Ethereum. And it probably likely will only ever be that. Like, I don't think there'll be any other protocols that do it because it's a lot harder to do that. It does stifle your growth a little bit because of the fact that you have to take into consideration decentralization, permissionlessness, you have to kind of work maybe slower than you otherwise would off because of the fact that there's a bunch of different considerations here.

But regardless of that, Rocket Pool is still one of the top staking protocols, the top staking entities. If I bring up HillDobby's dashboard again, the two staking dashboard that he has here, you know, Rocket Pool is still up there. If I, where is this? Yeah, if I go here, Rocket Pool is number 10, right? They have about almost 500,000 ETH staked with them.

Now, if you go through this list, right, Lido is obviously still number one. And as I said, they have decentralized over time, but they're not a fully permissionless staking protocol. At least last time I checked, maybe they've changed, but I don't believe so. I don't think I'm that out of date on this stuff.

But then you go down the list, right, Binance, Ethify, Coinbase, Figment, Kraken, BlockDamon, Everstate, Kiln, before you get to Rocket Pool. None of these are decentralized or permissionless in my opinion. Some of them are better than others. Like, you know, Ethify is better than Binance and Coinbase.

But then you go past Rocket Pool, Bitcoin, Suisse, Upbit, OKX, Stakewise. Stakewise is probably the next one.

But they're tiny now. They're, you know, they're quite small. And I don't know that much about Stakewise to claim that they're as decentralized or permissionless as Rocket Pool. I don't think they are. And then you keep going, ptp.org, Stakefish, Liquid Collective, Dharma Capital, MantleBits. These are all centralized entities, guys. They're not decentralized at all. And they're definitely not decentralized permissionless Staking Protocols. So it is right to claim that Rocket Pool is the only one there. And, you know, kudos to them for staying with it. Because without them, we wouldn't have one on Ethereum.

So, yeah, always a huge fan of Rocket Pool. You can go read the blog post here for all the kind of, I guess, details about Satin1. It's quite a kind of lengthy kind of blog post here, which is great to see because it describes everything. Like I read through it and I'm like, okay, I understand now what's going on here because I kind of fell off on a lot of these things. It's just so hard to keep up with everything. So it was great to see this here.

So yeah, you can go check this out for yourself.

I'll link it in the YouTube description below for you to do so.

All right, L2Beat has launched a new, I guess, page. Yes, page on their website called L2Beat Interop. So they are going to be giving you all the information that you need about all the different interoperability protocols across the ecosystem because there are a lot of them, right? There are a lot of interoperability protocols, a lot of bridges, a lot of these sorts of stuff. So if you guys select a pair of chains here in Go Ethereum and Arbitrum 1, you will see a bunch of metrics around it as well, not just kind of risks with the different kind of bridges and stuff like that, but lots of different metrics like flows, the tokens that are flowing between them, the transfer sizes, so on and so forth. What they're doing, is it a burn and mint? Is it a lock and mint? And what this actually means, right? And yeah, there's just a wealth of information here.

But then if you go to the side here and click on non-minting protocols, lock and mint protocols, or burn and mint protocols, you will get a list of these as well, which is really great to see. And I believe, I don't know if it's live yet, I did see this somewhere, that they plan to have complete breakdowns of each of these bridging protocols as well, because they say here they're currently tracking 22 different protocols, which is a lot, right? And yeah, they're going to have a breakdown of each of those things, like they do for each of the L2s. So huge kudos to them for building this. This again is another kick-ass resource that comes from them. And I think I'm going to be using a lot in the future, especially around, I guess, like these metrics as well, because that's pretty cool to see.

But yeah, good job, L2B team. You're always putting out quality resources for us to consume here.

All right, someone asked the question in the Daily Grade Discord channel the other day about kind of, they wanted me to talk about previous upgrades, previous EIPs that went live on Ethereum, and adoption of these different EIPs. So probably the main one that I think is worth talking about, I'm not going to talk about them all, but the main one is Max EB.

Now, this is the protocol upgrade that went live a little while ago now, actually quite a while ago now with Pectra, I believe. Was it a Pectra? I think it was Pectra that essentially allowed the maximum ETH per validator to be 2048 ETH instead of 32 ETH. So before this went live, you would spin up, if you had like 320 ETH, you would have to spin up 10 validators.

But now you can just have one validator. So this takes a load off the network. We don't need millions and millions of validators, because as I've explained before, one person can have 100 or 10,000 or 100,000 validators, one entity, not just one person. So validator count is largely meaningless from a decentralization and security perspective here.

So yeah, you can say 2048 ETH per validator. I think a lot of new validators have been spun up with this, but there's also a way to convert your existing validators over so you basically just like consolidate them. So what the person asked me was that like, you know, what's the adoption look like here? And the perfect site to track this is Petrified.com, which I'll link in the usual description below. And you can see what the kind of adoption has been like. So most of the validators are 2048 ETH validators, the ones that are consolidated, which is kind of great to see here in terms of the amount of ETH there. And you can kind of see a bunch of different stats around this like pending deposits, pending withdrawals, pending consolidations, so on and so forth.

But overall, the adoption has been quite slow, I think of this, because there's no real like incentive or motivation to do this. Because it's not necessarily going to save you that much money as a node operator. It does require a lot of work, depending on the node operator that you are, it does require touching your validators, which, you know, and changing them, which a lot of these node operators, especially the large ones are kind of weary about and it takes them a while to do this.

But I do know that a few of the bigger ones are planning on doing this towards the end of the year. So once they do it, this will this will look a lot better.

But, you know, as far as I know, at least if I'm reading this right, about 18% of the validators are accumulating validators today. So they've got the 0x02 withdrawal credentials here. This doesn't mean that they're all 2048 ETH validators. This just means that they are, I believe, more than 32 ETH validators, so accumulating validators. So they're enabled to be able to stake more than 32 ETH per validator. That's not too bad, but it has been a while since this went live. So I think that by the end of the year, we can probably be about 50% here, which is great, because we want to make sure that we can get the total validator count down for a number of different reasons, take load off the network, but also I believe in the kind of quantum world, in the Ethereum quantum world, post-quantum, we need the validator count to be a lot lower for the network to actually work, because quantum signatures are, as far as I know, a lot larger than BLS signatures, which means that it would take longer to propagate across the network. And if there's lots of validators, it takes even longer, and the network would degrade. That's all we need to do it, basically.

So yeah, that's kind of an update on that there.

But yeah, maybe I'll check that in a few months' time and see where we're at with that there.

All right, last up here, just a quick shout out to Ethereal News. So this is a newsletter that has been around for, I believe, 13 weeks now. It's the successor to, I guess, like Week in Ethereum news and also another newsletter that was being done, I believe, after that, that was kind of a short lift here.

But this is a really great resource, guys, by Andrew here. So Andrew was essentially managing Week in Ethereum news for quite a while, then he did something else. I can't remember the name of his other newsletter that he spun up, and now he's doing Ethereal News. It's basically formatted like the Week in Ethereum news newsletter was, and you've got so many kind of updates here, so much news here to digest. It's a crazy amount of stuff going on here, guys. So all this is to say, again, a huge shout out to Andrew, but also go subscribe if you haven't yet. Click the subscribe button here. Subscribe to the newsletter. I get it every week. I use it as a resource as well because it's just got so much information here. I use it for the refuel, too. I just haven't given it a shout out yet. I don't know why, but yeah, huge shout out to Andrew here for maintaining this. And I guess thanks to Consensus as well for sponsoring this and allowing Andrew to do this. I know for a little while there, Andrew wasn't sure how he was able to continue because he wasn't getting paid for it. He wasn't able to take it on as a full-time job because it is a full-time job, tracking all this stuff, putting it together, putting the newsletter out. So I thankful to Consensus and whoever else is funding Andrew here. He's providing an absolutely awesome service to the community, free of charge of course.

So yeah, kudos to everyone involved there.

But yeah, I think that's going to be it for today. That was a nice refuel, I think. We got through a lot there. Hopefully, we'll have another episode out on Monday for you guys. Hopefully, I won't have to delay it again. And that other channel that I spoke about for my novel writing that I was going to spin up. I haven't spun that up yet. I will do it soon. I've actually been really busy writing, so I'm writing and then I'm like, I've got to do this.

But then I'm like, it's going to take away from my writing. And I've also been reading a lot more too. So a lot of my time has been dedicated to that recently. And then of course, keeping up with all the Ethereum stuff and then all my fitness stuff. Like, it's a full life right now, guys. So anyway, enough about my personal life. That's going to be it for today. Thank everyone for listening and watching. Be sure to subscribe to the channel if you haven't yet. Give it a thumbs up. So guys, newsletters, join this channel and I'll catch you all next week. Thanks, everyone.
