# 3.	用Python编写一份九九乘法表，并将其写入txt文件中。

with open("99_table.txt", "w") as f:
    for i in range(1, 10):
        for j in range(1, i + 1):
            f.write(f"{j} * {i} = {j * i}\t")
        f.write("\n")


