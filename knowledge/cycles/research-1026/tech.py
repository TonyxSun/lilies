import yfinance as yf, pandas as pd, numpy as np, datetime, json
syms="ELV LMT TXN IWM XLE BNO SMH GLD SH BAH BCPC TLT".split()
d=yf.download(syms+["QQQ","SPY"],period="320d",auto_adjust=True,progress=False)
C=d["Close"];H=d["High"];L=d["Low"];V=d["Volume"];O=d["Open"]
r=C.pct_change()
out=[]
for s in syms:
    c=C[s].dropna()
    tr=pd.concat([H[s]-L[s],(H[s]-C[s].shift()).abs(),(L[s]-C[s].shift()).abs()],axis=1).max(axis=1)
    atr=tr.rolling(14).mean().iloc[-1]
    row=dict(sym=s,last_date=str(c.index[-1].date()),close=round(c.iloc[-1],2),sma50=round(c.rolling(50).mean().iloc[-1],2),sma200=round(c.rolling(200).mean().iloc[-1],2),
      ret5=round(100*(c.iloc[-1]/c.iloc[-6]-1),2),ret20=round(100*(c.iloc[-1]/c.iloc[-21]-1),2),hi20=round(c.iloc[-20:].max(),2),hi252=round(c.iloc[-252:].max(),2),
      atr14=round(atr,2),atr_pct=round(100*atr/c.iloc[-1],2),relvol=round(V[s].iloc[-1]/V[s].iloc[-21:-1].mean(),2),
      gap_today=round(100*(O[s].iloc[-1]/C[s].iloc[-2]-1),2),corrQQQ60=round(r[s].iloc[-60:].corr(r["QQQ"].iloc[-60:]),2),corrSPY60=round(r[s].iloc[-60:].corr(r["SPY"].iloc[-60:]),2))
    try:
        t=yf.Ticker(s); exps=t.options
        today=datetime.date(2026,10,23)
        e=[x for x in exps if (datetime.date.fromisoformat(x)-today).days>=7][0]
        ch=t.option_chain(e); px=c.iloc[-1]
        k=ch.calls.iloc[(ch.calls.strike-px).abs().argsort()[:1]].strike.values[0]
        cm=ch.calls[ch.calls.strike==k]; pm=ch.puts[ch.puts.strike==k]
        def mid(x): 
            b,a=x.bid.values[0],x.ask.values[0]; return (b+a)/2 if a>0 else x.lastPrice.values[0]
        st=mid(cm)+mid(pm)
        row.update(opt_exp=e,straddle=round(st,2),impl_move_pct=round(100*st/px,2),iv_call=round(cm.impliedVolatility.values[0],3))
    except Exception as ex: row.update(opt_err=str(ex)[:60])
    try:
        cal=yf.Ticker(s).calendar; ed=cal.get("Earnings Date") if isinstance(cal,dict) else None
        row["next_earn"]=str(ed[0]) if ed else ""
    except Exception: row["next_earn"]="?"
    out.append(row)
df=pd.DataFrame(out); df.to_csv("tech.csv",index=False); print(df.to_string())
print("QQQ",C.QQQ.iloc[-1],C.QQQ.rolling(200).mean().iloc[-1],"SPY",C.SPY.iloc[-1])
