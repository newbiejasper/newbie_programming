# -*- coding: utf-8 -*-

#函数是做什么的
#1. 函数是一个代码块，他采用和变量命名一样的方式
#2. 接受参数
#3. 执行特定的功能

#函数的编写
#def关键字

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
