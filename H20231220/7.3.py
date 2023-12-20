# 3.	将下面的列表favorite_languaged存入CSV文件和JSON文件。
# favorite_language = [
#     {"name":"小千","language":"汉语"},
#     {"name":"小锋","language":"汉语"},
#     {"name":"小狮","language":"汉语"},
#     {"name":"小明","language":"英语"},
# ]

import csv
import json

favorite_language = [
    {"name":"小千","language":"汉语"},
    {"name":"小锋","language":"汉语"},
    {"name":"小狮","language":"汉语"},
    {"name":"小明","language":"英语"},
]

# 将列表转换为csv格式并写入到csv文件中
with open('favorite_language.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "language"])
    writer.writeheader()
    for row in favorite_language:
        writer.writerow(row)

# 将列表转换为json格式并写入到json文件中
with open('favorite_language.json', 'w', encoding='utf-8') as f:
    json.dump(favorite_language, f, ensure_ascii=False, indent=4)


