# 处理bert预测的概率tsv，将其与原始数据表相结合

import pandas as pd

prob_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\output\test_results.tsv'
total_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\total_predict.csv'

total = pd.read_csv(total_path)
total.pop(total.columns[0])
prob = pd.read_csv(prob_path, sep='\t')

predicted_labels = prob.idxmax(axis=1)
print(predicted_labels.head)

combined_df = pd.concat([total, predicted_labels], axis=1, ignore_index=False)
combined_df.columns = ['Upload Time', 'Read', 'Author', 'Title', 'Label']
print(combined_df.head)


# print(prob.head)