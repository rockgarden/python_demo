# TODO: http://www.runoob.com/python3/python3-os-file-methods.html 31

pathFile = "/Users/wangkan/Documents/python_demo/code/source/os.txt"

# OS 文件/目录方法
# os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：
# 序号	方法及描述
# 1
# os.access(path, mode)
#
# 检验权限模式
# 2
# os.chdir(path)
#
# 改变当前工作目录
# 3
# os.chflags(path, flags)
#
# 设置路径的标记为数字标记。
# 4
# os.chmod(path, mode)
#
# 更改权限
# 5
# os.chown(path, uid, gid)
#
# 更改文件所有者
# 6
# os.chroot(path)
#
# 改变当前进程的根目录
# 7
# os.close(fd)
#
# 关闭文件描述符 fd
# 8
# os.closerange(fd_low, fd_high)
#
# 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
# 9
# os.dup(fd)
#
# 复制文件描述符 fd
# 10
# os.dup2(fd, fd2)
#
# 将一个文件描述符 fd 复制到另一个 fd2
# 11
# os.fchdir(fd)
#
# 通过文件描述符改变当前工作目录
# 12
# os.fchmod(fd, mode)
#
# 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
# 13
# os.fchown(fd, uid, gid)
#
# 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
# 14
# os.fdatasync(fd)
#
# 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
# 15
# os.fdopen(fd[, mode[, bufsize]])
#
# 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
# 16
# os.fpathconf(fd, name)
#
# 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
# 17
# os.fstat(fd)
#
# 返回文件描述符fd的状态，像stat()。
# 18
# os.fstatvfs(fd)
#
# 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
# 19
# os.fsync(fd)
#
# 强制将文件描述符为fd的文件写入硬盘。
# 20
# os.ftruncate(fd, length)
#
# 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
# 21
# os.getcwd()
#
# 返回当前工作目录
# 22
# os.getcwdu()
#
# 返回一个当前工作目录的Unicode对象
# 23
# os.isatty(fd)
#
# 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
# 24
# os.lchflags(path, flags)
#
# 设置路径的标记为数字标记，类似 chflags()，但是没有软链接
# 25
# os.lchmod(path, mode)
#
# 修改连接文件权限
# 26
# os.lchown(path, uid, gid)
#
# 更改文件所有者，类似 chown，但是不追踪链接。
# 27
# os.link(src, dst)
#
# 创建硬链接，名为参数 dst，指向参数 src
# 28
# os.listdir(path)
#
# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
# 29
# os.lseek(fd, pos, how)
#
# 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算;
# - os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
# 30
# os.lstat(path)
#
# 像stat(),但是没有软链接
# 31
# os.major(device)
#
# 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
# 32
# os.makedev(major, minor)
#
# 以major和minor设备号组成一个原始设备号
# 33
# os.makedirs(path[, mode])
#
# 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
# 34
# os.minor(device)
#
# 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
# 35
# os.mkdir(path[, mode])
#
# 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
# 36
# os.mkfifo(path[, mode])
#
# 创建命名管道，mode 为数字，默认为 0666 (八进制)
# 37
# os.mknod(filename[, mode=0600, device])
# 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
# 38
# os.open(file, flags[, mode])
#
# 打开一个文件，并且设置需要的打开选项，mode参数是可选的
# 39
# os.openpty()
#
# 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
# 40
# os.pathconf(path, name)
#
# 返回相关文件的系统配置信息。
# 41
# os.pipe()
#
# 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
# 42
# os.popen(command[, mode[, bufsize]])
#
# 从一个 command 打开一个管道
# 43
# os.read(fd, n)
#
# 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
# 44
# os.readlink(path)
#
# 返回软链接所指向的文件
# 45
# os.remove(path)
#
# 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
# 46
# os.removedirs(path)
#
# 递归删除目录。
# 47
# os.rename(src, dst)
#
# 重命名文件或目录，从 src 到 dst
# 48
# os.renames(old, new)
#
# 递归地对目录进行更名，也可以对文件进行更名。
# 49
# os.rmdir(path)
#
# 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
# 50
# os.stat(path)
#
# 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
# 51
# os.stat_float_times([newvalue])
# 决定stat_result是否以float对象显示时间戳
# 52
# os.statvfs(path)
# 获取指定路径的文件系统统计信息
# 53
# os.symlink(src, dst)
# 创建一个软链接
# 54
# os.tcgetpgrp(fd)
# 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
# 55
# os.tcsetpgrp(fd, pg)
# 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
# 56
# os.tempnam([dir[, prefix]])
# 返回唯一的路径名用于创建临时文件。
# 57
# os.tmpfile()
# 返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
# 58
# os.tmpnam()
# 为创建一个临时文件返回一个唯一的路径
# 59
# os.ttyname(fd)
# 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
# 60
# os.unlink(path)
# 删除文件路径
# 61
# os.utime(path, times)
# 返回指定的path文件的访问和修改的时间。
# 62
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# 输出在文件夹中的文件名通过在树中游走，向上或者向下。
# 63
# os.write(fd, str)
# 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度



