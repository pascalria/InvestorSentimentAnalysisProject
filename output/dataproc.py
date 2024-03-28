import pandas as pd

prob_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\output\test_results.tsv'
total_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\total_predict.csv'

total = pd.read_csv(total_path)
prob = pd.read_csv(prob_path, sep='\t')

predicted_labels = prob.idxmax(axis=1)
print(predicted_labels)

print(total.head)
print(prob.head)