# News-driven small/mid caps (news sleeve): catalyst research

Owner: News/Fundamentals agent. **Trader owns the test, sizing and exits.** Per Trader's 1:47pm spec: 2-3% positions, 10% sleeve cap, max 3 names, benchmark IWM.
Tradable test: `tools/universe_check.py --profile news` (Tradable v2-news). It is **pending Wuyue's yes**, as is v1.
Wuyue's steer (1:46pm ET, 10/22): news gives the edge. Newer companies (about 4 quarters of history) and hyped names are allowed and weighed on story and potential. Hype is a flag, not a filter.

## Method (tools/smallcap_catalysts.py)
- Universe: NYSE/Nasdaq listings with market cap from UC.THRESH['mcap_min'] to $10B.
- Catalyst discovery:
  - EDGAR full-text search over 8-Ks from the last N days, using phrase classes: fda, contract, guidance_up, index_add.
  - Nasdaq earnings calendar, keeping surprises of at least 10% either way.
  - Insider buys: Form 4 transaction code P in the last 90 days, parsed from the XML. openinsider is blocked.
- Timing: the EDGAR "Accepted" time comes from the filing index. For earnings, the release time is assumed to be 16:05 ET.
- Attention read, from completed daily sessions after the event:
  - LATE if the return since the event is at least 15% or peak relative volume is at least 5x.
  - EARLY if there are 2 or fewer sessions, peak relative volume is under 3x and the return is under 8%.
  - MID otherwise.
  - **EARLY?** means no completed session yet. The reaction day is still running, so re-read it intraday.
- Then check X daily post counts (x.get_posts_counts_recent; `$` is stripped, so plain-word tickers are noisy). A spike above about 5x the prior-days baseline counts as LATE (S-002, NS-004).
- Gate: UC.check(sym, mkt, UC.edgar(...), profile='news'). Every verdict comes back "INCOMPLETE" because H5 (spread) needs a live quote, which I don't pass.

## Run 2026-10-22, about 1:52pm ET (window 10/15 to 10/22; cycles/08-smallcap-catalysts-2026-10-22.tsv)
- 56 raw events across 56 names: earnings_surprise 38, fda 9, guidance_up 4, index_add 4, contract 1. The top 40 by market cap were checked.
- News-mode verdicts:
  - 36 INCOMPLETE (H5 only).
  - 4 NOT TRADABLE: MANE H8n (<4 periodic filings), QS H2, AQST H2, ASIC H4 (ADV $2.0M).
- Flags: CLF J1/J2/J3; BHVN, FRNM, AVBP, SGMT J2 (vol); LOB H7 (late filing). Each needs a dated source before use.
- Reads: EARLY 12, EARLY? 21, MID 6, LATE 1 (MANE +25.6%).
- **Phrase false positive:** SUPN's "FDA approval" 8-K (accepted 10/21 9:07pm ET) was an orphan-exclusivity notice, not an approval (ir.supernus.com, 10/22). Read the text of every fda hit.
- **8-K lag:** the IONS approval news came out 10/20 (FDA release and Business Wire about 9:20pm ET 10/20), but the 8-K was accepted 10/21 at 4:15pm ET. EDGAR time can trail the news by about 19h, so time the event from the press release, not the 8-K.

