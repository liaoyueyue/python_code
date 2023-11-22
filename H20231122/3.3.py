# 3.	用循环的方式通过输入创建一个字典favorite_dict，用于保留自己喜欢的食物，并打印出，参考指定输出格式。
favorite_dict = {}
while True:
    food = input("请输入你喜欢的食物，输入0退出")
    if food == "0":
        break
    else:
        rating = input("请输入你的该食物的评分1-10：")
        try:
            rating = int(rating)
            if 1 <= rating <= 10:
                favorite_dict[food] = rating
            else:
                print("评分必须在1-10")
        except ValueError:
            print("评分必须是整数")
print("\n您喜欢的食物及评分：")
for food, rating in favorite_dict.items():
    print(f"{food}: {rating}")
