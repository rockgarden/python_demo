# if 嵌套
# 在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
# if 表达式1:
#     语句
#     if 表达式2:
#         语句
#     elif 表达式3:
#         语句
#     else:
#         语句
# elif 表达式4:
#     语句
# else:
#     语句
print('=======测试模运算=======')
num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")
input("点击 enter 键退出")

# 该实例演示了数字猜谜游戏
print('=======数字猜谜游戏=======')
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

a = 1
i = 0  # 次数
while a != 20:
    a = int(input('请输入你猜的数字：'))
    i += 1
    if a == 20:
        if i < 3:
            print('真厉害，这么快就猜对了！')
        else:
            print('总算猜对了，恭喜恭喜！')
    elif a < 20:
        print('你猜的数字小了，不要灰心，继续努力！')
    else:
        print('你猜的数字大了，不要灰心，继续加油！')
input("点击 enter 键退出")

print("=======狗狗年龄对比系统========")
# 条件控制 if
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)
input("点击 enter 键退出")

# 条件控制 while
while True:
    try:
        age = int(input("请输入您家狗的年龄:"))
        print(" ")
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2) * 5
            print("相当于人类：", human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")
input("点击 enter 键退出")
