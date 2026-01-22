# Author: Gerardo Villegas
# GitHub username: villegag-droid
# Date: Oct 7th, 2025
# Description: 
#   This program is a class with three data members to track the position on a xy plane and the odometer reading that changes for each space moved
#   Assuming no requirement for listing the current coordinates of a cab


class Taxicab:


#    ""
#        Starts Taxicab and sets odometer to 0
#        
#        Arguments: x_coord - makes list for x coordinates
#                   y_coord - makes list for y coordinates
#                                                                     ""


    def __init__(self, x_coord, y_coord):


#   This is used for adding x coords to the "list" for a taxi 

        self._x_coord = x_coord


#             This is used for adding y coords to the "list" for a taxi

        self._y_coord = y_coord


#           This is used for making current odometer apart of the "list" for the taxi and setting it to zero 

        self._current_odometer = 0




    def move_x(self, x_coord):


#    ""
#        Moves the cab in the x direction and updates the odometer.
#        
#        Arguments: x_coord - Moves the car in the x direction given
#                                                                     ""

        self._x_coord += x_coord

        self._current_odometer += abs(x_coord)

        print(f"you have moved in the x direction {abs(x_coord)} space(s) and your odometer has gone up by {abs(x_coord)}")
        





    def move_y(self, y_coord):
#    ""
#        Moves the cab in the y direction and updates the odometer.
#        
#        Arguments: y_coord - Moves the car in the y direction given
#                                                                      ""     
        self._y_coord += y_coord

        self._current_odometer += abs(y_coord)

        print(f"you have moved in the y direction {abs(y_coord)} space(s) and your odometer has gone up by {abs(y_coord)}")


    



    def get_odometer(self):
#       ""
#           This is a getter used to get the total odometer I made it into a string instead of the value so that it makes more sense when printing 
#           Does it count as a getter if it doesnt return an int or float but a str?
#                                                            ""
        return f"Your current odometer mileage is: {self._current_odometer }"
    

    def get_x_coord(self):


        return self._x_coord
    
    def get_y_coord(self):

        return self._y_coord


    

