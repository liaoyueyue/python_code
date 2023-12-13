# 4.	在流感高发期，学校组织对学生一个月的体温监控，学生需要每天记录自己的体温，最终形成“**同学体温记录表.txt”文档，以班级为单位上报到学校，如图。学校现在需要对个别同学体温数据进行抽查，检测其是否有连续3天发热的情况（36.7以上视为发热），以李明同学为例，请编写程序，实现对李明同学的体温数据分析，输出分析结果，即是否有连续三天发热，如果有，输出连续发热的最长天数。

def analyze_temperature(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"读取文件每一行：{lines}")
    max_continuous_days = 0
    continuous_days = 0
    student_name = lines.pop(0)
    print(f"名字：{student_name}各天体温如下")
    for line in lines:
        print(line.split()[0])
        if float(line.split()[0]) >= 36.7:
            continuous_days += 1
            max_continuous_days = max(max_continuous_days, continuous_days)
        else:
            continuous_days = 0

    return max_continuous_days

file_name = "李明同学体温记录表.txt"
result = analyze_temperature(file_name)
if result > 0:
    print("李明同学有连续{}天发热。".format(result))
else:
    print("李明同学没有连续发热的情况。")
