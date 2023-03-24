class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lectuer(Mentor):
    pass

class Reviewer(Mentor):
    pass

tom = Lectuer('Tom','Wilson')
print(tom.name, tom.surname)
