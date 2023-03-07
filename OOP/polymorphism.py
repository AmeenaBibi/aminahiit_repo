# inheritance
class Animal:
    def type(self):
        print('This ia an animal')

    def legs(self):
        print('it has 4 legs')

class Spider(Animal):
    def legs(self):
        print('It has 8 legs')

a = Spider()
a.legs()
a.type()