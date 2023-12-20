# 5.	根据指定文件名，创建文件的备份。

import shutil

def create_backup(file_name):
    backup_file_name = file_name + '.bak'
    shutil.copy(file_name, backup_file_name)
    print(f"备份文件已创建： {backup_file_name}")

file_name = "required_backup_file.txt"
create_backup(file_name)
