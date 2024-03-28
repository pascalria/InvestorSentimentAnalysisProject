import pandas as pd
import numpy as np
import random


total = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\combined3.csv'
train_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\train.tsv'
dev_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\dev.tsv'
test_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\test.tsv'


total_df = pd.read_csv(total, header=None)
# 自定义列名
total_df.columns = ['label', 'comment']
# 获取唯一标签列表
unique_labels = total_df['label'].unique()
print(unique_labels)

# 定义划分比例
train_ratio = 0.99  # 训练集比例
test_ratio = 0.005  # 测试集比例
dev_ratio = 0.005  # 开发集比例

grouped = total_df.groupby('label')

train_sets = []
other_sets = []
test_sets = []
dev_sets = []

for label,group in grouped:
      train_set = group.sample(frac=train_ratio, random_state=random.randint(1,100))
      other_set = group.drop(train_set.index)
      train_sets.append(train_set)
      other_sets.append(other_set)

other_sets = pd.concat(other_sets)

grouped2 = other_sets.groupby('label')
for label,group in grouped2:
      test_set = group.sample(frac=0.5, random_state=0)
      dev_set = group.drop(test_set.index)
      test_sets.append(test_set)
      dev_sets.append(dev_set)

train_sets = pd.concat(train_sets).sample(frac=1, random_state=42)
test_sets = pd.concat(test_sets).sample(frac=1, random_state=42)
dev_sets = pd.concat(dev_sets).sample(frac=1, random_state=42)

print(train_sets)
print(dev_sets)
print(test_sets)

train_sets.to_csv(train_path, sep='\t', header=False, index=False)
test_sets.to_csv(test_path, sep='\t', header=False, index=False)
dev_sets.to_csv(dev_path, sep='\t', header=False, index=False)
