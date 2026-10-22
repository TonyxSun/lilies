# Catalyst calendar Oct 23-30, 2026, with pre-registered EARLY/LATE criteria (owner 牛马; written 10/22 about 2:20pm ET)
Trader owns the tradable test (`universe_check.py --profile news`, pending Wuyue's yes), sizing and exits. This file only fixes which events to watch and how each one will be read, before the event happens.

## Macro (ET; areas/macro-regime.md)
- Wed 10/28: FOMC statement at 2:00pm, presser at 2:30pm. No new single-stock entries 1:30-3:00pm (MR-3).
- Thu 10/29, 8:30am: GDP Q3 advance and Sep PCE.
- Fri 10/30, 8:30am: Q3 Employment Cost Index.
- MR-3: index exposure stays on through all of these.

## Megacaps (≥$200B; core/QQQ names; Tradable v1; MR-4: no opening or adding in the 2 sessions before each report; expected |move| 4.4%, UV-008)
| Date | Before open | After close |
|---|---|---|
| Fri 10/23 | AXP | |
| Tue 10/27 | KO, NVS | V (HSBC time n/a) |
| Wed 10/28 | GEV | **MSFT, GOOGL**, KLAC (FOMC day) |
| Thu 10/29 | LLY, MA, MRK, CAT, SHEL, LIN | **AMZN**, INTC, SNDK |
| Fri 10/30 | XOM, ABBV, CVX, AZN | |
| Mon 11/2 | | AAPL (outside this file's range) |

## Sleeve-range reporters (tools/catalyst_calendar.py; cycles/09-catalyst-calendar-2026-10-23_30.tsv, plus -part2.tsv for smaller names)
- **Universe:** 773 NYSE/Nasdaq reports from 10/23 to 10/30 above the $300M floor: mega 22, large 268, mid 269, small 214.
- **Part 1 (the 150 largest mid/small names, about $4-10B):**
  - 130 TRADABLE-NEWS (mechanical part; spread snapshot at about 2:05-2:20pm ET 10/22, which must be re-checked at order) and 20 NOT TRADABLE.
  - Of the 20 failures, 17 are mostly foreign filers: H6 and/or H8n on 20-F/40-F filers (MMYT, KOF, EDU, EGO, VIST, ASR, SIMO, STNG, TFII, BVN, TAL, WFG, MEOH, CGAU, SIM) or too few periodic filings (CBC, JMKE).
  - The rest: H5 spread over 0.5% (HRI 0.66%, LGND 0.67%) and H9 (GVA).
  - Hype flags, which need a dated news source before any use: J2 on CVLT, GLXY, FORM, PSN, TENB, PBF; J1+J2 on OPCH.
- **Passing names by report date** (time, frozen 20-day ADV):
  - 10/23 (BMO): BAH, ALV, BCPC, RITM, FLG, GNTX.
  - 10/26 (AMC): BRX, SSD, ARE, NE, PSMT, PECO.
  - 10/27: 20 names, including RGEN, PNR, CVLT, GLXY (BMO) and BXP, ZWS, STAG, NOV, CHE, EXLS (AMC).
  - 10/28: 36 names, including OGE, LFUS, EVR, PB, ETSY, EAT (BMO) and MUSA, AM, FLS, HLI, FORM, NEU (AMC).
  - 10/29: 52 names, including CFR, PBF, DAR, LTH, SIRI, SAIA, OSK, AOS (BMO) and CUBE, SPXC, MHK (AMC).
  - 10/30: 10 names, including FRT, GTES, OMF, LEA, AN, PIPR (BMO).
  - The full list with frozen thresholds is in the TSV.

- **Part 2 (200 names, $1.0-4.1B, no spread snapshot, so H5 is checked at decision; -part2.tsv):**
  - 184 INCOMPLETE (every checked hard row passes) and 16 NOT TRADABLE (10 foreign filers on H6/H8n, 5 H2, 1 H8n).
  - Flags: J2 on 21 names, including VKTX, WING, TDOC, BHC, ULCC, AXTI; J1 on 2.
  - H7 late filing: MCHB, DAN, HUBG. Each flag needs a dated news source before use.
  - Counts by date: 10/23 4 (FHB, GRC, RBCAA, TMP); 10/26 20; 10/27 37; 10/28 51; 10/29 68; 10/30 4.
- **Part 3** ($300M-1B, -part3.tsv), 133 names: 91 INCOMPLETE (spread unchecked) and 42 NOT TRADABLE (H4 x21, mostly thin ADV; H2 x19; H8n x11; H6 x9). Flags: J2 x19, J1 x3, H7 on CLB, RJET and XRX. About 1 in 3 names under $1B fail before the spread check (CC-006).

## PRE-REGISTERED read (frozen 10/22; tools/read_preregistered.py applies it mechanically)
- **Event time:** the press-release time. BMO reports react the same day; AMC or unknown react the next weekday (NS-R2).
- **Baselines:** `base_dvol_m` (20-day mean $ volume before 10/22) is frozen in the TSV. The X baseline is the mean posts/day over the 5 days before the event (agent, x.get_posts_counts_recent; plain-word tickers are noisy).
- **EARLY:** all of the following. EARLY is eligible for Trader's review only with positive news (a beat plus raised or maintained guidance, read from the 8-K).
  - The decision falls on or before `early_deadline`, i.e. ≤2 completed sessions.
  - Every session's $ volume is below `early_dvol_cap_m` (3× base).
  - |return since the pre-event close| < 8%.
  - X posts/day < 5× the X baseline.
- **LATE:** any of the following. LATE means do not buy (NS-004, S-002).
  - Return ≥ +15%.
  - Any session's $ volume ≥ `late_dvol_m` (5× base).
  - X ≥ 5× baseline.
- **MID:** anything else. No entry; re-read the next session.
- **Cost gate:** the measured spread at decision time must be ≤0.5% (H5). The typical round trip is 0.17-0.27% (NS-018/019).
- **Logging:** every read goes into INDEX.tsv (forward log) with the 10-day excess vs IWM recorded afterwards. This is the evidence that change-our-mind item 2 needs.
- **Frozen:** no threshold may change after 10/22; any change ships as a new dated version.

## Tomorrow (10/23), mechanically
1. After the 10/23 close: `python3 tools/read_preregistered.py cycles/09-catalyst-calendar-2026-10-23_30.tsv --x T=ratio ...` covers BAH, ALV, BCPC, RITM, FLG, GNTX, AXP.
2. `python3 tools/smallcap_catalysts.py --days 3 --spread` picks up unscheduled 8-K catalysts.
3. Read the direction of each event from the 8-K and log it.

## Pre-registered X baselines for the 10/23 reporters (x.get_posts_counts_recent; mean of full UTC days 10/17-10/21; pulled 10/22 at 2:23pm ET)
| Ticker | X baseline posts/day | LATE if posts/day ≥ |
|---|---|---|
| BCPC | 25.8 | 129 |
| RITM | 186 | 930 |
| FLG | 232 (partly noise) | 1160 |
| GNTX | 49 | 245 |
| BAH | about 37,000: the plain word "bah" makes it unusable | X criterion n/a; volume and price only |
| ALV | about 10,900: slang noise | X criterion n/a; volume and price only |

## Own test of the pre-registered read (CC-007, B)
`tools/attention_test.py` -> cycles/09-attention-test.txt. This covers 3,585 past earnings 8-Ks (Item 2.02) of 314 current sleeve names. The metric is the next-10-session excess return vs IWM, entering at the decision-session close.

| group | n | mean | median | hit | t(event) |
|---|---|---|---|---|---|
| EARLY-up | 1135 | -0.19% | -0.66% | 45% | -1.08 |
| MID-up | 426 | -0.32% | -0.65% | 45% | -0.88 |
| LATE-up | 253 | +0.27% | -0.52% | 48% | 0.41 |
| down | 1771 | -0.12% | -0.33% | 48% | -0.71 |

None of the groups is significant after week clustering. On price and volume alone, the EARLY label has no edge, and it does not beat LATE. The X leg could not be tested. Survivorship bias (we only tested current names) favors longs, which makes the null result stronger. **Implication:** run tomorrow's mechanical read as a paper log only. It does not support a live entry until a forward record (CM-R1) shows otherwise.

Footer: parts 1-3 complete. 483 sleeve names checked in total. Finalized 2:28pm ET 10/22.
