# 2.	模拟简易点餐软件进行点餐，当选中某样菜品的时候，选择该菜品放入已选菜单中。当某些菜品库存为0时，提示：“该菜品已经售完，请选择其他菜品。”，最后完成点餐输出选择菜单。
foods = {"牛奶": 2, "蛋糕": 3, "土豆": 1}
select_foods = []
def order_dish(dish):
    if foods.get(dish, 0) > 0:
        select_foods.append(dish)
        foods[dish] -= 1
        print(f"点了：{dish}")
    else:
        print("该菜品已经售完，请选择其他菜品。")
while True:
    print("请选择菜品")
    print("1: 牛奶")
    print("2: 蛋糕")
    print("3: 土豆")
    print("0: 退出")
    dish = input("请输入")
    if dish == '0':
        break
    elif dish == '1':
        order_dish("牛奶")
    elif dish == '2':
        order_dish("蛋糕")
    elif dish == '3':
        order_dish("土豆")
    else:
        print("没有这个选项!\n")
print(f"选择的菜单{select_foods}")
