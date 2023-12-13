# 1.	之、乎、者、也为文言文中常用的四个语气助词，古人赋诗作文，多会用到这些助词，编写程序统计唐代文学家韩愈的文章《师说》中，“之、乎、者、也”四个词出现的次数？

# python初学者解法
# 需要的依赖库：os, re
import re

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    words = ['之', '乎', '者', '也']
    count = {word: len(re.findall(word, content)) for word in words}
    return count

print(count_words("师说.txt"))
