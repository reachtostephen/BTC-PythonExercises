''' #Class, Inheritance, Encapsulation
class Employee:
    designation = "Software Engineer" #Class attribute

    def __init__(self, name, age):
        self.__gender = 'male' #Encapsulation
        self.name = name
        self.age = age

    def work(self, shift):
        return "{} works in {} shift".format(self.name, shift)

    def details(self):
        return "{} is {} of age and is a {}".format(self.name, self.age, self.__gender)


class Sub(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Sub class is called")

    def tech(self, technology):
        print("{} works in {}".format(self.name, technology))


abc = Employee('ABC', 21)
defg = Employee('DEFG', 27)
print(defg.details())

print("{} is a {} and was aged {}".format(abc.name, abc.__class__.designation, abc.age))
print("{} is a {} and was aged {}".format(defg.name, defg.__class__.designation, defg.age))

print(abc.work("night"))
print(defg.work("day"))

sub = Sub('Steve', 21)
sub.tech('Python')
'''


# Polymorphism
class Python:
    def __init__(self, name):
        self.name = name

    def work(self):
        return "{} works in Python".format(self.name)


class Java:
    def __init__(self, name):
        self.name = name

    def work(self):
        return "{} works in Java".format(self.name)


abc = Python('abc')
print(abc.work())
defg = Java('def')
print(defg.work())
