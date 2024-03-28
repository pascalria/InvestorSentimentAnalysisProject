import csv
import pandas as pd
# from random import shuffle

data = pd.read_csv(r'E:\resources\project\bert\bert-master\data_collection\saved\comment.csv').iloc[12018:495007]

data.to_csv(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\total_predict.csv')
data = data[['Title']]
data.to_csv(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\predict.tsv', sep='\t', header=False, index=False)
# for i in range(len(data_rows)):
#     data.append(data_rows[i][3])

# print(data_rows[0])