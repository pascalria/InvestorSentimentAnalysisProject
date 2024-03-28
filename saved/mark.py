import csv

def conv(i):
    i = int(i)
    if i == 1:
        return 'negative'
    elif i == 2:
        return 'neutral'
    else :
        return 'positive'

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

with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\samples2.csv', 'r', encoding='utf-8') as f:
    readerd = csv.reader(f)
    data_rows = list(readerd)

with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\marks.csv', 'r', encoding='utf-8') as f:
    readerl = csv.reader(f)
    next(readerl)
    label_rows = list(readerl)

# with open(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\marks.csv', 'r', encoding='utf-8') as f:
#     readerl = csv.reader(f)
#     label_rows = list(readerl)
    
yanzheng(data_rows, label_rows)
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

    save_labels(r'E:\resources\project\bert\InvestorSentimentAnalysisProject\saved\marks2.csv', label_rows)
    print("标签已保存到labels.csv文件中。")