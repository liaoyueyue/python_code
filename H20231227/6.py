# 掷骰子的规则是，三颗骰子放在有盖的器皿内摇晃。当玩家猜大小，点数小于等于11为小，大于11为大。请编写程序，模拟100000次游戏的结果，输出结果为大和小的次数。

import random
def roll():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
small_wins = 0
large_wins = 0
for _ in range(100000):
    dice_sum = roll()
    if dice_sum <= 11:
        small_wins += 1
    else:
        large_wins += 1
print("小赢次数：", small_wins)
print("大赢次数：", large_wins)




