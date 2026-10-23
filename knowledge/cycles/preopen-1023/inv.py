import yfinance as yf, numpy as np, pandas as pd
pairs=[('SH','SPY',-1),('PSQ','QQQ',-1),('QID','QQQ',-2),('SQQQ','QQQ',-3),('RWM','IWM',-1),('SRTY','IWM',-3),('QLD','QQQ',2)]
tk=sorted({a for a,_,_ in pairs}|{b for _,b,_ in pairs})
d=yf.download(tk,start='2010-03-01',auto_adjust=True,progress=False)['Close']
r=d.pct_change()
for a,b,k in pairs:
    x=r[[a,b]].dropna()
    for H in (5,10):
        ga=(1+x[a]).rolling(H).apply(np.prod,raw=True)-1; gb=(1+x[b]).rolling(H).apply(np.prod,raw=True)-1
        vol=x[b].rolling(H).std()*np.sqrt(252)
        dd=pd.DataFrame({'ga':ga,'gb':gb,'vol':vol}).dropna(); dd['gap']=dd.ga-k*dd.gb
        hv=dd[dd.vol>dd.vol.quantile(.8)]
        print(f"{a} vs {k}x{b} H={H}d n={len(dd)} start={x.index[0].date()} gap mean {dd.gap.mean()*100:.2f}% med {dd.gap.median()*100:.2f}% highvol(>{dd.vol.quantile(.8)*100:.0f}%) mean {hv.gap.mean()*100:.2f}% | P(fund up) {(dd.ga>0).mean()*100:.0f}% fund p5 {dd.ga.quantile(.05)*100:.1f}% p95 {dd.ga.quantile(.95)*100:.1f}%")
print('last date', d.index[-1])
