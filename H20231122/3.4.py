# 4.	自选一篇文章，对文章进行词频统计，提取该文的关键词。
import jieba
from collections import Counter

user_input = input("请输入一篇文章：")
words = jieba.lcut(user_input)
word_count = Counter(words)
print("词频统计结果：")
print(word_count)