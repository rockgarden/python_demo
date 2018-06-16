title = "列表"

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
a.index(333)
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles[0] = 'ducati'  # 修改元素
print(motorcycles)
motorcycles.append('honda')  # 末尾添加元素
motorcycles.insert(0, 'yamaha')  # 插入元素
motorcycles.insert(1, 'suzuki')

# del 语句
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。
# 可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]  # delete 0 元素
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a  # del 删除实体变量

# List 删除任一元素，若有重复只删除第一个
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# List 当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
# 用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
stack = [3, 4, 5, 6, 7]
last_one = stack.pop()
stack.pop(0)  # 弹出0元素
print(stack)

# List 永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print("Here is the original list:")
print(cars)
cars.sort(reverse=True)
print(cars)

# List 临时排序
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse alphabetical list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)

# List 长度
print(len(cars))

# List 遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    # 缩进表示在循环体内
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone, that was a great magic show!")

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数。
for i in reversed(range(1, 10, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# range() 构造数字集
for v in range(1, 5):
    print(v)
numbers = list(range(1, 6))  # list(range())列表
print(numbers)
even_numbers = list(range(2, 11, 2))  # 指定步长
print(even_numbers)
squares = []
for value in range(1, 11):
    square = value ** 2  # **运算
    squares.append(square)
print(squares)
squares = [v ** 2 for v in range(1, 12)]
print(squares)

# 统计计算
print(min(squares), max(squares), sum(squares))

# List 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])  # 2到4
print(players[2:])  # 3到最后
print(players[-3:])  # 最后3个
print("Here are the first three players on my team:")
for player in players[:3]:  # 未指定第一个索引相当于0开始
    print(player.title())

# List 复制
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 这是复制, friend_foods = my_foods 是引用赋值
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 将列表当作队列使用
# 也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue)
queue.popleft()  # The first to arrive now leaves
print(queue)
queue.popleft()  # The second to arrive now leaves
print(queue)

# 列表推导式
# 列表推导式提供了从序列创建列表的简单途径。
# 通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
# 返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
vec = [2, 4, 6]
print([3 * x for x in vec])

print([[x, x ** 2] for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([3 * x for x in vec if x > 3])
print([3 * x for x in vec if x < 2])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])
print([x + y for x in vec1 for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])

# 列表推导式可以使用复杂表达式或嵌套函数：
print([str(round(355 / 113, i)) for i in range(1, 6)])

# Bug:列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边#第一条语句是最后一层。
# print([x*y for x in range[1,5] if x > 2 for y in range[1,4] if x < 3])
# for x in range[1,5]:
#     if x > 2:
#         for y in range[1,4]:
#             if x < 3:
#                 print(x*y)
