import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('covid19.csv')
df.columns = df.columns.str.strip() # Get rid of trailing spaces in column names
df.replace([np.inf], 0, inplace=True) # gets rid of some infinities
print(df['Confirmed'].describe().apply(lambda x: format(x, 'f'))) # the apply stops scientific notation
print(df['Deaths'].describe().apply(lambda x: format(x, 'f')))
print(df['Recovered'].describe().apply(lambda x: format(x, 'f')))
print(df['Active'].describe().apply(lambda x: format(x, 'f')))
print(df['New cases'].describe().apply(lambda x: format(x, 'f')))
print(df['New deaths'].describe().apply(lambda x: format(x, 'f')))
print(df['New recovered'].describe().apply(lambda x: format(x, 'f')))
print(df['Deaths / 100 Cases'].describe().apply(lambda x: format(x, 'f')))
print(df['Recovered / 100 Cases'].describe().apply(lambda x: format(x, 'f')))
print(df['Deaths / 100 Recovered'].describe().apply(lambda x: format(x, 'f')))
print(df['Confirmed last week'].describe().apply(lambda x: format(x, 'f')))
print(df['1 week change'].describe().apply(lambda x: format(x, 'f')))
print(df['1 week % increase'].describe().apply(lambda x: format(x, 'f')))
"""
count        187.000000
mean       88130.935829
std       383318.663831
min           10.000000
25%         1114.000000
50%         5059.000000
75%        40460.500000
max      4290259.000000
Name: Confirmed, dtype: object
count       187.000000
mean       3497.518717
std       14100.002482
min           0.000000
25%          18.500000
50%         108.000000
75%         734.000000
max      148011.000000
Name: Deaths, dtype: object
count        187.000000
mean       50631.481283
std       190188.189643
min            0.000000
25%          626.500000
50%         2815.000000
75%        22606.000000
max      1846641.000000
Name: Recovered, dtype: object
count        187.000000
mean       34001.935829
std       213326.173371
min            0.000000
25%          141.500000
50%         1600.000000
75%         9149.000000
max      2816444.000000
Name: Active, dtype: object
count      187.000000
mean      1222.957219
std       5710.374790
min          0.000000
25%          4.000000
50%         49.000000
75%        419.500000
max      56336.000000
Name: New cases, dtype: object
count     187.000000
mean       28.957219
std       120.037173
min         0.000000
25%         0.000000
50%         1.000000
75%         6.000000
max      1076.000000
Name: New deaths, dtype: object
count      187.000000
mean       933.812834
std       4197.719635
min          0.000000
25%          0.000000
50%         22.000000
75%        221.000000
max      33728.000000
Name: New recovered, dtype: object
count    187.000000
mean       3.019519
std        3.454302
min        0.000000
25%        0.945000
50%        2.150000
75%        3.875000
max       28.560000
Name: Deaths / 100 Cases, dtype: object
count    187.000000
mean      64.820535
std       26.287694
min        0.000000
25%       48.770000
50%       71.320000
75%       86.885000
max      100.000000
Name: Recovered / 100 Cases, dtype: object
count     187.000000
mean       39.473850
std       332.178192
min         0.000000
25%         1.295000
50%         3.510000
75%         6.190000
max      3259.260000
Name: Deaths / 100 Recovered, dtype: object
count        187.000000
mean       78682.475936
std       338273.676567
min           10.000000
25%         1051.500000
50%         5020.000000
75%        37080.500000
max      3834677.000000
Name: Confirmed last week, dtype: object
count       187.000000
mean       9448.459893
std       47491.127684
min         -47.000000
25%          49.000000
50%         432.000000
75%        3172.000000
max      455582.000000
Name: 1 week change, dtype: object
count    187.000000
mean      13.606203
std       24.509838
min       -3.840000
25%        2.775000
50%        6.890000
75%       16.855000
max      226.320000
Name: 1 week % increase, dtype: object
"""