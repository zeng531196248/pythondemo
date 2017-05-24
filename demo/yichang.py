#处理异常的方式
# try 语句有两种主要形式: try-except 和 try-finally . 这两个语句是互斥的, 也就是说你
# 只能使用其中的一种. 一个 try 语句可以对应一个或多个 except 子句, 但只能对应一个
# finally 子句, 或是一个 try-except-finally 复合语句
try:
    1/0
except :
    import  sys
    print(sys.exc_info()) #获取异常信息

#对异常进行捕获
# sys.exc_info()是线程安全的，其他的都不是线程安全的
# 我们从 sys.exc_info()得到的元组中是:
# z exc_type: 异常类
# z exc_value: 异常类的实例
# z exc_traceback: 追踪(traceback)对象
# try:
# try_suite
# except Exception1:
# suite_for_Exception1
# except (Exception2, Exception3, Exception4):
# suite_for_Exceptions_2_3_and_4
# except Exception5, Argument5:
# suite_for_Exception5_plus_argument
# except (Exception6, Exception7), Argument67:
# suite_for_Exceptions6_and_7_plus_argument
# except:
# suite_for_all_other_exceptions
# else:
# no_exceptions_detected_suiteEdit By Vheavens
# finally:
# always_execute_suite
#try-except-else-finally的方式，这种方式一锅端


#具体的异常不一一举出


