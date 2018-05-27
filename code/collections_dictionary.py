# 字典
# 另一个非常有用的 Python 内建数据类型是字典。
# 序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
# 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
# 一对大括号创建一个空的字典：{}。
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)

for item in enumerate(tel):
    print(item)

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
print(tel.items())

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对。
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x ** 2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))
