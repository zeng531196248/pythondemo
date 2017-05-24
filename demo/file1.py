#内建函数 open() 返回一个文件对象
filename = input('Enter file name: ')
f = open(filename, 'r')
for eachLine in f:
    print(eachLine),f.close()
# file.close() 关闭文件
# file.fileno() 返回文件的描述符(file descriptor ,FD, 整数值)
# file.flush() 刷新文件的内部缓冲区
# file.isatty() 判断 file 是否是一个类 tty 设备
# file.nexta() 返回文件的下一行(类似于 file.readline() ), 或在没有其它
# 引发 StopIteration 异常
# file.read(size=-1) 从文件读取 size 个字节, 当未给定 size 或给定负值的时候,
# 取剩余的所有字节, 然后作为字符串返回
# file.readintob(buf, size) 从文件读取 size 个字节到 buf 缓冲器(已不支持)
# file.readline(size=-1) 从文件中读取并返回一行(包括行结束符), 或返回最大


