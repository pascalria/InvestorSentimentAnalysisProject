# 从2015年12月25日（周五）至2019年12月31日（周二）之间的评论中
# 随机抽取7000条评论，选择其中的5000条作为训练集，
# 由“专业金融人士”为所有被抽取的评论标记情感。

import importlib
import csv
# from random import shuffle

with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\comment.csv', 'r', encoding='utf-8') as f: 
    readerd = csv.reader(f)
    next(readerd)
    data_rows = list(readerd)

data_rows = data_rows[495007:]
print(data_rows[0])

# 设置训练集比例
train_ratio = 0.8

random = importlib.import_module('random')
# 打乱原始数据列表
random.shuffle(data_rows)
print(data_rows[0])

# 计算抽取大小
size = int(7000)

randitem = random.sample(data_rows, k=size)
print(len(randitem))


with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\samples.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        for row in randitem:
            writer.writerow(row)
