# -*- coding: utf-8 -*-
# @Data : 2019-11-26

'''
抽象工厂

要点: 玩游戏为核心调用类, 具体玩的游戏是不同的类, 通过main方法, 根据判断, 选择玩不同的游戏
'''

class Frog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))
    

class Bug:
    def __str__(self):
        return 'a bug'
    
    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t----- Frog World -----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))
    

class Ork:
    def __str__(self):
        return 'an evil ork'
    
    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t----- Wizard World ------'
    
    def make_character(self):
        return Wizard(self.player_name)
    
    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    
    def play(self):
        self.hero.interact_with(self.obstacle)
        
def validate_age(name):
    try:
        age = input('Welcome {}. How old are you? \n'.format(name))
        age = int(age)
    except ValueError:
        print("Age {} is invalid, please try again...".format(age))
        return (False, age)
    return (True, age)

def main():
    name = input("Hello. What's your name? \n")
    vaild_input = False
    while not vaild_input:
        vaild_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    envrionment = GameEnvironment(game(name))
    envrionment.play()


if __name__ == "__main__":
    main()