'''
os.access() 方法使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。
语法
access()方法语法格式如下：
os.access(path, mode);
参数
path -- 要用来检测是否有访问权限的路径。
mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
os.F_OK: 作为access()的mode参数，测试path是否存在。
os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
返回值
如果允许访问返回 True , 否则返回False。
'''

import os, sys

# 假定 /tmp/foo.txt 文件存在，并有读写权限

ret = os.access(pathFile, os.F_OK)
print ("F_OK - 返回值 %s"% ret)

ret = os.access(pathFile, os.R_OK)
print ("R_OK - 返回值 %s"% ret)

ret = os.access(pathFile, os.W_OK)
print ("W_OK - 返回值 %s"% ret)

ret = os.access(pathFile, os.X_OK)
print ("X_OK - 返回值 %s"% ret)



'''
os.chdir() 方法用于改变当前工作目录到指定的路径。
'''
path = "/Users/wangkan/Documents/python_demo/code/source"

# 查看当前工作目录
retval = os.getcwd()
print("当前工作目录为 %s" % retval)

# 修改当前工作目录
os.chdir(path)

# 查看修改后的工作目录
retval = os.getcwd()

print ("目录修改成功 %s" % retval)



# os.chmod() 方法用于更改文件或目录的权限。
# 语法
# chmod()方法语法格式如下：
# os.chmod(path, mode)
# 参数
# path -- 文件名路径或目录路径。
# flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加
# - 目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
# stat.S_IXOTH: 其他用户有执行权0o001
# stat.S_IWOTH: 其他用户有写权限0o002
# stat.S_IROTH: 其他用户有读权限0o004
# stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
# stat.S_IXGRP: 组用户有执行权限0o010
# stat.S_IWGRP: 组用户有写权限0o020
# stat.S_IRGRP: 组用户有读权限0o040
# stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
# stat.S_IXUSR: 拥有者具有执行权限0o100
# stat.S_IWUSR: 拥有者具有写权限0o200
# stat.S_IRUSR: 拥有者具有读权限0o400
# stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
# stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
# stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
# stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
# stat.S_IREAD: windows下设为只读
# stat.S_IWRITE: windows下取消只读
# 返回值
# 该方法没有返回值。
import os, sys, stat

os.chmod(pathFile, stat.S_IXGRP)

# 设置文件可以被其他用户写入
os.chmod(pathFile, stat.S_IWOTH)

print("修改成功!!")



# os.chown() 方法用于更改文件所有者，如果不修改可以设置为 -1, 你需要超级用户权限来执行权限修改操作。
# 只支持在 Unix 下使用。
# 语法
# chown()方法语法格式如下：
# os.chown(path, uid, gid);
# 参数
# path -- 设置权限的文件路径
# uid -- 所属用户 ID
# gid -- 所属用户组 ID
import os, sys

# 设置所有者 ID 为 100
os.chown(pathFile, 100, -1)
print("修改权限成功!!")



# os.chflags() 方法用于设置路径的标记为数字标记。多个标记可以使用 OR 来组合起来。
# 只支持在 Unix 下使用。
# 语法
# chflags()方法语法格式如下：
# os.chflags(path, flags)
# 参数
# path -- 文件名路径或目录路径。
# flags -- 可以是以下值：
# stat.UF_NODUMP: 非转储文件
# stat.UF_IMMUTABLE: 文件是只读的
# stat.UF_APPEND: 文件只能追加内容
# stat.UF_NOUNLINK: 文件不可删除
# stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
# stat.SF_ARCHIVED: 可存档文件(超级用户可设)
# stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
# stat.SF_APPEND: 文件只能追加内容(超级用户可设)
# stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
# stat.SF_SNAPSHOT: 快照文件(超级用户可设)

