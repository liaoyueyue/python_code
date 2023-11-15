# 1.	给定一个由20个整数值构成的列表[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1] , 编程只对列表中下标（索引）为3的倍数元素进行升序排列，下标不是3的倍数的元素保持留存原位。

list = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# 提取索引为3的倍数的元素并进行排序
list_index_multiple_3 = list[::3]
sorted_multiples_of_3 = sorted(list_index_multiple_3)
# 将排序后的元素放回原列表对应位置
list[::3] = sorted_multiples_of_3
print(list)