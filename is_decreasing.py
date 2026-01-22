# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 11-5-25
# Description: checks wether array given is decreasing which return true and vice versa

def is_decreasing(array):

    if len(array) <= 1:
        
        return True
    
    if array[0] < array[1]:
        
        return False

    
    del array[0]

    return is_decreasing(array)

