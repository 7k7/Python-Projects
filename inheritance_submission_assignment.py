
# Python: 3.11.7
#
# Author: Kevin Montano
#
# Purpose:  This python program is part of The Tech Academy Python Course -
#           INHERITANCE SUBMISSION ASSIGNMENT
#           Containing two classes that inherit from another class;
#           demonstrating a parent-child class relationship



# This is a very simplified parent-child relationship between
# chair and different kinds of chairs
# but the gist of it is:
# a chair seats a person and the other two kinds of chairs
# have specific purposes and characterics



# Parent class definition/structure
# Chair class type:
# a chair by definition is something that
# humans use to sit on; elevated from the ground
class Chair:
    # This init dunder method to denote that each attribute will 
    # be initialized upon instantiation of this class object type
    def __init__(self, material, seatHeight, hasArmrests, hasBackrest):
        material = self.material
        seatHeight = self.seathight
        hasArmrests = self.hasArmrests
        hasBackrest = self.hasBackrest
        # behavior: can be used to seat someone
        # by default, chairs are in a 'stand-by' state
        sitOn = 'unseated' 

        
# Child class Dining_Chair from parent Chair
# Dining chair are concerned with:
# style i.e. modern contemp, electric, industrial
# finishes i.e. wood finishes like vernish, resin, lacquer
# legs total amount
# note that each child class references the parent class in the class def
class Dining_Chair(Chair):
    # This init dunder method to denote that each attribute will 
    # be initialized upon instantiation of this class object type
    def __init__(self, finishType, styleType, legsTotal):
        finishType = self.finishType
        styleType = self.styleType
        legsTotal = self.legsTotal
        

# This is another child class from Chair called Office_Chair
# An instance of this class has many different
# features than other more straightforward, and simple kinds of chairs
# In a nutshell, the attributes are very specific and comfort, and ergonomic
# oriented
class Office_Chair(Chair):
    # This init dunder method to denote that each attribute will 
    # be initialized upon instantiation of this class object type
        def __init__(self, adjustableSeatHeight, seatDepth, seatTilt,
                     hasLumbarSupport, hasBackrestRecline, hasSwivel,
                     hasHeadrest, wheelsTotal):
            adjustableSeatHeight = self.adjustableSeatHeight
            seatDepth = self.seatDepth
            seatTilt = self.seatTilt
            hasLumbarSupport = self.hasLumbarSupport
            hasBackrestRecline = self.hasBackrestRecline
            hasSwivel = self.hasSwivel
            hasHeadrest = self.hasHeadrest
            wheelsTotal = self.wheelsTotal
            # Behaviors:
            # by default, chairs are in a 'stand-by' state
            swivelAround = 'still'
            rollChair = 'still'
            adjustHeight = 'no adjustment'
            adjustTilt = 'no adjustment'
            adjustHeadrest = 'no adjustment'
            reclineBackrest = 'no recline'





            
    
