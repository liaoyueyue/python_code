# 2.	定义一个生成器函数，传入英文字符串，选出其中长度超过4的单词，顺序返回这些单词。

def long_words(text):
    words = text.split()
    for word in words:
        if len(word) > 4:
            yield word

text = "Will do! Take care and have a great day!"
for word in long_words(text):
    print(word)
