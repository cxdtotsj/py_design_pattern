# -*- coding: utf-8 -*-
# @Data : 2019-11-29

'''
适配器模式

对于不同名称,想要适配的方法, 可以使用待适配的方法名,作为字典的KEY, 被适配的不同对象的方法名, 作为VALUE, 更新至 Adapter 类的 __dict__ 中;
对于不同适配类的相同变量和方法, 可以在适配配中, 定义相同名称的方法, 通过 self.obj 调用, 做兼容处理

'''

# 待兼容类
class Synthesizer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    
    def play(self):
        return 'is playing an electronic song'
    

# 待兼容类
class Human:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return '{} the human'.format(self.name)
    
    def speak(self):
        return 'say hello'
    

# 被兼容类
class Computer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} computer'.format(self.name)
    
    def execute(self):
        return 'execute a program'


# 适配器
class Adapter:
    def __init__(self, obj, adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)
    
    def __str__(self):
        return str(self.obj)
    
    @property
    def name(self):
        return self.obj.name

def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    hunman = Human('Bob')
    objects.append(Adapter(hunman, dict(execute=hunman.speak)))

    # print(objects)
    for obj in objects:
        print('{} {}'.format(str(obj), obj.execute()))
    for obj in objects:
        print(obj.name)
    
        
if __name__ == "__main__":
    main()