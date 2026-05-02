# 基础题（作业难度，必做）：单位换算小程序
# 需求：写一个程序，让用户输入以「米」为单位的长度，程序转换成「厘米」和「毫米」，按格式打印出来。示例输出：用户输入 1.8，程序打印「1.8 米 = 180 厘米 = 1800 毫米」
long = input("请输入长度 （单位：米）：")
long =int(long)
print(f"长度是{long}米，等于是{long*100}厘米，等于是{long*1000}毫米")
# 进阶题（作业难度，选做）：成绩计算小程序
# 需求：写一个程序，让用户输入数学、语文、英语三门课程
score_math = input("请输入数学成绩：")
score_math =float(score_math)
score_chinese= input("请输入语文成绩：")
score_chinese =float(score_chinese)
score_english = input("请输入英语成绩：")
score_english =float(score_english)
average_score=(score_english+score_chinese+score_math)/3
print(f"平均成绩是{average_score}")
total_score=score_english+score_math+score_chinese
print(f"总成绩是{total_score}")
# 个人信息录入小程序
# 需求：写一个程序，让用户输入姓名、年龄、专业、学号等信息，并按格式打印出来
name=input("请输入姓名:")
age=input("请输入年龄：")
age=int(age)
major=input("请输入专业：")
id=input("请输入学号：")
print("====================")
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"专业：{major}")
print(f"学号：{id}")
print("====================")