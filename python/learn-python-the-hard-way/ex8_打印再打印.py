# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

#formatter嵌套在formatter里，也就是说一个格式化语句可以放在另一
#格式化语句里
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# %s和%r的区别
# %s用在绝大数场景
# %r用在分析代码上，debugging
