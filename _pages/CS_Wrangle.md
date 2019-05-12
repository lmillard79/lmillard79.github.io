---
permalink: /cheatsheets/CS_Wrangle/
title: Data Wrangling tips
author_profile: False

sidebar:
  title: "Top Tips"
  nav: sidebar-sample
---

## Markdown Syntax used in this Blog  
### Mainly for my reference as I can't remember anything

```python
nparr = np.zeros((15,2))

for i, l in enumerate(lst):    
    print i
    c = 0
    fold = os.path.join(inpath,l)
    files = os.listdir(fold)
    for f in files:        
        if f.endswith('i.csv'):            
            fin = os.path.join(fold,f)
            df = pd.read_csv(fin,i
            d1 = df.sum(axis=1)
            mx = d1.max(axis=0)
            nparr[c,i] = mx
            arr.append(m1)
```

```python
dfQ = pd.read_table(Q, skipfooter=2, skipinitialspace=True, delimiter=',', index_col=None, skiprows=(0,3,4,5,6), header=[0,1])
m = []
ls = dfQ.columns.get_level_values(0).tolist()
for i, item in enumerate(ls):
    if len(item[1])<2:
        #print i, item[1]
        m.append(i)
    elif len(item[1])>15:
        #print i, item[1]
        m.append(i)
dfQ.drop(dfQ.columns[m],axis=1,inplace=True)
dfQ.ix[:,~dfQ.columns.duplicated()]
dfQ.columns = pd.MultiIndex.from_tuples(dfQ.columns.tolist())
```

```python
for n, line in enumerate(p):      
    if "River Levels" in line:
        WL_start = int(n)
    if "Flow Rates  " in line:
        Q_start = int(n)
    if "PARAMETER data" in line:
        param_start = int(n)
count = 0
```

```python
## - Standard Normal Deviate 
dfRES_24mrg['Z'] = -1*scipy.stats.norm.ppf(dfRES_24mrg['aep%'])
```

List Comprehension
```python
flist = [f for f in os.listdir(inpath) if f.endswith('.csv') and f.startswith(evt)]
```