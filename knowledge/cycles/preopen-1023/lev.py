import yfinance as yf, numpy as np, pandas as pd, datetime as dt
d=yf.download(['QQQ','QLD','TQQQ','^VXN'],start='2010-02-11',auto_adjust=True,progress=False)['Close'].dropna()
r=d[['QQQ','QLD','TQQQ']].pct_change().dropna()
H=10
out=[]
for k,name in [(2,'QLD'),(3,'TQQQ')]:
    lq=np.log1p(r['QQQ']); 
    gq=(1+r['QQQ']).rolling(H).apply(np.prod,raw=True)-1
    gl=(1+r[name]).rolling(H).apply(np.prod,raw=True)-1
    vol=r['QQQ'].rolling(H).std()*np.sqrt(252)
    dfx=pd.DataFrame({'gq':gq,'gl':gl,'vol':vol}).dropna()
    dfx['decay']=dfx.gl-k*dfx.gq
    dfx['excess']=dfx.gl-dfx.gq
    q=dfx.vol.quantile([.5,.8])
    print(name,'n',len(dfx),'decay mean %.2f%% med %.2f%%'%(dfx.decay.mean()*100,dfx.decay.median()*100),
      'decay when vol>p80(%.0f%%): mean %.2f%%'%(q[.8]*100,dfx[dfx.vol>q[.8]].decay.mean()*100),
      'excess vs QQQ p5 %.1f%% p50 %.1f%% p95 %.1f%%'%tuple(dfx.excess.quantile([.05,.5,.95])*100),
      'P(beat QQQ) %.0f%%'%((dfx.excess>0).mean()*100), 'lev p5 %.1f%%'%(dfx.gl.quantile(.05)*100), 'worst %.1f%%'%(dfx.gl.min()*100))
print('last VXN',d['^VXN'].iloc[-1], d.index[-1].date(), 'QQQ 20d realized vol %.1f%%'%(r['QQQ'][-20:].std()*np.sqrt(252)*100))
