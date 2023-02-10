class Person:
    
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    def full_name(self):
        return self.first_name + ' ' + self.surname
        
class Employee(Person):
    
    def __init__(self, first_name, surname, salary):
        Person.__init__(self, first_name, surname)
        self.salary = salary
        
    def give_rise(self, percent):
        self.salary += self.salary * percent / 100
    

p = Employee('Simon', 'Monk', 100)
p.give_rise(10)
print(p.salary)