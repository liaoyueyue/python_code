# 已知两个长度相等的列表ls1 = [1,2,3,4,5]，ls2 = [6,7,8,9,10]，编程实现将两个列表中对应位置元素相加得到一个新的列表ls_new，并打印输出新列表ls_new。要求通过键盘输入元素来得到列表ls1，列表ls2由ls1得到。

ls1 = input("请输入列表ls1的元素，用逗号隔开：").split(',')
ls2 = [int(i) + 5 for i, j in zip(ls1, ls1)]
ls_new = [int(i) + int(j) for i, j in zip(ls1, ls2)]
print(f"新的列表{ls_new}")
