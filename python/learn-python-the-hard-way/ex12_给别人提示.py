# -*- coding:utf-8 -*-

#在要求用户从控制台输入时
#需要给别人一些提示，告诉他写下什么东西
y = raw_input("写下你的年龄（不能超过100）：")

#提示的内容不会赋值给y变量

#重新编写上一节中的例子
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#pydoc+函数名称，可以调出这个函数的文档
#例如 pydoc raw_input
#按Q键退出
#pydoc open 打开文件，返回文件对象
#pydoc file 打开文件
#os,sys 都是模块