import stat

# 为文件设置标记，使得它不能被重命名和删除
flags = stat.SF_NOUNLINK
retval = os.chflags(pathFile, flags )
# PermissionError: [Errno 1] Operation not permitted: '/Users/wangkan/Documents/python_demo/code/source/fileFlag.txt'
print ("返回值: %s" % retval)


os.chmod(pathFile, stat.S_IRWXU)



# os.chroot() 方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。
# 语法
# chroot()方法语法格式如下：
# os.chroot(path);
# 参数
# path -- 要设置为根目录的目录。
# 返回值
# 该方法没有返回值。

# 设置根目录为 /tmp
os.chroot("/tmp")

print ("修改根目录成功!!")



# os.close() 方法用于关闭指定的文件描述符 fd。
# 语法
# close()方法语法格式如下：
# os.close(fd);
# 参数
# fd -- 文件描述符。
# 返回值
# 该方法没有返回值。
# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

#  写入字符串
os.write(fd, "This is test")

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")



# os.closerange() 方法用于关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。
# 语法
# closerange()方法语法格式如下：
# os.closerange(fd_low, fd_high);
# 参数
# fd_low -- 最小文件描述符
# fd_high -- 最大文件描述符
# 该方法类似于：
# for fd in xrange(fd_low, fd_high):
#     try:
#         os.close(fd)
#     except OSError:
#         pass
# 返回值
# 该方法没有返回值。

# 打开文件
fd = os.open("foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test")

# 关闭文件
os.closerange(fd, fd)

print ("关闭文件成功!!")



# os.dup() 方法用于复制文件描述符 fd。
# 语法
# dup()方法语法格式如下：
# os.dup(fd);
# 参数
# fd -- 文件描述符
# 返回值
# 返回复制的文件描述符。

# 打开文件
fd = os.open("foo.txt", os.O_RDWR|os.O_CREAT )

# 复制文件描述符
d_fd = os.dup(fd )

# 使用复制的文件描述符写入文件
os.write(d_fd, "This is test")

# 关闭文件
os.closerange(fd, d_fd)

print("关闭所有文件成功!!")



# os.dup2() 方法用于将一个文件描述符 fd 复制到另一个 fd2。
# Unix, Windows 上可用。
# 语法
# dup2()方法语法格式如下：
# os.dup2(fd, fd2);
# 参数
# fd -- 要被复制的文件描述符
# fd2 -- 复制的文件描述符
# 返回值
# 没有返回值。

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test")

# 文件描述符为 1000
fd2 = 1000
os.dup2(fd, fd2);

# 在新的文件描述符上插入数据
os.lseek(fd2, 0, 0)
str = os.read(fd2, 100)
print ("读取的字符串是 : ", str)

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")



# os.fchdir() 方法通过文件描述符改变当前工作目录。
# Unix, Windows 上可用。
# 语法
# fchdir()方法语法格式如下：
# os.fchdir(fd);
# 参数
# fd -- 文件描述符
# 返回值
# 该方法没有返回值。
import os, sys

# 首先到目录 "/var/www/html"
os.chdir("/var/www/html" )

# 输出当前目录
print ("当前工作目录为 : %s" % os.getcwd())

# 打开新目录 "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# 使用 os.fchdir() 方法修改到新目录
os.fchdir(fd)

# 输出当前目录
print ("当前工作目录为 : %s" % os.getcwd())

# 关闭打开的目录
os.close( fd )



