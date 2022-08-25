## 1 ##
from pandas import  pandas as dt
print(dt.now())
print(dt.now().days)
print(dt.now().year)

##2 ##
import random
plot = sns.lineplot(
x="date",
y="value",
hue='variable',
data=pd.melt(df_mcd, ['date'])
)
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)
