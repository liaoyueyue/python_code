# 4.	查找出工作目录下的所有Python程序文件（以.py结尾的文件），然后将所有Python程序复制到新建文件夹my_python下,最后把my_python文件夹及其中文件进行删除。

import os
import shutil

# 查找工作目录下的所有Python程序文件（以.py结尾的文件）
python_files = [f for f in os.listdir() if f.endswith('.py')]

# 将所有Python程序复制到新建文件夹my_python下
if not os.path.exists('my_python'):
    os.mkdir('my_python')
for file in python_files:
    shutil.copy(file, 'my_python')

# 删除my_python文件夹及其中文件
shutil.rmtree('my_python')


