# 写代码计算 10 除以 3 的商、余数、2 的 10 次方，分别打印出来
a = 10
b = a//3
c = a % 3
d = 2
f = d**10
print(f"10除以3的商是{b},余数是{c},2的10次方是{f}")
# 定义一个变量存你的成绩，写代码判断它是不是大于 90、是不是等于 100、是不是小于 60，分别打印 3 个结果
score = 120
print(score > 90)
print(score == 100)
print(score < 60)
# 定义一个变量存你的年龄，写代码判断它是老年人、成年人还是未成年人，并打印结果
age = input("请输入年龄：")
age = int(age)
if age >= 60:
    print("您是老年人")
elif age >= 18 and age < 60:
    print("您是成年人")
else:
    print("您是未成年人")
# 使用 range() 函数创建一个包含 1 到 100 的整数的列表，使用 range() 函数创建一个包含 2 到 100 的偶数的列表，使用 range() 函数创建一个包含 10 到 1 的整数的列表，并打印出来
list1 = range(1, 101)
list2 = range(2, 101, 2)
list3 = range(10, 0, -1)
print(list(list1))
print(list(list2))
print(list(list3))
# 计算1到100的奇数总和，计算100以内的偶数和奇数的个数
total = 0
for i in range(1, 100, 2):
    total = total+i
print(f"1到100的奇数总和是：{total}")
# 计算100以内的偶数和奇数的个数
even_count = 0
odd_count = 0
for num in range(1, 101):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"100以内的偶数有{even_count}个，100以内的奇数有{odd_count}个")
# 使用 input() 函数获取用户输入的密码，要求用户输入两次密码，如果两次输入的密码不一致，则提示用户重新输入，直到两次输入的密码一致为止，最后打印“密码确认成功”
password_1 = input("请输入密码")
password_2 = input("请再次输入密码")
while password_1 != password_2:
    print("两次密码不一致，请重新输入密码")
    password_2 = input("请再次输入密码")
print("密码确认成功")

# 写一个循环，让用户一直输入数字，输入负数就直接终止循环，输入正数就打印出来。
while True:
    num = input("请输入一个数字：")
    num = int(num)
    if num < 0:
        print("输入了负数，循环终止")
        break
    else:
        print(f"你输入的数字是{num}")
# 写一个循环，让用户一直输入数字，输入负数就直接终止循环，输入正数就打印出来。
while True:
    num = input("请输入数字")
    num = int(num)
    if num >= 0:
        print(num)
    else:
        print("输入了负数，循环终止")
        break
# 写一个循环，让用户一直输入密码，输对123456就终止，输错就提示重新输入
while True:
    answer = 123456
    a = int(input("请输入密码"))
    if a == answer:
        break
    else:
        print("密码错误，请重新输入")
