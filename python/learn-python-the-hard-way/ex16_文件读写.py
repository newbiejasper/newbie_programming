# -*- coding:utf-8 -*-

#close 关闭文件
#read 读取文件内容，可以把它赋值给一个变量
#readline 读取文件的某一行
#truncate 清空这个文件
#write("stuff") 把字符串"stuff"写入文件

#examples
import os
#os.system("")引号里可以添加任何的终端命令
files = os.listdir(".")#列出当前目录下的所有文件及文件夹
for i in range(len(files)):
    print files[i].decode("utf-8")#目录下有中文，所以采用utf-8解码

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')#w文件有写得权限,r读的
#权限，a添加的权限，w+r可读可写

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)#把你输入的line1写入文件
target.write("\n")#换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
