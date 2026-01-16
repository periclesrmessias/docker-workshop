import sys

import pandas as pd

df = pd.DataFrame({"A": [1, 2], "Number of Passengers": [3, 4]})
month = int(sys.argv[1])
df['month'] = month

df.to_parquet(f'output_{month}.parquet')
print(df.head())

print('Arguments', sys.argv)



print(f'Hello Pipeline, month={month}')