# os.fchmod() 方法用于改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
# Unix上可用。
# 语法
# fchmod()方法语法格式如下：
# os.fchmod(fd, mode);
# 参数
# fd -- 文件描述符
# mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：
# stat.S_ISUID:设置 UID 位
# stat.S_ISGID: 设置组 ID 位
# stat.S_ENFMT: 系统文件锁定的执法行动
# stat.S_ISVTX: 在执行之后保存文字和图片
# stat.S_IREAD: 对于拥有者读的权限
# stat.S_IWRITE: 对于拥有者写的权限
# stat.S_IEXEC: 对于拥有者执行的权限
# stat.S_IRWXU:对于拥有者读、写、执行的权限
# stat.S_IRUSR: 对于拥有者读的权限
# stat.S_IWUSR: 对于拥有者写的权限
# stat.S_IXUSR: 对于拥有者执行的权限
# stat.S_IRWXG: 对于同组的人读写执行的权限
# stat.S_IRGRP: 对于同组读的权限
# stat.S_IWGRP:对于同组写的权限
# stat.S_IXGRP: 对于同组执行的权限
# stat.S_IRWXO: 对于其他组读写执行的权限
# stat.S_IROTH: 对于其他组读的权限
# stat.S_IWOTH: 对于其他组写的权限
# stat.S_IXOTH:对于其他组执行的权限
# 返回值
# 该方法没有返回值。
import os, sys, stat

# 打开文件 "/tmp/foo.txt"
fd = os.open( "/tmp", os.O_RDONLY )

# 设置文件可通过组执行

os.fchmod( fd, stat.S_IXGRP)

# 设置文件可被其他用户写入
os.fchmod(fd, stat.S_IWOTH)

print ("修改权限成功!!")

# 关闭文件
os.close( fd )



# os.fchown() 方法用于修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
# Unix上可用。
# 语法
# fchown()方法语法格式如下：
# os.fchown(fd, uid, gid)
# 参数
# fd -- 文件描述符
# uid -- 文件所有者的用户id
# gid -- 文件所有者的用户组id
import os, sys, stat

# 打开文件 "/tmp/foo.txt"
fd = os.open( "/tmp", os.O_RDONLY )

# 设置文件的用户 id 为 100
os.fchown( fd, 100, -1)

# 设置文件的用户组 id 为 100
os.fchown( fd, -1, 50)


print ("修改权限成功!!")

# 关闭文件
os.close( fd )



# os.fdatasync() 方法用于强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。如果你需要刷新缓冲区可以使用该方法。
# Unix上可用。
# 语法
# fdatasync()方法语法格式如下：
# os.fdatasync(fd);
# 参数
# fd -- 文件描述符
import os, sys

# 打开文件 "/tmp/foo.txt"
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test")

# 使用 fdatasync() 方法
os.fdatasync(fd)

# 读取文件
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print ("读取的字符是 : ", str)

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")



# os.fdopen() 方法用于通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。
# Unix, Windows上可用。
# 语法
# fdopen()方法语法格式如下：
# os.fdopen(fd, [, mode[, bufsize]]);
# 参数
# fd -- 打开的文件的描述符，在Unix下，描述符是一个小整数。
# mode -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写
# -的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
# bufsize -- 可选，指定返回的文件对象是否带缓冲：buffersize=0，表示没有带缓冲；bufsize=1，表示该文件对象是行缓冲的；bufsize=正数，
# - 表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，对于tty字元设备一
# - 般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。
# 返回值
# 通过文件描述符返回的文件对象。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 获取以上文件的对象
fo = os.fdopen(fd, "w+")

# 获取当前文章
print ("Current I/O pointer position :%d" % fo.tell())

# 写入字符串
fo.write( "Python is a great language.\nYeah its great!!\n");

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print ("Read String is : ", str)

# 获取当前位置
print ("Current I/O pointer position :%d" % fo.tell())

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")



# os.fpathconf() 方法用于返回一个打开的文件的系统配置信息。
# Unix上可用。
# 语法
# fpathconf()方法语法格式如下：
# os.fpathconf(fd, name)
# 参数
# fd -- 打开的文件的描述符。
# name -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
# bufsize -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，传递一个数字作为名字，也是可以接受的。
# 返回值
# 返回一个打开的文件的系统配置信息。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

print ("%s" % os.pathconf_names)

# 获取最大文件连接数
no = os.fpathconf(fd, 'PC_LINK_MAX')
print ("文件最大连接数为 :%d" % no)

# 获取文件名最大长度
no = os.fpathconf(fd, 'PC_NAME_MAX')
print ("文件名最大长度为 :%d" % no)

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")



