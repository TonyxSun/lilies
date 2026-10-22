# Earnings-season playbook — warm digest (owner 牛马; new area, pass 1+2, 2026-10-22 12:36pm ET)
Ids ES-. Builds on fundamentals (F-), macro calendar (M-014, M-020) and news (N-).

## Findings
1. **Past winners run up into earnings, then give it back [A].** Top prior-12-month winners earn +1.58% in the 5 days before the report and −1.86% in the 5 days after, which survives costs. It's an attention effect, not information (ES-001). Lottery-like names show the same thing (+85–107 bp in the 10 days before, ES-002). The bubble-era internet sample was far larger (ES-003, cold).
2. **The pre-EA run-up is the mirror of FC-5.** We don't buy into earnings. The stronger insight is for names we *already hold*: high-momentum holdings are statistically weak in the week after their report.
3. **IV crush doesn't matter for stock holders** (ES-004, reasoning). What matters is the realized move vs the stop. Large-cap implied moves are roughly unbiased (M-017), so use the implied move to judge whether the position can survive the gap.
4. **LLM reading of calls and guidance [B]:** contextual or Q&A features beat raw sentiment, and positive tone mostly shows up in the overnight/day-0 return (ES-005). The tradable part for us is the *filter* (FC-1): read guidance and the Q&A, and stand aside if they're negative, even when the stock popped.
5. **Earnings-season concentration:** the Oct 28–Nov 2 mega-cap cluster (M-014) sets QQQ's path. Today's examples show beats being sold and guidance driving the reaction (ES-006, C).

## Doesn't apply
- Straddles and IV trades (no options).
- Short-selling the post-EA reversal.

## Rule candidates
- **ES-R1:** Don't open a position in a top-decile 12-month winner within 5 trading days *after* its earnings, because the reversal averages about −1.9% (ES-001). Test by logging candidates and their +5d abnormal return.
- **ES-R2:** For a held name with earnings within 2 sessions, require that implied move × position weight ≤ the per-position loss budget. Otherwise trim before the report (ES-004, M-017, F-019).
- **ES-R3:** After a report, summarize guidance and the Q&A with the LLM on anonymized text. A guidance cut or negative Q&A tone vetoes entry regardless of the price reaction (ES-005, F-017, N-006).

## Pass 3: own test on megacaps, 2021–26 (12:40pm ET; tools/pead_test.py; events in cycles/05-largecap-pead-events.tsv)
The sample is 808 earnings 8-Ks (item 2.02) across 44 current megacaps. Timing comes from the EDGAR acceptance timestamp, and prices are Yahoo adjusted closes.
- **Weak continuation survives:** the top-minus-bottom day-1 tercile spread is +1.12% over the next 10 days. Season-clustered, that's t=2.0 and positive in 13 of 19 seasons (ES-007). This is in-sample and has survivorship bias, so grade it B at most.
- **Asymmetric for a long-only book:**
  - A reaction above +5% is followed by +1.26% over 10 days (t 1.95).
  - A reaction below −5% is followed by −0.41%, with a 43% hit rate (ES-008).
- **No announcement premium** in megacaps: mean +0.06%. Mean |day-1 excess| is 4.4% (ES-009).
- **The pre-earnings run-up reversal doesn't show up** (ES-010).

### Rules
- **ES-R4:** never buy a megacap within 10 sessions of an earnings drop of more than 5% vs SPY ("dip-buying"). A rise of more than 5% vs SPY on earnings is a reason to keep holding, not to take profit. You may buy it from day 2, but not at the open (Berkman, N-024).
- **ES-R5:** holding through earnings is a variance bet of about 4.4% vs SPY with zero expected premium. Allow it only at a reduced size set by Trader.

### Pass 3b: robustness check (12:43pm ET). It overturns part of the above.
- **Second universe:** 38 other large caps, including laggards (660 events). The positive-continuation leg disappears:
  - top-minus-bottom spread −0.28%
  - a reaction above +5% is followed by +0.06%
- **ES-007 and ES-008's positive leg was survivorship (ES-011).** ES-007 is demoted to C/warm.
- **What survives in both samples:** after an earnings drop of more than 5% vs SPY, the next 10 days run −0.41% and −0.61%, with hit rates of 43% and 38%. That's weak but consistent.
- **ES-R4 is revised:** keep "no dip-buying for 10 sessions after an earnings drop of more than 5%." Drop "a big rise is a reason to hold or buy."

### Pass 4: gap vs intraday (12:52pm ET; tools/gap_test.py)
- **Sample:** 1,468 events. 86% of the day-1 move vs SPY is in the opening gap. There's no open-to-close continuation (corr −0.01).
- **After a gap-up of more than 7%:** −0.46% from open to close, with a 36% hit rate (ES-012).
- **ES-R6:** never buy an earnings gap-up at or near the open. A reaction we see after the open isn't actionable as momentum; at most it's information for the day-2+ rules (ES-R4).

### Pass 5: name-level earnings variance for this window's reporters (12:57pm ET)
- **Mean |day-1| vs SPY for this window's reporters:**

  | Ticker | Report date | Mean \|day-1\| |
  |---|---|---|
  | AMZN | 10/29 | 7.1% |
  | MSFT | 10/28 | 4.9% |
  | GOOGL | 10/28 | 4.9% |
  | AAPL | 11/2 | 2.8% |

  Each is up about 50% of the time (ES-013).
- **ES-R5 in numbers:** holding AMZN through 10/29 is roughly a ±7% coin flip vs SPY. Trader should size this.
- **Data caveat:** the item-2.02 filter double-counts some issuers (ABBV) and misses others (XOM).
