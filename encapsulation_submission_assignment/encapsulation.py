
##Author: Kevin Montano
##
##Python v 3.11.7
##
##Purpose: A class that demonstrates encapsulation principles


#
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

    
            
            