# os.fstat() 方法用于返回文件描述符fd的状态，类似 stat()。
# Unix，Windows上可用。
# fstat 方法返回的结构:
# st_dev: 设备信息
# st_ino: 文件的i-node值
# st_mode: 文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)
# st_nlink: 硬连接数
# st_uid: 用户ID
# st_gid: 用户组 ID
# st_rdev: 设备 ID (如果指定文件)
# st_size: 文件大小，以byte为单位
# st_blksize: 系统 I/O 块大小
# st_blocks: 文件的是由多少个 512 byte 的块构成的
# st_atime: 文件最近的访问时间
# st_mtime: 文件最近的修改时间
# st_ctime: 文件状态信息的修改时间（不是文件内容的修改时间）
# 语法
# fstat()方法语法格式如下：
# os.fstat(fd)
# 参数
# fd -- 文件的描述符。
# 返回值
# 返回文件描述符fd的状态。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 获取元组
info = os.fstat(fd)

print ("文件信息 :", info)

# 获取文件 uid
print ("文件 UID :%d" % info.st_uid)

# 获取文件 gid
print ("文件 GID  :%d" % info.st_gid)

# 关闭文件
os.close( fd)



# os.fstatvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息，类似 statvfs()。
# Unix上可用。
# fstatvfs 方法返回的结构:
# f_bsize: 文件系统块大小
# f_frsize: 分栈大小
# f_blocks: 文件系统数据块总数
# f_bfree: 可用块数
# f_bavail:非超级用户可获取的块数
# f_files: 文件结点总数
# f_ffree: 可用文件结点数
# f_favail: 非超级用户的可用文件结点数
# f_fsid: 文件系统标识 ID
# f_flag: 挂载标记
# f_namemax: 最大文件长度
# 语法
# fstatvfs()方法语法格式如下：
# os.fstatvfs(fd)
# 参数
# fd -- 文件的描述符。
# 返回值
# 返回包含文件描述符fd的文件的文件系统的信息。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 获取元组
info = os.fstatvfs(fd)

print ("文件信息 :", info)

# 获取文件名最大长度
print ("文件名最大长度 :%d" % info.f_namemax)

# 获取可用块数
print ("可用块数 :%d" % info.f_bfree)

# 关闭文件
os.close(fd)



# os.fsync() 方法强制将文件描述符为fd的文件写入硬盘。在Unix, 将调用fsync()函数;在Windows, 调用 _commit()函数。
# 如果你准备操作一个Python文件对象f, 首先f.flush(),然后os.fsync(f.fileno()), 确保与f相关的所有内存都写入了硬盘.在unix，Windows中有效。
# Unix、Windows上可用。
# 语法
# fsync()方法语法格式如下：
# os.fsync(fd)
# 参数
# fd -- 文件的描述符。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test")

# 使用 fsync() 方法.
os.fsync(fd)

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print ("读取的字符串为 : ", str)

# 关闭文件
os.close( fd)

print ("关闭文件成功!!")



# os.ftruncate() 裁剪文件描述符fd对应的文件, 它最大不能超过文件大小。
# Unix上可用。
# 语法
# ftruncate()方法语法格式如下：
# os.ftruncate(fd, length)¶
# 参数
# fd -- 文件的描述符。
# length -- 要裁剪文件大小。
# 返回值
# 该方法没有返回值。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test - This is test")

# 使用 ftruncate() 方法
os.ftruncate(fd, 10)

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("读取的字符串是 : ", str)

# 关闭文件
os.close( fd)

print("关闭文件成功!!")



# os.getcwd() 方法用于返回当前工作目录。
# 语法
# getcwd()方法语法格式如下：
# os.getcwd()
# 参数
# 无
# 返回值
# 返回当前进程的工作目录。
import os, sys

# 切换到 "/var/www/html" 目录
os.chdir("/var/www/html" )

# 打印当前目录
print ("当前工作目录 : %s" % os.getcwd())

# 打开 "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# 使用 os.fchdir() 方法修改目录
os.fchdir(fd)

# 打印当前目录
print ("当前工作目录 : %s" % os.getcwd())

# 关闭文件
os.close( fd )



# os.getcwdu() 方法用于返回一个当前工作目录的Unicode对象。
# Unix, Windows 系统下可用。
# 语法
# getcwdu()方法语法格式如下：
# os.getcwdu()
# 参数
# 无
# 返回值
# 返回一个当前工作目录的Unicode对象。
import os, sys

# 切换到 "/var/www/html" 目录
os.chdir("/var/www/html" )

