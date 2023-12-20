# 1.	创建一个英文文本文件english.txt，统计文件中出现的单词及其出现的次数，并存入CSV文件。

import re
import csv
from collections import defaultdict

# 读取文件内容
with open('english.txt', 'r') as f:
    text = f.read()

# 将文本内容分割成单词列表
words = re.findall(r'\b\w+\b', text.lower())

# 使用字典统计单词及其出现次数
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1

# 将统计结果写入CSV文件
with open('english_word_count.csv', 'w', newline='') as csvfile:
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in word_count.items():
        writer.writerow({'word': word, 'count': count})
