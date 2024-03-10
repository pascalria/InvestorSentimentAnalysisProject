from prompt_toolkit import prompt
import requests
import json
import csv

from zmq import NULL

def read_csv_file(file_path):
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for row in reversed(rows):  # 使用reversed函数倒序遍历行
            yield row

# 保存标签
def save_labels(file_path, labels):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Label'])
        for label in labels:
            writer.writerow([label])


# 准备请求数据
def req(comment):

    prompt = '你需要判断给定的金融评论的情绪倾向。只需回复“正面”、“负面”、“中性”。 评论：' + comment

    data = {
        "prompt": prompt,
        "history": [],
        "max_length": 2048,
        "top_p": 0.7,
        "temperature": 0.95
    }

    # 发送POST请求
    url = "http://localhost:8000/"  # 根据实际情况替换为API的URL
    response = requests.post(url, json=data)

    # 处理响应
    if response.status_code == 200:
        answer = response.json()
        print("回复:", answer["response"])
        ans = answer["response"]

    else:
        print("请求失败:", response.status_code)
        ans = NULL

    return ans

def main():
    # 输入CSV文件路径
    csv_file = r'E:\resources\project\bert\bert-master\data_collection\saved\comment.csv'
    count = 0
    # 读取CSV文件并逐行显示，并等待手动输入标签
    labels = []
    for row in read_csv_file(csv_file):
        comment = row[3]
        print(str(count)+comment)
        label = req(comment)
        labels.append(label)
        count +=1
        if count%1000 == 0:
            save_labels(r'E:\resources\project\bert\bert-master\data_collection\saved\labels.csv', labels)
            print("标签已保存到labels.csv文件中。")

    # 保存标签到CSV文件
    save_labels(r'E:\resources\project\bert\bert-master\data_collection\saved\labels.csv', labels)
    print("标签已保存到labels.csv文件中。")

if __name__ == '__main__':
    main()