# 打印当前目录
print ("当前工作目录 : %s" % os.getcwdu())

# 打开 "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# 使用 os.fchdir() 方法修改目录
os.fchdir(fd)

# 打印当前目录
print ("当前工作目录 : %s" % os.getcwdu())

# 关闭文件
os.close( fd )



# os.isatty() 方法用于判断如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
# 语法
# isatty()方法语法格式如下：
# os.isatty()
# 参数
# 无
# 返回值
# 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
str = "This is runoob.com site"
os.write(fd,bytes(str, 'UTF-8'))

# 使用 isatty() 查看文件
ret = os.isatty(fd)

print ("返回值: ", ret)

# 关闭文件
os.close( fd )



# os.lchflags() 方法用于设置路径的标记为数字标记，类似 chflags()，但是没有软链接。
# 只支持在 Unix 下使用。
# 语法
# lchflags()方法语法格式如下：
# os.lchflags(path, flags)
# 参数
# path -- 设置标记的文件路径
# flags -- 可以由一个或多个标记组合，多个使用"|"隔开：
# UF_NODUMP: 非转储文件
# UF_IMMUTABLE: 文件是只读的
# UF_APPEND: 文件只能追加内容
# UF_NOUNLINK: 文件不可删除
# UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
# SF_ARCHIVED: 可存档文件(超级用户可设)
# SF_IMMUTABLE: 文件是只读的(超级用户可设)
# SF_APPEND: 文件只能追加内容(超级用户可设)
# SF_NOUNLINK: 文件不可删除(超级用户可设)
# SF_SNAPSHOT: 快照文件(超级用户可设)
# 返回值
# 该方法没有返回值。
import os, sys

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭文件
os.close( fd )

# 修改文件标记
ret = os.lchflags(path, os.UF_IMMUTABLE )

print ("修改文件标记成功!!")



# os.lchmod() 方法用于修改连接文件权限。
# 只支持在 Unix 下使用。
# 语法
# lchmod()方法语法格式如下：
# os.lchmod(path, mode)
# 参数
# path -- 设置标记的文件路径
# mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：
# stat.S_ISUID:设置 UID 位
# stat.S_ISGID: 设置组 ID 位
# stat.S_ENFMT: 系统文件锁定的执法行动
# stat.S_ISVTX: 在执行之后保存文字和图片
# stat.S_IREAD: 对于拥有者读的权限
# stat.S_IWRITE: 对于拥有者写的权限
# stat.S_IEXEC: 对于拥有者执行的权限
# stat.S_IRWXU:对于拥有者读、写、执行的权限
# stat.S_IRUSR: 对于拥有者读的权限
# stat.S_IWUSR: 对于拥有者写的权限
# stat.S_IXUSR: 对于拥有者执行的权限
# stat.S_IRWXG: 对于同组的人读写执行的权限
# stat.S_IRGRP: 对于同组读的权限
# stat.S_IWGRP:对于同组写的权限
# stat.S_IXGRP: 对于同组执行的权限
# stat.S_IRWXO: 对于其他组读写执行的权限
# stat.S_IROTH: 对于其他组读的权限
# stat.S_IWOTH: 对于其他组写的权限
# stat.S_IXOTH:对于其他组执行的权限
# 返回值
# 该方法没有返回值。
import os, sys

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭文件
os.close( fd )

# 修改文件权限
# 设置文件可以通过组执行
os.lchmod( path, stat.S_IXGRP)

# 设置文件可以被其他用户写入
os.lchmod("/tmp/foo.txt", stat.S_IWOTH)

print ("修改权限成功!!")



# os.lchown() 方法用于更改文件所有者，类似 chown，但是不追踪链接。
# 只支持在 Unix 下使用。
# 语法
# lchown()方法语法格式如下：
# os.lchown(path, uid, gid)
# 参数
# path -- 设置权限的文件路径
# uid -- 所属用户 ID
# gid -- 所属用户组 ID
# 返回值
# 该方法没有返回值。
import os, sys

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭打开的文件
os.close( fd )

# 修改文件权限
# 设置文件所属用户 ID
os.lchown( path, 500, -1)

# 设置文件所属用户组 ID
os.lchown( path, -1, 500)

print ("修改权限成功!!")



