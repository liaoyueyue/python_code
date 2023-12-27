# 已知产品列表如li = ["木瓜", "樱桃", "火龙果", "香蕉"]， 编程循环输出序号（从1开始）和水果名称（如1木瓜），如果用户输入选择的水果序号，则能输出水果名称，然后再次循环要求用户输入序号。如果用户输入的不是数字，则提示请输入数字。如果用户输入的水果序号有误，则提示请输入有效数字，并重新输入，如果用户输入Q或者q，则退出程序。

li = ["木瓜", "樱桃", "火龙果", "香蕉"]
while True:
    for i, fruit in enumerate(li, start=1):
        print(f"{i}:{fruit}")
    choice = input("请输入水果序号（输入Q或q退出）：")
    if choice.lower() == 'q':
        break
    if not choice.isdigit():
        print("请输入数字")
        continue
    choice = int(choice)
    if 1 <= choice <= len(li):
        print(f"你选择的是：{li[choice-1]}")
    else:
        print("请输入有效数字")
