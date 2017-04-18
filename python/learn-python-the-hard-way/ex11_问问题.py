# -*- coding: utf-8 -*-

print "How old are you?",

#raw_input接受用户输入指令，并将输入值赋给age这个变量
#age值被当成是一个字符串
#如果要参与运算的话，首先要转换数据类型，比如int(age)
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#查看age的数据类型
print type(age)

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#逗号不换行
print "hello",
print "world"

#raw_input可以直接读取控制台的输入，所以一般比较常用
#input只能读取合法的python表达式，字符串一定要加引号
#input可以根据实际数据类型确定输出数据类型
r_input = raw_input("给出你的选择:")

print r_input
print type(r_input)