# os.link() 方法用于创建硬链接，名为参数 dst，指向参数 src。
# 该方法对于创建一个已存在文件的拷贝是非常有用的。
# 只支持在 Unix, Windows 下使用。
# 语法
# link()方法语法格式如下：
# os.link(src, dst)
# 参数
# src -- 用于创建硬连接的源地址
# dst -- 用于创建硬连接的目标地址
# 返回值
# 该方法没有返回值。
import os, sys

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭文件
os.close( fd )

# 创建以上文件的拷贝
dst = "/tmp/foo.txt"
os.link( path, dst)

print ("创建硬链接成功!!")



# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
# 只支持在 Unix, Windows 下使用。
# 语法
# listdir()方法语法格式如下：
# os.listdir(path)
# 参数
# path -- 需要列出的目录路径
# 返回值
# 返回指定路径下的文件和文件夹列表。
import os, sys

# 打开文件
path = "/var/www/html/"
dirs = os.listdir( path )

# 输出所有文件和文件夹
for file in dirs:
    print (file)



# os.lseek() 方法用于设置文件描述符 fd 当前位置为 pos, how 方式修改。
# 在Unix，Windows中有效。
# 语法
# lseek()方法语法格式如下：
# os.lseek(fd, pos, how)
# 参数
# fd -- 文件描述符。
# pos -- 这是相对于给定的参数 how 在文件中的位置。。
# how -- 文件内参考位置。SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始。
# 返回值
# 该方法没有返回值。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test")

# 所有 fsync() 方法
os.fsync(fd)

# 从开始位置读取字符串
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print ("Read String is : ", str)

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")



# os.lstat() 方法用于类似 stat() 返回文件的信息,但是没有符号链接。在某些平台上，这是fstat的别名，例如 Windows。
# 语法
# lstat()方法语法格式如下：
# os.lstat(path)
# 参数
# path -- 要返回信息的文件。
# 返回值
# 返回文件信息。
import os, sys

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭打开的文件
os.close( fd )

# 获取元组
info = os.lstat(path)

print ("文件信息 :", info)

# 获取文件 uid
print ("文件 UID  :%d" % info.st_uid)

# 获取文件 gid
print ("文件 GID :%d" % info.st_gid)



# os.major() 方法用于从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
# 语法
# major()方法语法格式如下：
# os.major(device)
# 参数
# device -- 原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
# 返回值
# 返回设备major号码。
import os, sys

path = "/var/www/html/foo.txt"

# 获取元组
info = os.lstat(path)

# 获取 major 和 minor 设备号
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print ("Major 设备号 :", major_dnum)
print ("Minor 设备号 :", minor_dnum)



# os.makedev() 方法用于以major和minor设备号组成一个原始设备号。
# 语法
# makedev()方法语法格式如下：
# os.makedev(major, minor)
# 参数
# major -- Major 设备号。
# minor -- inor 设备号。
# 返回值
# 返回设备号。
import os, sys

path = "/var/www/html/foo.txt"

# 获取元组
info = os.lstat(path)

# 获取 major 和 minor 设备号
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print ("Major 设备号 :", major_dnum)
print ("Minor 设备号 :", minor_dnum)

# 生成设备号
dev_num = os.makedev(major_dnum, minor_dnum)
print ("设备号 :", dev_num)



# os.makedirs() 方法用于递归创建目录。像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。
# 语法
# makedirs()方法语法格式如下：
# os.makedirs(path, mode=0o777)
# 参数
# path -- 需要递归创建的目录。
# mode -- 权限模式。
# 返回值
# 该方法没有返回值。
import os, sys

# 创建的目录
path = "/tmp/home/monthly/daily"

os.makedirs(path, 0o0755);

print ("路径被创建")



# os.minor() 方法用于从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
# 语法
# minor()方法语法格式如下：
# os.minor(device)
# 参数
# device -- 原始的设备(使用stat中的st_dev或者st_rdev field )
# 返回值
# 返回设备 minor 号。
import os, sys

path = "/var/www/html/foo.txt"

# 获取元组
info = os.lstat(path)

# 获取 major 和 minor 设备号
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print ("Major 设备号 :", major_dnum)
print ("Minor 设备号 :", minor_dnum)



