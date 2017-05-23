# -*- coding: utf-8 -*-

# Object-Oriented Programming (OOP)面向对象编程

#模块modules
# A Python file with some functions or variables in it ..
# You import that file.
# And you can access the functions or variables in that module with the . (dot) operator.
# 模块和字典的相似之处在于都遵循从什么得到什么的程式，也就是键和值对应，模块名对应于里面的函数和变量名，字典用[]取值，模块用.取值

#模块和类很像
#模块可以看做是特殊化的字典，它对应的值是python代码，用.根据键取值
#类是把一组函数和数据放到一个容器里，通过dot operator获取使用

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

#为什么使用类
# You can take this MyStuff class and use it to craft many of them, millions at a time if you want, and each one won't interfere with each other.
# When you import a module there is only one for the entire program unless you do some monster hacks.

#对象和import很像
#modules是需要import才能使用
#class则需要实例化（instantiate），生成对象才能使用

thing = MyStuff()
thing.apple()
print thing.tangerine

#上述代码的执行过程
# 1. Python looks for MyStuff() and sees that it is a class you've defined.
# 2. Python crafts an empty object with all the functions you've specified in the class using def.
# 3. Python then looks to see if you made a "magic" __init__ function, and if you have it calls that function to initialize your newly created empty object.
# 4. In the MyStuff function __init__ I then get this extra variable self, which is that empty object Python made for me, and I can set variables on it just like you would with a module, dictionary, or other object.
# 5. In this case, I set self.tangerine to a song lyric and then I've initialized this object.
# 6. Now Python can take this newly minted object and assign it to the thing variable for me to work with.

class Song(object):#如果没有合适的父类，就采用统一的object类，这是所有的类都会继承的类

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
