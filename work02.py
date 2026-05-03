# 成绩判断小程序
# 需求：写一个程序，让用户输入成绩，判断是否通过考试（60分及以上为通过），并按格式打印出来。
score_1 = input("请输入成绩：")
score_1 = int(score_1)
pass_score = 60
if score_1 >= pass_score:
    print("恭喜你，考试通过了！")
else:
    print("很遗憾，你考试没有通过！")
# 成绩等级判断小程序
# 需求：写一个程序，让用户输入成绩，判断成绩等级（90分及以上为A，80分及以上为B，70分及以上为C，60分及以上为D，60分以下为E），并按格式打印出来。
score_2 = input("请输入成绩：")
score_2 = int(score_2)
if score_2 >= 90:
    print("A")
elif score_2 >= 80 and score_2 < 90:
    print("B")
elif score_2 >= 70 and score_2 < 80:
    print("C")
elif score_2 >= 60 and score_2 < 70:
    print("D")
else:
    print("E")
# 闰年判断小程序
# 需求：写一个程序，让用户输入一个年份，判断该年份是否为
leap_year = input("请输入年份:")
leap_year = int(leap_year)
if (leap_year % 400 == 0) or (leap_year % 4 == 0 and leap_year % 100 != 0):
    print(f"{leap_year}是闰年")
else:
    print(f"{leap_year}不是闰年")

# 写一个程序，让用户输入一个正整数 n，完成两个功能：
# 1. 统计 1 到 n 里，能被 3 整除的数字有多少个，打印结果
# 2. 计算 1 到 n 的整数和，打印结果
n = int(input("请输入正整数"))
total = 0
for n in range(1, n+1):
    total = total+n
print(f"1到n的整数和为{total}")
x = 0
for n in range(1, n+1):
    if n % 3 == 0:
        x += 1
print(f"1到n能被3整除的数字有{x}个")
# 需求：带次数限制的猜数字游戏，完整规则如下：
# 设定一个 1-100 之间的整数作为答案；
# 用户最多有 5 次猜数字的机会；
# 每次用户输入后，提示「猜大了」/「猜小了」/「猜对了」；
# 如果用户 5 次都没猜对，游戏结束，提示「机会用完了，游戏失败，正确答案是 XX」；
# 如果用户猜对了，直接结束游戏，提示「恭喜你，用了 X 次就猜对了！」。
# for循环版本
answer1 = 30
guess_chance1 = 1
for guess_chance1 in range(1, 6):
    guess_number1 = int(input(f"这是第{guess_chance1}次猜，请输入1到100之间的一个整数"))
    if guess_number1 > answer1:
        print("猜大了")
    elif guess_number1 < answer1:
        print("猜小了")
    else:
        print(f"恭喜你，只用了{guess_chance1}次就猜对了！")
        break
else:
    print(f"机会用完了，游戏失败，正确答案是{answer1}")
# while循环版本
# 分割线
answer2 = 30
guess_chance2 = 1
while True:
    guess_number2 = int(input(f"这是第{guess_chance2}次输入，请输入一个1到100以内的数字"))
    if guess_number2 < answer2:
        print("猜小了")
        guess_chance2 += 1
    elif guess_number2 > answer2:
        print("猜大了")
        guess_chance2 += 1
    else:
        print(f"恭喜你，只用了{guess_chance2}次就猜对了！")
        break
    if guess_chance2 > 5:
        print(f"机会用完了，游戏失败，正确答案是{answer2}")
        break
# 写一个程序，让用户输入一个正整数 n，找出 1 到 n 之间的所有质数，打印出来
# 质数判断规则：一个大于 1 的整数，除了 1 和它本身，不能被其他任何正整数整除，这个数就是质数。
# 提示：用嵌套循环（外层循环遍历 1 到 n 的每个数，内层循环判断这个数是不是质数），结合 break 优化判断逻辑。
n = int(input("请输入一个正整数"))
for num in range(1, n+1):
	if num <= 1:
		pass
	elif num==2:
		print(f"{num}是素数")
	else :
		is_prime =True
		for i in range (2,num):
			if num % i == 0:
				is_prime = False
				break
	if is_prime:
		print(f"{num}是素数")