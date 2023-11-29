# 5.	设计一个学生类Student，每个学生都有三门课程的成绩，分别是语文、数学和物理。重载“+”运算符，用于两个学生对象每门成绩的求和，重载方法返回一个学生对象。用程序实现多个学生的成绩求和，并求每门课程成绩的平均分。

class Student:
    def __init__(self, chinese, math, physics):
        self.chinese = chinese
        self.math = math
        self.physics = physics

    def __add__(self, other):
        return Student(self.chinese + other.chinese, self.math + other.math, self.physics + other.physics)

    def __str__(self):
        return f"语文： {self.chinese}, 数学： {self.math}, 物理： {self.physics}"

    @classmethod
    def average_score(cls, students):
        total_chinese = sum([student.chinese for student in students])
        total_math = sum([student.math for student in students])
        total_physics = sum([student.physics for student in students])
        return cls(total_chinese / len(students), total_math / len(students), total_physics / len(students))

student1 = Student(60, 88, 90)
student2 = Student(65, 85, 65)
student3 = Student(65, 75, 95)
print("学生1" + student1.__str__())
print("学生2" + student2.__str__())
print("学生3" + student3.__str__())
average_student = Student.average_score([student1, student2, student3])
print("平均分：语文: {}，数学: {}，物理: {}".format(average_student.chinese, average_student.math, average_student.physics))
