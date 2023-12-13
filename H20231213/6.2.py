# 2.	圆周率PI前10000位数存放在文件“PI.txt”中，查询是否包含你出生日期的信息，即假设你的生日是4月12日，可以查询0412是否包含中PI值中。试编写程序完成查询。

def check_birthday_in_pi(file_path, birthday):
    with open(file_path, 'r') as f:
        pi_str = f.read()
    return birthday in pi_str

file_path = "Pi.txt"
birthday = "0412"
result = check_birthday_in_pi(file_path, birthday)
if result:
    print("生日信息在圆周率PI值中")
else:
    print("生日信息不在圆周率PI值中")
