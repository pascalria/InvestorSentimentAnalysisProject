# 用于将第一批标签和文本结合。

import csv

def save_tsv(file_path, labels):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Label'])
        for label in labels:
            writer.writerow([label])

# 读取CSV数据文件并按倒序排列行
with open(r'E:\resources\project\bert\bert-master\data_collection\saved\comment.csv', 'r', encoding='utf-8') as f:
    readerd = csv.reader(f)
    data_rows = list(readerd)
    data_rows.reverse()

# 读取标签文件
with open(r'E:\resources\project\bert\bert-master\data_collection\saved\labels2.csv', 'r', encoding='utf-8') as f:
    readerl = csv.reader(f)
    next(readerl)
    label_rows = list(readerl)

dataset = list()
for i in range(len(label_rows)):
    trow = list()
    row = label_rows[i][0]

    # 删除引号
    row = row.replace("'", "")

    # 删除括号
    row = row.replace("[", "").replace("]", "")
    trow.append(row)
    trow.append(data_rows[i][3])
    dataset.append(trow)

print(dataset)

