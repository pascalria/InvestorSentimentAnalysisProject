# 用于分批次爬取东方财富股吧创业板指数据
# 由于连续爬取35页后就会触发反爬虫
# 所以在触发之前sleel十分钟再继续

import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import os
import pandas as pd

# # 东方财富创业板指
# url = "https://guba.eastmoney.com/list,zssz399006,f.html"

# # 浏览器标识
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'}

# r = requests.get(url, headers=headers)
# print(r.apparent_encoding)
# r.encoding = r.apparent_encoding
# text1 = r.text;print(text1)


def get_batch(offset):

    PAGES = 35
    real = offset*PAGES
    
    data_list = list()
    readl = list()
    authorl = list()
    titlel = list()
    timel = list()

    for i in range(real, PAGES+real):

        if i==0:
            url = "https://guba.eastmoney.com/list,zssz399006,f.html"
        else:
            url = "http://guba.eastmoney.com/list,zssz399006,f_"+str(i+1)+".html"
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'}       #模拟电脑端浏览器登陆，如果不写的话有些网页进不去
        request = requests.get(url, headers=headers)

        # print(request.apparent_encoding)

        request.encoding = request.apparent_encoding

        text = request.text

        soup = BeautifulSoup(text, 'html.parser')

        readl.extend([read.text for read in soup.find_all('div', class_='read')])
        authorl.extend([author.text for author in soup.find_all('div', class_='author')])
        titlel.extend([title.text for title in soup.find_all('div', class_='title')])
        timel.extend([title.text for title in soup.find_all('div', class_='update')])

        time.sleep(random.randint(1,5)) 

    data_list = [timel, readl, authorl, titlel]
    print('batch ' + str(offset+1) + 'done')

    return data_list

# 将一批次的数据保存到一个csv中
def tocsv(offset, data_list):

    filename = 'request' + str(offset) + '.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Upload Time', 'Read', 'Author', 'Title'])
        for row in zip(*data_list):
            writer.writerow(row)

for i in range(58,280):
    data = get_batch(i)
    tocsv(i, data)
    time.sleep(600)

# 读取所有分片数据
dataset = list()
for i in range(280):
    file_name = os.path.join(r'E:\resources\project\bert\bert-master\data_collection', 'request'+str(i)+'.csv')
    # print(file_name)
    with open(file_name, 'r', encoding='utf-8') as file:
        data = pd.read_csv(file_name)
        dataset.append(data)

print(len(dataset))

# 删除由于爬虫延时产生的重复行
year = 2024
count = 0

for i in range(len(dataset)):
     # print('current table length: ' + str(len(dataset[i])))
     # print(dataset[i].iloc[0].values)

     if i != 0:
          target = dataset[i].iloc[0]
          # print(target.values)

          for j in range(len(dataset[i-1])):

               current = dataset[i-1].iloc[j]
               # print(current.values)

               if target.equals(current) == True:

                    count += 1
                    print('the same rows in %d and %d are from %d to %d' % (i-1,i,j, len(dataset[i-1])-1))
                    dataset[6].drop(dataset[6].index[(j):(len(dataset[i-1]))], inplace=True)

print(count)


# 合并数据表
merged_data = pd.DataFrame()
for i in range(len(dataset)):
    merged_data = pd.concat([merged_data, dataset[i]], ignore_index=True)

print(len(merged_data))
merged_data.head()
merged_data.head()
merged_data.tail()
print(merged_data.iloc[0,0])

#为时间标签增加年份
year = 2024
count = 0

for i in range(len(merged_data)):
    if i != 0:
        last = merged_data.iloc[i-1,0]
        next = merged_data.iloc[i,0]
        # print((int(last[5:7]),int(next[0:2])))

        if int(last[5:7]) < int(next[0:2]):
            count += 1
            year -= 1
            print('current year: %d' % year)
            merged_data.iloc[i,0] = str(year) + '-' + merged_data.iloc[i,0]

        else:
            merged_data.iloc[i,0] = str(year) + '-' + merged_data.iloc[i,0]
            
    else:
        merged_data.iloc[i,0] = str(year) + '-' + merged_data.iloc[i,0]

print(count)

merged_data.head()
merged_data.tail()
print(merged_data.iloc[-1,0])

#保存为csv
merged_data.to_csv('comment.csv',index=False)

#csv转tsv
with open(r'comment.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    with open(r'comment.tsv', 'w', newline='', encoding='utf-8') as tsv:
        tsv_writer = csv.writer(tsv, delimiter='\t')
        
        for row in csv_reader:
            tsv_writer.writerow(row)