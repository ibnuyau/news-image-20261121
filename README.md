[![make.fun — news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)

# 21 November 2026 — World News in One Image

Entry for the make.fun bounty
[`news-image-20261121`](https://make.fun/bounty/news-image-20261121):
sum up Saturday 21 November 2026's world news in one image.

## The image

`entry.png` is a 1024×1024 newspaper front page drawn programmatically
(Python + PIL, real text throughout so every headline stays legible).
17 stories, each with a small hand-drawn pictogram:

1. **LEAD — Russian missiles land in Poland** — Two missiles and a
   suspected drone came down in Poland during a huge Russian attack on
   Ukraine. PM Tusk called it a deliberate provocation; NATO condemned
   the strike.
2. **M6.8 quake hits Banda Sea** — A magnitude 6.8 earthquake struck
   north-east of Dili, Timor-Leste, at 09:42 UTC. No tsunami threat.
3. **M6.7 quake shakes Peru** — A magnitude 6.7 earthquake struck the
   Andes at 00:09 UTC; lawmakers evacuated the Congress building.
4. **AI rout drags S&P into correction** — US stocks fell 3.7% as an AI
   sell-off hit chipmakers; the Nasdaq erased its 2026 gains.
5. **COP31 talks run past deadline** — The UN climate summit in Antalya,
   Turkey, ran into overtime as nearly 200 nations deadlocked over
   fossil fuels.
6. **FBI and USDA hit by hackers** — The FBI and the US Agriculture
   Department were hacked as computer outages hit strategic US sectors.
7. **Trump tells Europe: defund Ukraine** — After his summit with Putin,
   President Trump told European leaders to withhold funding from
   Ukraine.
8. **UK and EU sign post-Brexit deals** — PM Andy Burnham and EU leaders
   signed three deals on food exports, carbon markets and youth
   mobility.
9. **Storm kills 3, wrecks 5,000 homes** — A severe storm ravaged
   southern Brazil, killing three people and destroying about 5,000
   homes.
10. **Bayer pays $7.25bn over Roundup** — A US judge approved Bayer's
    $7.25 billion deal to settle all complaints linked to weedkiller
    Roundup.
11. **SEC opens probe into Nvidia** — The SEC opened an accounting probe
    into Nvidia as Trump urged a second chance for ex-CEO Jensen Huang.
12. **Gen Z protests spread in 25 nations** — Youth-led protests spread
    across 25 European countries, the largest wave of Gen Z unrest yet.
13. **Spain heads to 29 Nov election** — Spain heads to a 29 November
    election as conservatives gain ground in the polls.
14. **Also today: Anthropic mathematician claims an AI proof of the
    Riemann hypothesis** — a long-standing maths problem.
15. **Also today: Indonesia hit by massive forest fires.**
16. **Also today: Basra power plant fire kills at least four.**
17. **Also today: Morocco and Mali win big at the U-17 World Cup.**

Every story above was first reported on Saturday 21 November 2026.

## Sources (all published 21 November 2026)

- Reuters (via KTWB and others) — magnitude 6.8 earthquake strikes
  Banda Sea near Timor-Leste, 21 Nov 2026.
- GDACS (EU Joint Research Centre) — earthquake alerts for Peru
  (M6.7, 00:09 UTC) and China (M5.9), 21 Nov 2026.
- OneTurn.news — "World news today: AI Stock Rout, Russia Strikes,
  Genocide Ruling", 21 Nov 2026 (Russia/Poland, AI sell-off, COP31,
  UK–EU deals, Gen Z protests, Spain election).
- Horizon (horizonapp.link) — "World news and markets for 21 November
  2026" (FBI/USDA hacks, Bayer settlement, Indonesia forest fires,
  Basra fire, Riemann hypothesis claim).
- TFI Online / The Telegraph — "Trump tells Europe to defund Ukraine
  after Putin summit", 21 Nov 2026.
- Dainik Jagran English — "Severe Storm Ravages Southern Brazil, Kills
  3 and Destroys 5,000 Homes", 21 Nov 2026; "Trump Calls for Nvidia to
  Give Jensen Huang a Second Chance After CEO's Exit", 21 Nov 2026.
- particle.news — "Nvidia Board Keeps Jensen Huang Resignation in Place
  as Probes Multiply" (SEC probe reported 21 Nov 2026).
- iqmia — "Global News Summary – 2026-11-21" (crypto liquidations,
  West Bank city plan).
- Juba Global — South Sudan and world news for Saturday 21 November
  2026 (Morocco and Mali at the U-17 World Cup).
- The Watchers — "Strong M6.8 earthquake hits Kepulauan Barat Daya,
  Indonesia, near Timor-Leste", 21 Nov 2026.

## The program

`gen.py` draws `entry.png` with Python + PIL (Liberation fonts).
`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no randomness — two runs
write identical bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
