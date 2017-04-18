# -*- coding:utf-8 -*-

#用双引号和单引号括起来的部分就创建了一个字符串
name = 'Zed A. Shaw'
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs

#格式化字符串就是把变量嵌入到字符串里去
#字符串序列里用(1)%s:表示字符串这里将要放置字符串变量，或者元组
#字符串序列里用(2)%d:表示字符串这里将要放置整数值变量
#%e:Floating point exponential format(lowercase).
#%E:Floating point exponential format (uppercase).
#%f:Floating point decimal format.
#%c:单个字符串
#%r:用 repr()转换的 python字符串对象

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
