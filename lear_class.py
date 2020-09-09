#!/usr/bin/env python-字符串格式化
# -*- coding:utf-8 -*-

# 创建一个类，创建一个object类
class Student(object):
    pass

# 变量bart指向 Student 实例
bart = Student()
bart

# 给变量bart
bart.name = 'Bart Simpson'
bart.name

# 类可以起到模板的作用，通过特殊的__init__的方法，在创建实例的时候，把name，score等属性绑上去
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

# __init__ 方法 第一个参数永远是self，__init__方法内部，可以把各种属性绑定到self，因为self就指向创建本身
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，python解释器自己会把实例变量传进去

bart = Student('Bart Simpson', 59)
bart.name
bart.score






















