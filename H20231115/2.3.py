# 3.	某集训队运动员的百米跨栏成绩（单位：秒）分别为：14.04, 13.15, 14.47 , 14.58, 14.04, 14.04, 13.15, 14.58, 13.15,请建立一个列表(data)存储这些数据。请编写程序解决如下问题：上述一共有几个数据？统计成绩为14.04秒的次数；找出所有成绩中的最好成绩,并删除首次出现的最好成绩,最后显示列表data。

data = [14.04, 13.15, 14.47, 14.58, 14.04, 14.04, 13.15, 14.58, 13.15]
total_data = len(data)
count_1404 = data.count(14.04)
max_data = max(data)
data.remove(max_data)

print("总共有", total_data, "个数据")
print("成绩为14.04秒的次数为", count_1404)
print("最好成绩为", max_data)
print("最终列表data:", data)