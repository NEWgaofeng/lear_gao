#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#test = "I'm %s. I'm %i years old" % ('Mr.gao', 27)
#print(test)

# 使用词典来进行传值

#print("I'm %(name)s. I'm %(age)d years old" % {'name':'Mr.gao','age':27})


#格式符
#格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:
#
#% s
#字符串(采用str()
#的显示)
#
#% r
#字符串(采用repr()
#的显示)
#
#% c
#单个字符
#
#% b
#二进制整数
#
#% d
#十进制整数
#
#% i
#十进制整数
#
#% o
#八进制整数
#
#% x
#十六进制整数
#
#% e
#指数(基底写为e)
#
#% E
#指数(基底写为E)
#
#% f
#浮点数
#
#% F
#浮点数，与上相同
#
#% g
#指数(e)或浮点数(根据显示长度)
#
#% G
#指数(E)
#或浮点数(根据显示长度)
#
#% % 字符
#"%"


#class Student(object):
#
#    def __init__(self, name, score):
#        self.name = name
#        self.score = score
#
#    def print_score(self):
#        print('%s: %s' % (self.name, self.score))

#class Student(object):
#
#    def __init__(self, name, score):
#        self.name = name
#        self.score = score
#
#    def print_score(self):
#        print('%s: %s' % (self.name, self.score))

# 封装 给Student类增加新的方法，get_grade：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >=90:
            return 'A'
        if self.score >=60:
            return 'B'
        else:
            return 'C'

#Jetli = Student('Jectli', 55)
#Bart = Student('Bart', 26)
#print(Jectli.name, Jectli.get_grade())
#print(Bart.name, Bart.get_grade())

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
