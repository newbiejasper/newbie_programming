# -*- coding: utf-8 -*-

#导入Python的功能模块
from sys import argv

#在终端运行时
#python ex13_参数_解包_变量.py first second third
#给python命令传入4个参数，argv把参数进行解包，赋值给四个变量名

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
