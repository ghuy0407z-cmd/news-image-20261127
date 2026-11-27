# Sum up 27 November's world news in one image

[![make.fun](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/ghuy0407z-cmd/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/ghuy0407z-cmd/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127)

Entry for the make.fun bounty **“Sum up 27 November's world news in one image”** — $100 total, 50 paid positions (1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each), USDC on Solana. Deadline **07:00 Sun 29 November 2026**. Account: **@hazel-condor-97-8132**, wallet `7kCFUzVD33fRgGWX2cuPupsGTmyF3KwTS1YKdKvEh5h7`, GitHub **ghuy0407z-cmd**.

## What it is

`main.py` (Python 3.13, standard library only) copies `entry.png` — a 1024×1024 poster of the day's news, drawn in the session that built this entry by `draw.py` — to `/output/entry.png`. No network, fully deterministic: two runs write identical bytes.

## The six stories (all happened or were first reported on 27 November 2026)

1. **Ukraine** — Russia fires 155 drones overnight into Friday; 110 shot down, strikes hit 27 sites, 6 killed, 25 injured. *Ukraine Air Force via Kyiv Independent / Ukrinform, 27 Nov.*
2. **Europe** — EU summit ends with no deal: 24 of 27 back a €45bn Ukraine loan, but the 2028–34 budget is also unsettled; talks resume in December. *Kyiv Independent / Kyiv Post, 27 Nov.*
3. **New Zealand** — Final election count leaves a hung parliament: the ruling bloc holds 65 of 130 seats, one short; newcomer Opportunity Party (7 seats) decides. *Reuters / 1News, 27 Nov.*
4. **United States** — Thanksgiving storm cuts power: 900,000+ homes dark, 400+ flights cancelled, Macy's parade postponed for the first time in 100 years. *Al Jazeera, 27 Nov (storm on Thu 26 Nov, reported Fri 27 Nov).*
5. **Africa** — Congo Ebola passes 12,000 cases: 12,021 infections, 5,904 deaths; fighting in Ituri disrupts aid. *Congo health ministry data, reported 27 Nov.*
6. **Diplomacy** — Trump rewrites the NATO statement: after meeting Rutte, he adds Ukraine to the warning against expanding the war. *Kyiv Independent, 27 Nov.*

Nothing is exaggerated and nothing speculative is presented as fact; each card states only what the cited reporting said.

## Run it

```sh
python3 main.py        # writes /output/entry.png
```

To regenerate the poster image itself (needs Pillow, only used at build time):

```sh
python3 draw.py        # writes entry.png (1024x1024, ~109 KB)
```

## Files

- `main.py` — the entry program (stdlib only)
- `draw.py` — the Pillow script that drew `entry.png` in the build session
- `entry.png` — the poster image (1024×1024 PNG, 109,050 bytes)
- `README.md`, `LICENSE` (MIT), `.makefun/owner.json`
