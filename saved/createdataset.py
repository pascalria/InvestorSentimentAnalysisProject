import csv
import os
from random import shuffle

total = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\combined.csv'

train_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\train.tsv'
dev_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\dev.tsv'
test_path = r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\dataset3\test.tsv'


with open(total, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    data_rows = list(csv_reader)

train_num = 0.8*len(data_rows)
dev_num = 0.1*len(data_rows)
test_num = 0.1*len(data_rows)

shuffle(data_rows)
train = data_rows[0:int(train_num)]
dev = data_rows[int(train_num):int(train_num + dev_num)]
test = data_rows[int(train_num + dev_num):int(train_num + dev_num + test_num)]

with open(train_path, 'w', newline='', encoding='utf-8') as tsv:
        tsv_writer = csv.writer(tsv, delimiter='\t')
        for row in train:
            tsv_writer.writerow(row)

with open(dev_path, 'w', newline='', encoding='utf-8') as tsv:
        tsv_writer = csv.writer(tsv, delimiter='\t')
        for row in dev:
            tsv_writer.writerow(row)

with open(test_path, 'w', newline='', encoding='utf-8') as tsv:
        tsv_writer = csv.writer(tsv, delimiter='\t')
        for row in test:
            tsv_writer.writerow(row)
