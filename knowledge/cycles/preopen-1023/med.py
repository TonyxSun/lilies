import yfinance as yf, numpy as np, pandas as pd
tk=['SPY','QQQ','IWM','SMH','ITA','PSQ','^IRX']
d=yf.download(tk,start='1999-03-10',auto_adjust=True,progress=False)['Close']
px=d[['SPY','QQQ','IWM','SMH','ITA','PSQ']]
print('== M1 seasonal Oct22->Dec31 returns')
rows=[]
for y in range(1999,2026):
    try:
        s=px.loc[f'{y}-10-22':].index[0]; e=px.loc[:f'{y}-12-31'].index[-1]
        r=(px.loc[e]/px.loc[s]-1)*100; rows.append(r.rename(y))
    except: pass
R=pd.DataFrame(rows)
print(R[['SPY','QQQ','IWM','SMH','ITA']].describe().loc[['count','mean','50%','std']].round(2))
for a in ['QQQ','IWM','SMH','ITA']:
    x=(R[a]-R['SPY']).dropna(); print(a,'-SPY mean %.2f med %.2f beat %d/%d t %.2f'%(x.mean(),x.median(),(x>0).sum(),len(x),x.mean()/x.std()*np.sqrt(len(x))))
    x=(R[a]-(0.7*R['SPY']+0.3*R['QQQ'])).dropna(); print('   vs 70/30 mean %.2f beat %d/%d t %.2f'%(x.mean(),(x>0).sum(),len(x),x.mean()/x.std()*np.sqrt(len(x))))
print(R.tail(8).round(1))
# M2 switch
print('== M2 QQQ/cash/PSQ switch on 200DMA (signal on close, trade next close, 0.15%/side cost, cash earns 13w T-bill)')
q=px['QQQ']; ma=q.rolling(200).mean(); sig=(q>ma).astype(int).shift(1)
rq=q.pct_change(); rp=px['PSQ'].pct_change(); rf=(d['^IRX']/100/252).shift(1).fillna(0)
for mode in ['cash','psq']:
    alt= rf if mode=='cash' else rp.fillna(-rq)
    strat=np.where(sig==1,rq,alt); strat=pd.Series(strat,index=q.index)
    trades=sig.diff().abs().fillna(0); strat=strat-trades*0.0015*(1 if mode=='cash' else 2)
    s=strat['2000-01-01':].dropna(); b=rq['2000-01-01':].dropna()
    for lab,a,z in [('2000-2026',None,None),('2010-2026','2010','2026')]:
        ss=s[a:] if a else s; bb=b[a:] if a else b
        cagr=lambda r:( (1+r).prod()**(252/len(r))-1)*100
        mdd=lambda r:((1+r).cumprod()/(1+r).cumprod().cummax()-1).min()*100
        print(mode,lab,'CAGR %.1f%% vs QQQ %.1f%% | maxDD %.0f%% vs %.0f%% | switches/yr %.1f'%(cagr(ss),cagr(bb),mdd(ss),mdd(bb),trades[ss.index].sum()/len(ss)*252))
    # Oct22-Dec31 windows
    ex=[]
    for y in range(2000,2026):
        w=s[f'{y}-10-22':f'{y}-12-31']; wb=b[f'{y}-10-22':f'{y}-12-31']
        ex.append(((1+w).prod()-(1+wb).prod())*100)
    ex=np.array(ex); print('   Oct22-Dec31 excess vs QQQ mean %.2f beat %d/%d'%(ex.mean(),(ex>0).sum(),len(ex)))
print('now: QQQ',round(q.iloc[-1],2),'200DMA',round(ma.iloc[-1],2), q.index[-1].date())
# M3 SMH big down day
print('== M3 SMH day <= -5%: forward excess vs QQQ (enter next close), declustered 20d')
rs=px['SMH'].pct_change(); ev=[]; last=None
idx=list(px.index)
for i,(t,v) in enumerate(rs.items()):
    if v<=-0.05 and (last is None or i-last>20) and i+51<len(idx):
        last=i; e=i+1
        out={}
        for H in (10,21,50):
            out[H]=(px['SMH'].iloc[e+H]/px['SMH'].iloc[e]-px['QQQ'].iloc[e+H]/px['QQQ'].iloc[e])*100
            out['abs%d'%H]=(px['SMH'].iloc[e+H]/px['SMH'].iloc[e]-1)*100
        out['date']=t; ev.append(out)
E=pd.DataFrame(ev)
for sub,lab in [(E,'all'),(E[E.date>='2010'],'2010+')]:
    for H in (10,21,50):
        x=sub[H]; print(lab,H,'n %d mean excess %.2f med %.2f hit %.0f%% t %.2f | abs mean %.2f'%(len(x),x.mean(),x.median(),(x>0).mean()*100,x.mean()/x.std()*np.sqrt(len(x)),sub['abs%d'%H].mean()))
