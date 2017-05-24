#coding=utf-8
# 字符操作的一些方法
# 方法 描述
# string.capitalize() 把字符串的第一个字符大写
# string.center(width) 返回一个原字符串居中,并使用空格填充至长度 width 的新字符
# 串
# string.count(str, beg=0,
# end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则
# 返回指定范围内 str 出现的次数
# string.decode(encoding='UTF-8',
# errors='strict') 以 encoding 指定的编码格式解码 string，如果出错默认报一个
# ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者
# 'replace'
# string.encode(encoding='UTF-8',
# errors='strict')a 以 encoding 指定的编码格式编码 string，如果出错默认报一个
# ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# string.endswith(obj, beg=0,
# end=len(string))b,e检查字符串是否以 obj 结束，如果 beg 或者 end 指定则检查指
# 定的范围内是否以 obj 结束， 如果是， 返回 True,否则返回 False.
# string.expandtabs(tabsize=8)把字符串 string 中的 tab 符号转为空格， 默认的空
# 格数 tabsize 是 8.
# string.find(str, beg=0,
# end=len(string)) 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，
# 则检查是否包含在指定范围内，如果是返回开始的索引值，否则
# 返回-1
# string.index(str, beg=0,
# end=len(string)) 跟 find()方法一样，只不过如果 str 不在 string 中会报一个异常.
# string.isalnum()a, b, c R 如果 string 至少有一个字符并且所有字符都是字母或数字则返
# 回 True,否则返回 False
# string.isalpha()a, b, c 如果 string 至少有一个字符并且所有字符都是字母则返回 True,
# 否则返回 False
# string.isdecimal()b, c, d 如果 string 只包含十进制数字则返回 True 否则返回 False.
# string.isdigit()b, c 如果 string 只包含数字则返回 True 否则返回 False.
# string.islower()b, c 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分
# 大小写的)字符都是小写，则返回 True，否则返回 False
