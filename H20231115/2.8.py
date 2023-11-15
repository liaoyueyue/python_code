# 8.	生肖又称属相,是中华民族悠久的民俗文化,每个中华儿女在出生时都确定自己的生肖。对于自己的生肖你可能记得很清楚,但是任意给定一个人的出生年份,你能很快算出他的生肖吗？

def calculate_zodiac(year):
    zodiacs = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    start_year = 1900  # 生肖循环开始的年份
    offset = (year - start_year) % 12  # 计算生肖的偏移量
    return zodiacs[offset]

# 输入一个人的出生年份
birth_year = int(input("请输入出生年份："))

# 计算对应的生肖
zodiac = calculate_zodiac(birth_year)
print(f"{birth_year}年出生的人的生肖是：{zodiac}")
