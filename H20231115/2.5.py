# 5.	游戏中诗词填空环节,给出诗词的上句,请你说出诗词的下一句；或者给出下句,请你说出上一句。请你编写程序,模拟出题的过程,随机显示一首诗词中的某一句,要求回答出相应的上句或下句。

import random

# 创建诗词库，上句作为键，下句作为值
poems = {
    "白日依山尽，黄河入海流": "欲穷千里目，更上一层楼",
    "床前明月光，疑是地上霜": "举头望明月，低头思故乡",
    "好雨知时节，当春乃发生": "随风潜入夜，润物细无声",
}
# 随机选择一句诗句
random_poem = random.choice(list(poems.keys()))
# 提示用户回答问题
print("请根据下句填写上句或根据上句填写下句：")
print(random_poem)
# 接收用户的回答
user_answer = input("请输入答案：")
# 检查用户答案是否正确
if user_answer == poems[random_poem]:
    print("回答正确！")
else:
    print("回答错误。正确答案是:", poems[random_poem])
