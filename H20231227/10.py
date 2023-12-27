# 设有一个文本文件data.txt，存放了若干以逗号分隔的整数，求所有整数的平均值，将结果写到文件result.txt中。

with open("data.txt", "r") as f:
    data = f.read()
nums = [int(x) for x in data.split(",")]
avg = sum(nums) / len(nums)
with open("result.txt", "w") as f:
    f.write(str(avg))

