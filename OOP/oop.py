# single inheritance
"""  class Parent:
    def __init__(self, name, job):
        self.pname = name
        self.pjob = job

class Child(Parent):
    def __init__(self, cname, pname, pjob):
        super().__init__(pname, pjob)

        self.child_name = cname
    
peter = Child('Peter', 'James', 'Programmer')
print(peter.pjob)
print(peter.pname)""" 


# multiple inheritance
"""class Mother:
    def __init__(self, name):
        self.mname = name

class Father:
    def __init__(self, name):
        self.fname = name

class Child(Father, Mother):
    def __init__(self, cname, mname, fname):
        super().__init__(fname)
        Mother.__init__(self, mname)

        self.child_name = cname
            
man = Child('James', 'Sasha', 'Peter', )         
print(man.fname)
print(man.child_name)"""


# multi-level inheritance
"""class GrandParent:
    def __init__(self, name):
        self.gname = name

class Parent(GrandParent):
    def __init__(self, name, gname):
        super().__init__(gname)
        self.pname = name

class Child(Parent):
    def __init__(self, cname, pname, gname):
        super().__init__(pname, gname)
        self.child_name = cname

man = Child('Peter', 'James', 'Charlie')
print(man.gname)"""


#hierachical inheritance
"""class Parent:
    def __init__(self, name):
        print('I am the father')
        self.pname = name

    def getfather(self):
        print('I am a father')

class Child1(Parent):
    def __init__(self, cname, pname):
        super().__init__(pname)
        self.child_name = cname
    
class Child2(Parent):
    def __init__(self, cname, pname):
        super().__init__(pname)
        self.child_name = cname

man = Child1('Max', 'David')
print(man.pname)"""


# hybrid inheritance
"""class GrandParent:
    def __init__(self, grandma, grandpa):
        self.grandma = grandma
        self.grandpa = grandpa

class Father(GrandParent):
    def __init__(self, name, grandma, grandpa):
        GrandParent.__init__(self, grandma, grandpa)
        self.pname = name

class Mother(GrandParent):
    def __init__(self, name, grandma, grandpa):
        GrandParent.__init__(self, grandma, grandpa)
        self.mname = name

class Child(Father, Mother):
    def __init__(self, cname, father, mother, grandma, grandpa):
        Father.__init__(self, father, grandma, grandpa)
        Mother.__init__(self, mother, grandma, grandpa)
        self.child_name = cname

family = Child('Max', 'John', 'Sasha', 'Jerry', 'Tom')
print(family.mname)"""