# os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
# 语法
# mkdir()方法语法格式如下：
# os.mkdir(path[, mode])
# 参数
# path -- 要创建的目录
# mode -- 要为目录设置的权限数字模式
# 返回值
# 该方法没有返回值。
import os, sys

# 创建的目录
path = "/tmp/home/monthly/daily/hourly"

os.mkdir(path, 0o0755 )

print ("目录已创建")



# os.mkfifo() 方法用于创建指令路径的管道，并设置权限模式。默认的模式为 0666 (八进制)。
# 语法
# mkfifo()方法语法格式如下：
# os.mkfifo(path[, mode])
# 参数
# path -- 要创建的目录
# mode -- 要为目录设置的权限数字模式
# 返回值
# 该方法没有返回值。
import os, sys

# 创建的目录
path = "/tmp/hourly"

os.mkfifo(path, 0o0644)

print ("路径被创建")



# os.mknod() 方法用于创建一个指定文件名的文件系统节点（文件，设备特别文件或者命名pipe）。
# 语法
# mknod()方法语法格式如下：
# os.mknod(filename[, mode=0600[, device=0]])
# 参数
# filename -- 创建的文件系统节点
# mode -- mode指定创建或使用节点的权限, 组合 (或者bitwise) stat.S_IFREG, stat.S_IFCHR, stat.S_IFBLK, 和stat.S_IFIFO (这些常数
# 在stat模块). 对于 stat.S_IFCHR和stat.S_IFBLK, 设备定义了 最新创建的设备特殊文件 (可能使用 os.makedev()),其它都将忽略。
# device -- 可选，指定创建文件的设备
# 返回值
# 该方法没有返回值。
import os
import stat

filename = '/tmp/tmpfile'
mode = 0o0600|stat.S_IRUSR

# 文件系统节点指定不同模式
os.mknod(filename, mode)



# os.open() 方法用于打开一个文件，并且设置需要的打开选项，模式参数mode参数是可选的，默认为 0777。
# 语法
# open()方法语法格式如下：
# os.open(file, flags[, mode]);
# 参数
# file -- 要打开的文件
# flags -- 该参数可以是以下选项，多个使用 "|" 隔开：
# os.O_RDONLY: 以只读的方式打开
# os.O_WRONLY: 以只写的方式打开
# os.O_RDWR : 以读写的方式打开
# os.O_NONBLOCK: 打开时不阻塞
# os.O_APPEND: 以追加的方式打开
# os.O_CREAT: 创建并打开一个新文件
# os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
# os.O_EXCL: 如果指定的文件存在，返回错误
# os.O_SHLOCK: 自动获取共享锁
# os.O_EXLOCK: 自动获取独立锁
# os.O_DIRECT: 消除或减少缓存效果
# os.O_FSYNC : 同步写入
# os.O_NOFOLLOW: 不追踪软链接
# mode -- 类似 chmod()。
# 返回值
# 返回新打开文件的描述符。
import os, sys

# 打开文件
fd = os.open("foo.txt", os.O_RDWR|os.O_CREAT)

# 写入字符串
os.write(fd, "This is test")

# 关闭文件
os.close(fd)

print("关闭文件成功!!")



# os.openpty() 方法用于打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
# 语法
# openpty()方法语法格式如下：
# os.openpty()
# 参数
# 无
# 返回值
# 返回文件描述符对，主从。
import os

# 主 pty, 从 tty
m,s = os.openpty()

print (m)
print (s)

# 显示终端名
s = os.ttyname(s)
print (m)
print (s)



# 40
# os.pathconf() 方法用于返回一个打开的文件的系统配置信息。
# Unix 平台下可用。
# 语法
# fpathconf()方法语法格式如下：
# os.fpathconf(fd, name)
# 参数
# name -- 文件描述符
# name -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平
# 台也定义了一些额外的名字。这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，传递一个数字作为名字，也是可以接受的。
# 返回值
# 返回文件的系统信息。
import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

print ("%s" % os.pathconf_names)

# 获取文件最大连接数
no = os.fpathconf(fd, 'PC_LINK_MAX')
print ("Maximum number of links to the file. :%d" % no)

# 获取文件名最大长度
no = os.fpathconf(fd, 'PC_NAME_MAX')
print ("Maximum length of a filename :%d" % no)

# 关闭文件
os.close( fd)

print ("关闭文件成功!!")
