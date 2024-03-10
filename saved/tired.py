import csv

def conv(i):
    i = int(i)
    if i == 1:
        return 'negative'
    elif i == 2:
        return 'neutral'
    else :
        return 'positive'


# # 读取CSV文件
# def read_csv_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         rows = list(reader)  # 将所有行存储在列表中
#         reversed_rows = reversed(rows)  # 反转行的顺序
#         for row in reversed_rows:
#             yield row

# 保存标签
def save_labels(file_path, labels):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Label'])
        for label in labels:
            writer.writerow([label])

def yanzheng(data, label):
    for i in range(len(label)):
        print((data[i], label[i]))
    print(data[len(label)])

# # 主程序
# def main():
#     # 输入CSV文件路径
#     csv_file = r'E:\resources\project\bert\bert-master\data_collection\saved\comment.csv'
#     lis = read_csv_file(csv_file)
#     # 读取CSV文件并逐行显示，并等待手动输入标签
#     labels = []
#     st = 
#     for i in range(st, len(lis)):
#         print("当前行数据：", row)
#         label = int(input("请输入标签（整数）: "))
#         if label == 5:
#             break
#         labels.append(label)
#         save_labels(r'E:\resources\project\bert\bert-master\data_collection\saved\labels.csv', labels)
#         print("标签已保存到labels.csv文件中。")

#     # 保存标签到CSV文件


# if __name__ == '__main__':
#     main()

# 读取CSV数据文件并按倒序排列行
with open(r'E:\resources\project\bert\bert-master\data_collection\saved\comment.csv', 'r', encoding='utf-8') as f:
    readerd = csv.reader(f)
    data_rows = list(readerd)
    data_rows.reverse()

# 读取标签文件
with open(r'E:\resources\project\bert\bert-master\data_collection\saved\new_labels.csv', 'r', encoding='utf-8') as f:
    readerl = csv.reader(f)
    next(readerl)
    label_rows = list(readerl)

yanzheng(data_rows, label_rows)

# 找到最后一个标签对应的索引
bp = len(label_rows)

# 从最后一个标签对应的索引开始输入新标签
for i in range(bp,len(data_rows)):

    print("当前行数据：", data_rows[i])
    new_label = input(f"Enter a label for row {i} (or 'q' to quit): ")
    if new_label.lower() == 'q':
        break
    elif not new_label:  # 处理空输入
        print("Input cannot be empty. Please try again.")
        continue
    try:
        print(conv(new_label))
        label_rows.append([conv(new_label)])
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

    save_labels(r'E:\resources\project\bert\bert-master\data_collection\saved\labels2.csv', label_rows)
    print("标签已保存到labels.csv文件中。")

# # 保存新标签至文件
# with open(r'E:\resources\project\bert\bert-master\data_collection\saved\new_labels.csv', 'a', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     for label in new_labels:
#         writer.writerow([label])

print("New labels saved to 'new_labels.csv'.")