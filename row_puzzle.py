# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 11-5-25
# Description: I dont know how to explain so im stealing from github assignment:
# takes a list of integers as a parameter and returns True if the puzzle is solvable for that row, but returns False otherwise
# this should have been the whole assignment too much brain power needed 
# spent like 4 times the amount of time on this then the others and not worth as much points compared to time to complete others 
# should hae been worth more points at the minimum

def row_puzzle(array):
    
        
        
    def solver(location, memo):

        #checks if location is at the last spot of the array completing puzzle
        if location == ( len(array) - 1 ):
            return True

        if location in memo:
            return False
        
        #stores current location
        memo.add(location)

        #how many places to move
        move_value = array[location]

        
        #moves right if True
        if location + move_value < len(array):
            if solver(location + move_value, memo):
                return True
    
        #moves left if True
        if location - move_value >= 0:
            if solver(location - move_value, memo):
                return True
            
        memo.remove(location)

        return False

    return solver( 0, set() )

        
