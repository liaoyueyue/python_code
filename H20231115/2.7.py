# 7.	老师在课堂上经常有提问环节,采用随机点名回答问题的方式,既体现了抽取学生的公平和公正,也让每个同学都做好回答问题的准备,使学生都能积极参与到课堂活动中,同时也增加了课堂趣味性。请你使用Python软件编写随机点名程序,从班级同学中随机抽取一位同学,并显示该同学姓名。

import random

# 班级同学姓名列表
students = ["张三", "李四", "王五", "赵六"]

# 从列表中随机抽取一位同学
random_student = random.choice(students)

# 显示被抽取的同学姓名
print(f"被抽到回答问题的同学是：{random_student}")