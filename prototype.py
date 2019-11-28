# -*- coding: utf-8 -*-
# @Data : 2019-11-28

'''
原型模式

1. 类实例化之后的 __dict__ 只包含 self 的对象, 类的 __str__ 输出的是字符串
2. 通过 可变参数 定义一个类, 使用 __str__ 输出格式化信息, 使用 clone 方法去更新这个类
'''

import copy
from collections import OrderedDict


class Book:
    
    def __init__(self, name, authors, price, **kwargs):
        '''kwargs: 出版商、长度、标签、出版日期'''
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(kwargs)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for k in ordered.keys():
            mylist.append('{}:{}'.format(k, ordered[k]))
            if k == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)
        

class Prototype:
    
    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def unregister(self, identifier):
        del self.objects[identifier]
    
    def clone(self, identifier, **kwargs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(kwargs)
        return obj

def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
                price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
                tags=('C', 'programming', 'algorithms', 'data structures'))
    print(b1)
    print(b1.__dict__)
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99, lengtg=274, publication_date='1988-04-01', edition=2)

    for i in (b1, b2):
        print(i)
    print("ID b1: {} != ID b2: {}".format(id(b1), id(b2)))



if __name__ == "__main__":
    main()
    b1 = Book("a", "b", "c")
    d = "a:1, b:2, c:3"
    # print(d.__dict__)
    # print(b1.__dict__)