## Live candidates (watch list, not trade calls; Trader decides)
| Ticker | Catalyst (dated source) | Price/volume since | X attention (UTC days) | Read | UC news | Thesis (one line) |
|---|---|---|---|---|---|---|
| HCSG ($1.5B) | Q3 EPS $0.36 vs $0.22 est (+64%); Q4 revenue guide $535-545M; 2027 growth raised to low double digits. Press release 10/21: investor.hcsgcorp.com/news/news-details/2026/Healthcare-Services-Group-Reports-Third-Quarter-Results/default.aspx | +10.2% on 10/22 intraday (21.71 to 23.93); volume 2x on 10/21 | about 3/day, then 39 (10/21), then 31 by 1:51pm 10/22: about 10x | MID turning LATE (reaction day in progress) | INCOMPLETE (H5); no flags | A guidance raise from a cash-rich services name. Edge only if drift beyond day 1; NS-002 says this size has no PEAD, so don't chase today; re-check 10/23 |
| WFRD ($6.1B) | Q3 EPS $1.66 vs $1.21 (+37%); Q4 revenue guide $1.28-1.33B vs Q3 $1.143B. 8-K 10/20: sec.gov/Archives/edgar/data/1603923/000160392326000118/a2026-q3ex991earningsrelea.htm | +7.8% on 10/21, then -5.6% on 10/22 | 3/day, then 35, then 67: about 20x spike | LATE | INCOMPLETE; no flags | Beat plus guide, but attention spiked and price is already giving back, matching the NS-004/S-002 reversal pattern. Avoid |
| IRDM ($4.7B) | Q3 EPS $0.38 vs $0.29 (+31%). Nasdaq calendar 10/20 | +0.7% on 10/21, -2.2% on 10/22: no reaction | 157 on 10/20, now 22-53: faded | EARLY on price, attention already spent | INCOMPLETE; no flags | A beat the market ignored. Only a case if guidance or KPIs back it; without that, NS-002 says no drift. Low priority |
| IONS ($7.4B) | GSK/Ionis Hibsago (bepirovirsen) FDA approval 10/20; Ionis gets 10-12% royalties plus milestones. FDA release 10/20: fda.gov/news-events/press-announcements/fda-approves-first-its-kind-chronic-hepatitis-b-treatment | -2.5% on 10/21, -0.9% on 10/22 | about 400/day baseline, 573 peak: 1.4x (noisy word) | Priced / sell-the-news | INCOMPLETE; no flags; director bought $1.06M on 7/30-31 at $51.6-53.4 (stock now $43.9) | NS-005: FDA approvals are priced by day +1. No edge from the event; the royalty ramp is a slow story, not a 2-week trade. Avoid |
| NPB ($0.52B; IPO 2025, about 6 quarters) | Q3 EPS $0.39 vs $0.60 (-35%), with a $3.1M fraud loss, $4.3M markdowns and a mortgage-channel sale. Business Wire 10/20: businesswire.com/news/home/20261020826020/en/ | -4.1% since; $15.38 | about 10/day, 18 peak: no spike | EARLY | INCOMPLETE; no flags | Contrarian insider: the CEO bought about $2.75M on 8/25-9/1 at about $16.8, above today's price (Form 4: sec.gov/Archives/edgar/data/1336706/000205756726000008/). NS-007 says this is an opportunistic-type buy, but NS-003 says bad-news drift is negative. Conflicting signals; watch only |

**Wider run (--max 60, cycles/08-smallcap-catalysts-2026-10-22-max60.tsv)** added the non-earnings hits:
- Guidance raises:
  - VMI (10/20 7:05am ET): -3.4% by 10/22.
  - WH (10/21 4:31pm ET): -1.3% on 10/22.
  - COCO (10/22 7:32am ET): FY26 sales raised to $810-820M (GlobeNewswire, 10/22), yet -4.4% today after a +7.5% run-up on 10/19-10/21, so it was priced before the print.
  - EQPT is LATE (+24%) and NOT TRADABLE (H8n).
- Index hits:
  - ZION, ADC, R and FBNC are earnings-release boilerplate. ZION is an existing S&P 400 member, not an add (NS-016).
  - Rule: only S&P DJI press releases count as index-add events.
- Contract: OPK is NOT TRADABLE (H2).

**Bottom line for 10/22:** no candidate is both EARLY and positive-surprise with intact price. HCSG is the best story but has turned MID/LATE intraday. Re-run on 10/23 before the open with `--days 3`.

## Evidence (INDEX NS-001..NS-007)
- NS-001 (A): Chordia et al. 2009. PEAD is concentrated in illiquid stocks, and trading costs eat 70-100% of it.
- NS-002 (A): Martineau 2022. Since 2006, PEAD is gone above the NYSE 20th percentile; since 2016, it's gone in microcaps too. Prices adjust within about 5 days or less.
- NS-003 (A): Chan 2003. Drift follows news, mostly bad news; no-news moves reverse. Strongest in small stocks.
- NS-004 (A): Da, Engelberg and Gao 2011. An attention spike gives about +30bp over 2 weeks, then reverses. S-002: buying after an attention spike loses about 4.7% the next month.
- NS-005 (B): FDA approvals show no drift after day +1.
- NS-006 (B): S&P 600 adds gain +4-9% on day 1, then reverse within 60 days.
- NS-007 (A): Cohen, Malloy and Pomorski 2012. Opportunistic insider buys earn about +90bp/month; routine buys earn nothing.
- UV-009/010 (B): quality junk veto. Over 12 months, the pass-minus-fail spread is about +9-10% in every size bucket. P(return below -50%) is 2-7% for passes vs 16-21% for fails, which matters for story names.

## Rules (testable)
- **NS-R1 (hot-candidate):** Buy only EARLY reads: within 2 sessions of the event, under 3x relative volume, under 8% move, and no X spike above 5x baseline. Never buy after an attention spike (NS-004, S-002).
- **NS-R2:** Time the event from the press-release timestamp, not the 8-K acceptance (IONS shows a 19h lag).
- **NS-R3:** Every fda, contract or index hit needs a human or text read before it counts (SUPN false positive).
- **NS-R4:** FDA approvals and index adds are not drift catalysts (NS-005, NS-006). Use them only for pre-event setups, which Trader owns.
- **NS-R5:** A name failing the quality veto (UV-009) gets a blow-up flag; the sizing consequence is Trader's call. Expect about 3x the rate of -50% outcomes.
- **NS-R6:** Weigh insider buys only if opportunistic (not the same month every year) and at least $100k. A CEO buying above the current price is a watch-list cue, not a trigger.
