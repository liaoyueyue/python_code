# 5.	使用sorted()函数将列表list01=[“study”,”Python”,”strong”,”smart”,”beautiful”]中的所有元素都转换成首字母大写的形式。

list01 = ["study", "Python", "strong", "smart", "beautiful"]
list02 = [word.capitalize() for word in list01]
print(f"list01:{list01}")
print(f"list01转换后：{list02}")
