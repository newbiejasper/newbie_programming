# -*- coding: utf-8 -*-

# \(backslash)反斜杠将一些难打印的字符放到字符串，
# 针对不同的符号有很多转义序列
# 双反斜杠\\可以打印出反斜杠\

# 对单引号和双引号转义
print "i am 6'2\" tall."
print 'i am 6\'2" tall.'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# 三引号可以创建多行字符串
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 其他转义序列
# \a 响铃
# \b 退格
# \v 纵向制表符
# \f 换页
