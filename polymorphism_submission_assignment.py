


# Python: 3.11.7
#
# Author: Kevin Montano
#
# Purpose:  This python program is part of The Tech Academy Python Course -
#           POLYMORPHISM SUBMISSION ASSIGNMENT
#           Demonstrating two child classes inheriting attributes and functions
#           from a parent class and utilizing polymorphism to aggregate/modify
#           inherited class methods and properties in child classes



# parent class
class Person:
    # init dunder method is always called to instantiate an object of this class
    # requires firstname and lastname arguments to initialize the instance
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    # class method; prints first and last name of a Person instance
    def greeting(self):
        print('Hello, {} {}. Hope you are having a good day.'.format(self.firstname, self.lastname))


# child class of Person class
class Student(Person):
    # initialization class method when instantiating a new object of type Teacher
    # attribute: self - access all objects attributes
    # attributes: firstname and lastname inherited from parent class Person 
    # age and graduationyear are specific to the Student class type 
    def __init__(self, fname, lname, age, year):
        # super() ref/inherits the parent class' init method
        super().__init__(fname, lname)
        self.age = age
        self.graduationyear = year

    # utilize polymorphism on the parent class method: greeting()
    def greeting(self):
        # prints welcome message using most attr values for this instance of Student
        print('Welcome', self.firstname, self.lastname, "to the class of", self.graduationyear)


# child class of Person class
class Teacher(Person):
    # initialization class method when instantiating a new object of type Teacher
    # attribute: self - access all objects attributes
    # attributes: firstname and lastname inherited from parent class Person
    # classname and gradelevel are specific to the Teacher class type 
    def __init__(self, fname, lname, classname, gradelevel): # 3 attributes are parameters needed
        # super() ref/inherits the parent class' init method
        super().__init__(fname, lname) 
        # notice how there is no need to assign/declare object properties with class properties
        # because of polymorphism, only the attributes specific to this class are declared here
        self.classname = classname
        self.gradelevel = gradelevel
        
    # utilize polymorphism on the parent class method: greeting()
    def greeting(self):
        # outputs message with Teacher instances' own attr values
        print('Hello class and welcome, to the {}th grade {} class!\nMy name is {} {}.'
              .format(self.gradelevel, self.classname, self.firstname, self.lastname))
        
    


if __name__ == '__main__':

    # Instantiating a Person object type and passing required arguments
    # Parent class; referencing the __init__ class method/constructor
    john = Person('John', "Smith")
    # welcome message: print first and last names of this instance of type Person
    john.greeting()

    # Instantiating a Student object type and passing required arguments
    # child class to Person class type
    benny = Student('Benny', 'McCoy', 15, 2019) 
    # prints welcome message with the firstname and lastname of Student is-a Person 
    benny.greeting()


    # Instantiating a Teacher object type and passing required arguments
    teacher1 = Teacher('Benjamin', 'Morgan', 'Trigonometry', '10')
    # call to parent class' method
     # prints welcome message with the firstname and lastname of Teacher is-a Person
    teacher1.greeting()











    
