# -*- coding: utf-8 -*-

# python列表机制，例如
# mystuff.append('hello')
# python在对列表调用append函数时具体作了什么？
# 1. 寻找mystuff变量，发现这是一个列表
# 2. mystuff这里有点运算符(Dot)operator，就去寻找列表拥有的一些方法
# 3. 找到append，对这个列表调用函数

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #pop(i)从列表中扔掉第i+1元素,pop(-1)扔掉最后一个
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!把空格插入到stuff列表元素之间
print '#'.join(stuff[3:5]) # super stellar!
