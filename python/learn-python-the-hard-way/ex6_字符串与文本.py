# -*- coding:utf-8 -*-

#什么叫字符串：字符串就是一块文本，你想要展示给别人，
#或者作为程序输出的结果

#格式化输出时，如果你想要输出多个，可以用%(one,two,three)的格式,%前面没有逗号

#例如
one = 'i'
two  = 'lee sin'
three = 'ashe'
print "%s like the heroes %s and %s best" %(one,two,three)

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#%r用来做debugging，因为它展示的是未经处理的数据
#%s是用来向用户展示数据的
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
