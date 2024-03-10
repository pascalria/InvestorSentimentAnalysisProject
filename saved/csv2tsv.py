import csv
import os

csv_file = r'e:\resources\project\bert\bert-master\data_collection\saved\test.csv'
tsv_file = 'test.tsv'

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
csv_path = os.path.join(current_dir, csv_file)
print(csv_path)
tsv_path = os.path.join(current_dir, tsv_file)
print(tsv_path)

with open(r'e:\resources\project\bert\bert-master\data_collection\saved\test.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    with open(tsv_file, 'w', newline='', encoding='utf-8') as tsv:
        tsv_writer = csv.writer(tsv, delimiter='\t')
        
        for row in csv_reader:
            tsv_writer.writerow(row)

