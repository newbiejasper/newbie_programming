# -*-coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv#from_file应该是目录下已经存在的文件

print "Copying from %s to %s" % (from_file, to_file)

# 打开文件，并将读取内容赋值给变量indata
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)#返回变量的长度

print "Does the output file exist? %r" % exists(to_file)#判断文件是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)#文件写入

print "Alright, all done."

out_file.close()
in_file.close()
#操作完成后记得关闭文件
