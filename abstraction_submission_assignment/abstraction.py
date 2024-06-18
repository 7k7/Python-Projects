
##Author: Kevin Montano
##
##Python v 3.11.7
##
##Purpose: A class that demonstrates abstraction principles


# import relevante modules to create abstract methods
from abc import ABC, abstractmethod


# This class acts as the parent class; Book
# Bio class will be the child class and implement the abstract method
# in the Book class
class Book:

    # This constructor method is called when instantiating a Book
    # Parameters: self instance, author name, book title, number of pages, 
    def __init__(self, author, title, pages):

        # assigns author attribute to the passed in argument value 'author'
        # a private var of type string
        # A Book's author should not have to be changed unless there is intent
        self.__author = author

        # assigns title attribute to the passed in argument value 'title'
        # type string and private variable
        # A Book's title should not have to be changed unless there is intent
        self.__title = title
        
        # assigns pages attribute to the passed in argument value 'pages'
        # type integer and protected variable
        # A Book's page amount could be updated if needed
        self._pages = pages


    # Methods:
    # setter and getter methods are provided to allow
    # users to update private values

    # Setter methods: update a Book's property values 

    # update the value of author
    def setAuthor(self, author):
            
        # For programmer debugging purposes
        # print statements allows us to see the before and after change
        print("Author current name: '{}'".format(self.__author))
            
        # sets the private author property to the new passed argument value
        self.__author = author

        # print our the update change to author
        print("Author updated name: '{}'".format(self.__author))

    # update the value of title
    def setTitle(self, title):

        # print the current value
        print("Title currently is: '{}'".format(self.__title))

        # sets the private title property to a new title value
        self.__title = title

        # print the new, updated title property value
        print("Title updated name: '{}'".format(self.__title))
        

    # Getter methods: retrieves the property values of a Book object

    # get author property value
    def getAuthor(self):
        print("getAuthor() returned: '{}'".format(self.__author))
        return self.__author

    # get title property value
    def getTitle(self):
        print("getTitle() returned: '{}'".format(self.__title))
        return self.__title

    # get pages property value
    def getPages(self):
        print("getPages() returned: '{}'".format(self._pages))
        return self._pages

    # Abstract method
    # only defines the method not its implementation

    # a short description of the Book
    @abstractmethod
    def aboutTheBook(self, description):
        pass


# This is a class definition of the a child class
# parent class is Book
class Bio(Book):

    # inherits all properties of Book

    # a few more properties that pertain to a biography book
    def __init__(self, author, title, pages, person, birthplace, education, work):
        Book.__init__(self, author, title, pages)
        
        self.__author = author
        self.__title = title
        self._pages = pages
        self._person = person
        self._birthplace = birthplace
        self._education = education
        self._work = work

    # Implementing its parent's class abstract method
    def aboutTheBook(self, description):
        print("This biopgrahy, '{}' by '{}', is the recounting of the life of '{}'. \
            \nSome profile information: {}".format(self.getTitle(), self.getAuthor(), self._person, description))



# This is the start of the program
# if run as the main program not as a script
# I demonstrate how a Book can be instantiated and
# modified 
if __name__ == "__main__":

    # instantiate a Book and passing in the required arguments
    oliverTwistBk = Book('Ernest Hemingway', 'Oliver Twist', 320)

    # print Book
    print("Book author: '{}' - title: '{}' - pages: '{}'".format(oliverTwistBk.getAuthor(), oliverTwistBk.getTitle(), oliverTwistBk.getPages()))

    # Because the author is incorrect, the setter method
    # is called to update the property '__author'
    oliverTwistBk.setAuthor('Charles Dickens')

    # the 'Oliver Twist' book actually has 608 pages
    # will update the pages property of this Book
    oliverTwistBk._pages = 608

    # lets see the changes by retrieving it via getter method
    oliverTwistBk.getPages()

    # instantiate a Bio
    theFirstAmericanBio = Bio('H. W. Brands', 'The First American: The Life and Times of Benjamin Franklin', \
                              784, 'Benjamin Franklin', 'Boston, Massachusetts', 'limited formal education; self-taught', \
                              'diplomat, scientist, philosopher, businessman and inventor')

    # This var will be passed into the abstract method aboutThebook
    # Contains data specific to the book
    profile = "\nbirthplace: " + theFirstAmericanBio._birthplace + "\neducation: " + theFirstAmericanBio._education + "\nwork: " + theFirstAmericanBio._work

    # calling the abstract method with the above argument
    theFirstAmericanBio.aboutTheBook(profile)
    
            
            
