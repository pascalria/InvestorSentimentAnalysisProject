import pandas as pd

df = pd.read_csv(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\datasetfin\test.tsv', sep='\t', header=None)
# 添加新列并指定内容
value = 'neutral'
df.insert(0, 'label', value)

dev_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\datasetfin\dev.tsv'
df.to_csv(dev_path, sep='\t', header=False, index=False)