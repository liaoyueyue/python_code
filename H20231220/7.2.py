# 2.	student.txt文件在代码编辑文件的同级目录下。由于业务需要，要将txt文件转换为csv文件，student.txt中的内容如下：
# 姓名 年龄 成绩
# 张三  16   85
# 李四  16   77
# 韩梅梅 17  93
# 李雷   17  59。

import csv

# 打开student.txt文件，读取内容
with open('student.txt', 'r', encoding='utf-8') as infile:
    content = infile.read()

# 将读取到的内容按行分割
lines = content.split('\n')

# 将每行内容按空格分割，得到姓名、年龄和成绩
data = [line.split() for line in lines]

# 创建一个新的csv文件，将分割后的数据写入csv文件
with open('student.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)


