from random import randint

key = randint(0, 10)
count = 0

while True:
    num = int(input("你要猜的数字"))
    count += 1
    if num == key:
        print(f"恭喜，你猜对了！你一共猜了 {count} 次。")
        break
    elif num < key:
        print("太小了，请再试一次。")
    else:
        print("太大了，请再试一次。")





