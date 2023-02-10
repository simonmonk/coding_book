class Person:
    
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    def full_name(self):
        return self.first_name + ' ' + self.surname
        

p = Person('Simon', 'Monk')
print(p.full_name())