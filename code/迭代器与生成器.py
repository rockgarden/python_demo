__author__ = 'rockgarden'

import sys # 引入 sys 模块
'''
迭代器
是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器
'''
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print(next(it))   # 输出迭代器的下一个元素
print(next(it))


list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print(it)
for x in it:
    print(x, end=" ")

l = [i for i in range(0,15)]
print(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
m = (i for i in range(0,15))
print(m)    # m 是 generator object 迭代器
for g in m:
    print(g,end=', ')

list = [1, 2, 3, 4]
it = iter(list) #创建迭代器对象

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


'''
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
'''
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


def fibonacci(n,w=0): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print (next(f), end=" ")
#     except :
#         sys.exit()

def fibonacci1(n,w=0): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        #yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
# f1 = fibonacci1(10,0) # f 函数只是简单执行，并没有返回迭代器。


# 什么情况下需要使用 yield？
# 一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化），并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），这个时候，我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到每个 list 元素而不是直接得到一个完整的 list 来节省内存，这个时候 yield 就很有用。
# http://www.runoob.com/w3cnote/python-yield-used-analysis.html
# 以斐波那契函数为例，我们一般希望从 n 返回一个 n 个数的 list：
def fab(max):
   n, a, b = 0, 0, 1
   L = []
   while n < max:
       L.append(b)
       a, b = b, a + b
       n = n + 1
   return L
# 上面那个 fab 函数从参数 max 返回一个有 max 个元素的 list，当这个 max 很大的时候，会非常的占用内存。

# 我们实际使用的是 list 的遍历，也就是 list 的迭代器。那么我们可以让这个函数 fab 每次只返回一个迭代器——一个计算结果，而不是一个完整的 list
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

for x in fab(1000):
    print(x)
# 或者 next 函数之类的，实际上的运行方式是每次的调用都在 yield 处中断并返回一个结果，然后再次调用的时候再恢复中断继续运行。