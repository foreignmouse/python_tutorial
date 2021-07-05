class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Elon", "Musk")
print(x.graduationyear)

class Primary(Student):
    def __init__(self, fname, age):
        self.nianling = age
    def calculate(self):
        return (self.nianling + 1) 


cyrus = Primary("hanzhe", 9)
print(cyrus.nianling) 

print(cyrus.calculate())
