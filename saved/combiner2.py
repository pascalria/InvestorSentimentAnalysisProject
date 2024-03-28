# 7000条样本，随机划分
import csv

with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\marks.csv', 'r', encoding='utf-8') as f: 
    readerd = csv.reader(f)
    next(readerd)
    label_rows = list(readerd)

with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\samples2.csv', 'r', encoding='utf-8') as f: 
    reader = csv.reader(f)
    data_rows = list(reader)

combined = list()
print(type(label_rows[2][0]))

for i in range(len(label_rows)):
    row = [label_rows[i][0].strip("[]'"), data_rows[i][3]]
    combined.append(row)

with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\combineds.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in combined:
            writer.writerow(row)
