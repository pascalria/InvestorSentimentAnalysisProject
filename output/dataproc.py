# 处理bert预测的概率tsv，将其与原始数据表相结合，

import pandas as pd

prob_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\output\test_results.tsv'
total_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\total_predict.csv'

total = pd.read_csv(total_path)
total.pop(total.columns[0])
prob = pd.read_csv(prob_path, sep='\t')

predicted_labels = prob.idxmax(axis=1)
# print(predicted_labels.head)

combined_df = pd.concat([total, predicted_labels], axis=1, ignore_index=False)
combined_df.columns = ['Upload Time', 'Read', 'Author', 'Title', 'Label']
combined_df.pop('Author')

# combined_df.to_csv(r'\raw.csv')

# 将字符串日期转换为datetime日期
combined_df['Upload Time'] = pd.to_datetime(combined_df['Upload Time']).dt.date

# # 使用简单投资者情绪计算方法
# grouped_df = combined_df.groupby('Upload Time')['Label'].value_counts()
# grouped_df.to_csv(r'count.csv')

# 使用加权投资者情绪计算方法
grouped_df = combined_df.groupby(['Upload Time', 'Label'])['Read'].sum().reset_index()
count_df = combined_df.groupby(['Upload Time'])['Read'].sum().reset_index()

print(count_df.head)

label_map = {'negative': -1, 'neutral': 0, 'positive': 1}
grouped_df['label_score'] = grouped_df['Label'].map(label_map)
grouped_df['index'] = grouped_df['label_score'] * grouped_df['Read']
index_by_date = grouped_df.groupby('Upload Time')['index'].sum()

merged_df = pd.merge(index_by_date, count_df, on='Upload Time')

# print(merged_df.head)
# merged_df.to_csv(r'merged.csv', index=False)

merged_df['norm index'] = merged_df['index'] / merged_df['Read']

print(merged_df.head)
merged_df.to_csv(r'merged.csv', index=False)