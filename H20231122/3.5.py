# 5.	学校元旦联欢会，设定了抽奖环节，只要表演节目或是参加游戏的同学就可以得到一次抽奖机会，百分百中奖。请你设计这个随机抽奖程序。
import random

# 假设有一个参与活动的学生列表
students = ['小明', '小红', '小刚', '小美', '小亮', '小花', '小强', '小婷']

# 假设这里有表演节目或参加游戏的同学
participants = ['小明', '小红', '小亮', '小花']

# 按照要求，只要参加活动就有抽奖机会
eligible_students = list(set(students) & set(participants))

# 如果有参与活动的学生
if eligible_students:
    # 随机抽取一个获奖者
    winner = random.choice(eligible_students)
    print(f"恭喜 {winner} 获得了抽奖奖品！")
else:
    print("很抱歉，本次没有学生参与活动，无法进行抽奖。")
