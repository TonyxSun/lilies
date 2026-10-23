import yfinance as yf, pandas as pd, numpy as np
syms="QQQ SPY IWM SMH SH PSQ QID SQQQ RWM SRTY QLD TQQQ VOO QQQM MSFT GOOGL AMZN META".split()
d=yf.download(syms,start="2010-01-01",auto_adjust=True,progress=False)["Close"]
last=yf.download(syms,period="5d",auto_adjust=False,progress=False)["Close"].iloc[-1]
print("closes", last.index.name, {s:round(float(last[s]),2) for s in syms})
r=d.pct_change()
# proxy for bad hyperscaler guidance: MSFT/GOOGL/AMZN/META single-day <= -5% while QQQ down less than half that (idiosyncratic) 
ev=[]
for s in ["MSFT","GOOGL","AMZN","META"]:
    x=r[s]; q=r["QQQ"]
    idx=x[(x<=-0.05)&(q> x/2)].index
    ev+= [(i,s) for i in idx]
ev=sorted(ev); keep=[];lastd=None
for i,s in ev:
    if lastd is None or (i-lastd).days>14: keep.append((i,s)); lastd=i
res=[]
for i,s in keep:
    k=d.index.get_loc(i)
    if k+10<len(d):
        q10=d["QQQ"].iloc[k+10]/d["QQQ"].iloc[k]-1
        q5=d["QQQ"].iloc[k+5]/d["QQQ"].iloc[k]-1
        res.append((q5,q10))
a=np.array(res); n=len(a)
for j,h in enumerate([5,10]):
    m=a[:,j].mean(); t=m/(a[:,j].std(ddof=1)/np.sqrt(n))
    print(f"QQQ next {h}d after event-close: n={n} mean {100*m:+.2f}% t {t:.2f} P(down) {100*(a[:,j]<0).mean():.0f}%")
# unconditional
for h in [5,10]:
    u=(d["QQQ"].shift(-h)/d["QQQ"]-1).dropna(); print(f"uncond QQQ {h}d mean {100*u.mean():+.2f}% P(down) {100*(u<0).mean():.0f}%")
