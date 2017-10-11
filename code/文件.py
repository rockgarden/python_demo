"""
File(文件) 方法
file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：
序号	方法及描述
1
file.close()
关闭文件。关闭后文件不能再进行读写操作。
2
file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
3
file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
4
file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。
5
file.next()
返回文件下一行。
6
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
7
file.readline([size])
读取整行，包括 "\n" 字符。
8
file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
9
file.seek(offset[, whence])
设置文件当前位置
10
file.tell()
返回文件当前位置。
11
file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。
12
file.write(str)
将字符串写入文件，没有返回值。
13
file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
"""


# 打开文件
fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)

# 刷新缓冲区
fo.flush()

fid = fo.fileno()
print ("文件描述符为: ", fid)

ret = fo.isatty()
print ("返回值 : ", ret)

# 关闭文件
fo.close()

fr = open("/Users/wangkan/Documents/python_demo/code/source/testfile.txt", "r")
print ("文件名为: ", fr.name)
for index in range(1): # 不可越界
    line = next(fr)
    print ("第 %d 行 - %s" % (index, line))

line1 = fr.read(10)
print("读取的字符串: %s" % (line1))

fr.close()

# 打开文件
fo = open("/Users/wangkan/Documents/python_demo/code/source/testfile.txt", "r+")
print ("文件名为: ", fo.name)

line = fo.readline()
print ("读取第一行 %s" % (line))

line = fo.readline(5) # 中文也为一个字符
print ("读取的字符串为: %s" % (line))

for line in fo.readlines():                          #依次读取每行
    line = line.strip()                             #去掉每行头尾空白
    print ("读取的数据为: %s" % (line))

# 重新设置文件读取指针到开头
fo.seek(0, 0)
line = fo.readline()
print ("读取的数据为: %s" % (line))

# 获取当前文件位置
pos = fo.tell()
print ("当前位置: %d" % (pos))

# 循环读取文件
fo.truncate()
line = fo.readlines()
print ("读取行: %s" % (line))

str = fo.read()
print ("读取数据: %s" % (str))

# 关闭文件
fo.close()


# 打开文件
fo = open("/Users/wangkan/Documents/python_demo/code/source/testfile.txt", "r+")
print ("文件名: ", fo.name)

str = "\n6:www.test.com"
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write( str )

# 读取文件所有内容
fo.seek(0,0)
for index in range(5):
    line = next(fo)
    print ("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()

fo = open("/Users/wangkan/Documents/python_demo/code/source/testfile.txt", "w","r")
print ("文件名为: ", fo.name)

seq = ["www.test.com 1\n", "www.test.com 2\n", "www.test.com 3\n", "www.test.com 4\n", "www.test.com 5\n"]
fo.writelines( seq )

# 读取文件所有内容
fo.seek(0,0)
for index in range(5):
    line = next(fo)
    print ("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()

'''
重置文件 testfile.txt
1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com
'''
# 打开文件
fo = open("/Users/wangkan/Documents/python_demo/code/source/testfile.txt", "r+")
print ("文件名为: ", fo.name)

# 截取10个字节
fo.truncate(10)

str = fo.read()
print ("读取数据: %s" % (str))

# 关闭文件
fo.close()


import os
import os.path

#path = 'D:/UC/'
ls = []

def getAppointFile(path,ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path,tmp)
            if True==os.path.isdir(pathTmp):
                getAppointFile(pathTmp,ls)
            elif pathTmp[pathTmp.rfind('.')+1:].upper()=='PY': # 检索指定路径下后缀JPG的文件 PY -> JPG
                ls.append(pathTmp)
    except PermissionError:
        pass

def main():

    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path,ls)
    #print(len(ls))
    print(ls)
    print(len(ls))

main()

