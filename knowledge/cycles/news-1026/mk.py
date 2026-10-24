import yfinance as yf, pandas as pd, datetime
syms="BAH BCPC LMT TXN ELV ALV GNTX".split()
rows=[];oh=[]
d=yf.download(syms,period="400d",auto_adjust=False,progress=False)
for s in syms:
    i=yf.Ticker(s).info
    c=d["Close"][s].dropna(); v=d["Volume"][s].dropna()
    adv=float((c*v).iloc[-30:].mean())
    b,a=i.get("bid"),i.get("ask")
    sp=(a-b)/((a+b)/2) if b and a and a>b>0 else ""
    r=c.pct_change()
    rows.append(dict(symbol=s,price=float(c.iloc[-1]),market_cap=i.get("marketCap"),adv_usd=round(adv),spread_pct=round(sp,5) if sp!="" else "",max_ret_21d=round(float(r.iloc[-21:].max()),4),vol_63d=round(float(r.iloc[-63:].std()*252**.5),4)))
    print(s,"bid",b,"ask",a,"200d",round(c.iloc[-200:].mean(),2),"close",round(c.iloc[-1],2),"prev",round(c.iloc[-2],2), "5d", round(100*(c.iloc[-1]/c.iloc[-6]-1),2), "52wH", round(c.iloc[-252:].max(),2))
    for dt_,cc,vv in zip(c.index[-260:],c.iloc[-260:],v.reindex(c.index).iloc[-260:]): oh.append(dict(date=dt_.date(),symbol=s,close=cc,volume=vv))
pd.DataFrame(rows).to_csv("market.csv",index=False); pd.DataFrame(oh).to_csv("ohlcv.csv",index=False)
print(pd.DataFrame(rows).to_string()); print(datetime.datetime.now())
