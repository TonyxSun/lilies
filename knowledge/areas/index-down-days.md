# Index big-down days — worker B, cycle 17 (2026-10-22 ~12:53 ET)
Cross-refs: ST-002 (single-stock big days are a coin flip), M-011/M-015 (VIX and trend regime), T-025 (200DMA timing fails as a standalone signal), BP-R1 (default no trade).

## Key findings
- **Today:** QQQ is down ~2.8% and SPY ~1.4% intraday, but both are still above their 200DMA (+4.4% and +5.5%) (DD-001).
- **After big down days in an uptrend,** the index has historically bounced over 10 days by about +0.9 pts more than normal (67% up vs 59%). This is weak evidence (t ~1.4), but the direction matches the "buy dips in uptrends" folklore. Below the 200DMA there is no bounce (DD-002).
- **No QQQ-vs-SPY catch-up** after QQQ lags on a down day (DD-003).

## Evidence strength
- B: a single source, events at least 6 days apart but 10-day windows can still overlap, t ~1.4, and the result is in-sample.
- The direction is consistent across SPY and QQQ and in the post-2010 subsample.

## What doesn't apply
- Single-stock dip buying, which is a coin flip (ST-002).
- Leveraged "buy the dip" plays (LE-R1).

## Rule candidates
- **DD-R1:** Don't de-risk the core because of a big down day while above the 200DMA. Forward returns after such days equal the base rate in every sample (DD-006), and selling after a drop is the disposition/panic error (DD-002, cf. R-013).
- **DD-R2:** At most, a big down day in an uptrend can bring forward an already-planned core purchase (e.g. finishing the 70% SPY/QQQ core). It can never justify a new satellite or a leveraged position (DD-002, BP-R1, LE-R1).
- **DD-R3:** Below the 200DMA, there's no dip edge, so stick to the plan (DD-002).

## Addendum, cycle 27 (2026-10-22): semis and NVDA dip-buys
- After an SMH ≤-5% day above its 200DMA (today's setup), the 10-day excess vs SPY was +2.1% (n=11, t 1.2). That is weak and does not meet MA-R1 (DD-004).
- NVDA after ≤-5% days performed no better than NVDA on any day (+1.1% vs +1.3% 10-day excess). A dip adds nothing beyond the ex-post-winner bias (DD-005).
- **DD-R4 (new):** No "buy the semis/NVDA dip" satellite today. If a semis satellite is already planned on other grounds, the dip does not justify upsizing it, and it is still subject to EH-R1/EVENT-GUARD (NVDA reports ~Nov 18, outside the window, unverified).

## Addendum, cycle 39: replication
- The DD-002 bounce does not replicate before 1999 (NDX 1985-99: +0.02% vs base, t 0.02; GSPC 1950-98: t -0.11) (DD-006). It is downgraded to "no edge".
- What survives across all samples: after a big down day in an uptrend, the next 10 days look like any other 10 days. **DD-R1 stands** (no de-risking). **DD-R2 is withdrawn** (bringing forward a planned core buy): there is no bounce to capture, so keep the original schedule.

## Addendum, cycle 40: global "Black Thursday"
- Today EEM is -3.1% and EWY -4.8%. The CSI 300 bear market is reported on X (unverified) (DD-007).
- Big EM or China down days in a US uptrend do not predict US weakness over 1-10 days (t ≤1.5 either way) (DD-008). DD-R1 still holds; no new rule.
