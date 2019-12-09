# -*- coding: utf-8 -*-
# @Data : 2019-12-09

'''
MVC 设计模式

M: 控制数据读取
V: 控制前端展示
C: 控制M的数据读取和V的视图改变

'''

quotes = ('A man is not complete until he is married. Then he is finished.',
            'As I said before, I never repeat myself.',
            'Behind a successful man is an exhausted woman.',
            'Black holes really suck...', 'Facts are stubborn things.')

class QuoteModel:

    def get_quote(self, n):
        if n <= 0:
            raise IndexError('index must be 1 or bigger.')
        try:
            value = quotes[n-1]
        except IndexError:
            value = 'NOT found!'
        return value
    

class QuoteTerminalView:

    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))
    
    def error(self, msg):
        print('Error: {}'.format(msg))
    
    def select_quote(self):
        return input('Which qoute number would you like to see?')
    

class QuoteTerminalController:

    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError:
                self.view.error("Incorret index '{}'".format(n))
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == "__main__":
    main()