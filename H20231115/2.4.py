# 4.	下面是武汉某一周各天的最高和最低气温（单位为摄氏度）。其中,第一行为最高气温,第二行为最低气温。
# 最高温	10	15	14	14	18	19	20
# 最低温	1	4	6	2	4	5	6
# 编程找出这一周中第几天最热（按最高气温计算），最高多少度？这一周中第几天最冷（按最低气温计算），最冷多少度？求出全周每天的平均气温。假设在气象意义上,入冬标准是连续5天日均气温小于或等于10℃,根据这一周的气象数据判断武汉是否已经入冬？

max_temperatures = [10, 15, 14, 14, 18, 19, 20]
min_temperatures = [1, 4, 6, 2, 4, 5, 6]
max_temperature_day = max_temperatures.index(max(max_temperatures)) + 1
min_temperature_day = min_temperatures.index(min(min_temperatures)) + 1
print(f"第 {max_temperature_day} 天最热，最高气温为 {max(max_temperatures)} 度")
print(f"第 {min_temperature_day} 天最冷，最低气温为 {min(min_temperatures)} 度")
# 每天的平均气温
avg_temperatures = [(high + low) / 2 for high, low in zip(max_temperatures, min_temperatures)]
for day, temp in enumerate(avg_temperatures, start=1):
    print(f"第 {day} 天的平均气温为 {temp} 度")
# 判断是否入冬
days_below_10 = 0
for temp in avg_temperatures:
    if temp <= 10:
        days_below_10 += 1
    else:
        days_below_10 = 0
    if days_below_10 == 5:
        print("武汉已经入冬")
        break
else:
    print("武汉还没入冬")
