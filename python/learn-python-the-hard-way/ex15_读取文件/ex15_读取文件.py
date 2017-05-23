# -*- coding: utf-8 -*-

#我们在读取文件时，如果在代码中固定好一个文件名，那么载下次想要重新读取别的文件时，就要重新写，所以最好的方法是让用户输入读取哪一个文件

from sys import argv

script, filename = argv

#filename可以改为“ex15_example.txt”
#open返回的是一个文件对象，而不是文件内容
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
