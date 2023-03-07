class School:
    def __init__(self, maths, english, physics, chemistry, biology):
        self.subject = maths
        self.subject = english
        self.subject = physics
        self.subject = chemistry
        self.subject = biology

        



class Person(School):
    def __init__(self, name, age, maths, english, physics, chemistry, biology):
        super().__init__(self, name, age, maths, english, physics, chemistry, biology)
        self.name = name
        self.age = age