# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

i = 256 * 256
print('i 的值为：', i)

# end 关键字
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b

a = 10;
b = 388;
c = 98
print(a, b, c, sep='@')


# 递归方式求斐波纳契数列
def fab(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


list = fab(30)
print(list)

# 条件控制
'''

'''
var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

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

### 退出提示
input("点击 enter 键退出")

print("=======欢迎进入狗狗年龄对比系统========")
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
###退出提示
input("点击 enter 键退出")

# 该实例演示了数字猜谜游戏
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

'''
if 嵌套
在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''
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

print('数字猜谜游戏！')

a = 1
i = 0
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

import random

x = random.choice(range(100))
y = random.choice(range(200))
print(x, y)
if x > y:
    print('x:', x)
elif x == y:
    print('x+y', x + y)
else:
    print('y:', y)

# Python3 循环语句
'''
# 循环语句有 for 和 while。
while 循环
while语句的一般形式：
while 判断条件：
    语句
同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
while 循环语句和 for 循环语句使用 else 的区别：
1.如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
2.如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行。
'''
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

# 无限循环
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#     if num == 100:
#         var = 0

# print("Good bye!")
# 你可以使用 CTRL+C 来退出当前的无限循环。
# 无限循环在服务器上客户端的实时请求非常有用。


# while 循环使用 else 语句
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

# flag = 1
# while (flag): print('欢迎访问菜鸟教程!')
# print("Good bye!")


# for 语句
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)
# for 实例中使用了 break 语句，break 语句用于跳出当前循环体
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# range()函数
for i in range(5):
    print(i)
# range指定区间
for i in range(5, 9):
    print(i)
# range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
for i in range(0, 10, 3):
    print(i)
for i in range(-10, -100, -30):
    print(i)
# 结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# break和continue语句及循环中的else子句

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
# 查询质数
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# pass 语句
# pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)

n = 0
sum = 0
for n in range(0, 101):  # n 范围 0-100
    sum += n
print(sum)

# 循环嵌套来实现99乘法法则
# 外边一层循环控制行数
# i是行数
i = 1
while i <= 9:
    # 里面一层循环控制每一行中的列数
    j = 1
    while j <= i:
        mut = j * i
        print("%d*%d=%d" % (j, i, mut), end="  ")
        j += 1
    print("")
    i += 1

# for 循环的嵌套
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end='')
    print('\r')
