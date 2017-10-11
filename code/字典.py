# Python3 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }


# 访问字典里的值
# 如果用字典里没有的键访问数据，会输出错误
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8         # 更新 Age
dict['School'] = "教程"  # 添加信息


print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。显示删除一个字典用del命令
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键 'Name'
print(dict)
dict.clear()     # 删除字典
del dict         # 删除字典


'''
字典键的特性
字典值可以没有限制地取任何对象，既可以是标准的对象，也可以是用户定义的，但键不行。
'''
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("dict['Name']: ", dict['Name'])
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# dict = {['Name']: 'Runoob', 'Age': 7}
# print ("dict['Name']: ", dict['Name'])


'''
字典内置函数&方法
len(dict)
计算字典元素个数，即键的总数。
str(dict)
输出字典，以可打印的字符串表示。
type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。
'''


'''
Python字典包含了以下内置
序号	函数及描述
1	radiansdict.clear()
删除字典内所有元素
2	radiansdict.copy()
返回一个字典的浅复制
3	radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
以列表返回一个字典所有的键
8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
10	radiansdict.values()
以列表返回字典中的所有值
11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
随机返回并删除字典中的一对键和值(一般删除末尾对)。
'''