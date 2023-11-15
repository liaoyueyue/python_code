# 2.	用户分别从键盘输入5个整数和3个整数组成两个列表list1和list2,将列表list1合并到list2中,并在list2末尾再添加两个数字88和188,然后对list2降序排列,最后输出最终的列表list2。

list1 = []
list2 = []
for i in range(5):
    num = int(input("请输入整数："))
    list1.append(num)
for i in range(3):
    num = int(input("请输入整数："))
    list2.append(num)
list2.extend(list1)
list2.extend([88, 188])
list2.sort(reverse=True)
print("最终list2:", list2)
