# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 10-29-25
# Description: 
# This module defines a Box class with dimensions and a method to compute its volume. 
# It also includes a function to sort a list of Box objects by their volumes in descending order.

class Box:
    """
    Represents a 3D rectangular box with length, width, and height.
    """

    def __init__(self, length, width, height):
        """
        Initializes a Box object with the given dimensions.
        """
        self._length = length
        self._width = width
        self._height = height 

    def get_length(self):
        return self._length
    
    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def volume(self):
        """
        Computes and returns the volume of the box.
        """
        return (self._length * self._width * self._height)
    
def box_sort(list):
    """    
    Sorts a list of Box objects by their volume in descending order using insertion sort.
    This function modifies the input list in-place by replacing Box objects with their volumes.
    """
    # Convert Box objects to their volumes to make sorting easier
    for place in range(len(list)):
        list[place] = list[place].volume()

    # Perform insertion sort on the list of volumes
    for index in range(1, len(list)):        
        value = list[index]        
        pos = index - 1        

        while pos >= 0 and list[pos] < value:            
            list[pos + 1] = list[pos]            
            pos -= 1        

        list[pos + 1] = value



b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
box_list = [b1, b2, b3]
box_sort(box_list)
    
print(box_list)
