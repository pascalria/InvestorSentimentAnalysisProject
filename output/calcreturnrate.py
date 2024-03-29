import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

index = pd.read_csv(r'E:\resources\project\bert\bert-master\data_collection\saved\sz399006.csv')
merged = pd.read_csv(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\merged.csv')
merged.rename(columns={'Upload Time': 'Date'}, inplace=True)
index['Date'] = pd.to_datetime(index['Date']).dt.date
merged['Date'] = pd.to_datetime(merged['Date']).dt.date
index.set_index('Date', inplace=True)
index['Return'] = index['Close'].pct_change()

start_date = pd.to_datetime('2023-12-29').date()
end_date = pd.to_datetime('2020-1-1').date()

sub_index =  index.loc[(index.index >= end_date) & (index.index <= start_date)]
print(sub_index.head)

total = pd.merge(merged, index, on='Date', how='left')

print(total.head)

for i in range(len(total)-1):
    if np.isnan(total.iloc[i,4]):
        total.iloc[i+1,1] = total.iloc[i+1,1] + total.iloc[i,1]
        total.iloc[i+1,2] = total.iloc[i+1,2] + total.iloc[i,2]

total.dropna(subset=['Open'], inplace=True)
total['norm index'] = total['index'] / total['Read']
print(total.head)
total.to_csv(r'final.csv', index=False)

plt.scatter(total['Return'],total['norm index'])
plt.show()


# plt.scatter(total['Trans'],total['norm index'])
# plt.show()

# plt.scatter(total['Trans'],total['Return'])
# plt.show()