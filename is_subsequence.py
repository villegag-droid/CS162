# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 11-5-25
# Description: checks wether first arguement contains the same letters in the same order as arguement 2 


def is_subsequence( str1, str2 ):

    #if all letters are deleted from str2 then false
    if str2 == "":
        
        return False

    if str1 == str2 or str1 == "":
        
        return True
    
    if str1[0] == str2[0]:

        #restarts function without the first letter of both strings
        return is_subsequence(str1[1:], str2[1:])
    
    #if no if functions are true restarts function from second letter of second arguement
    return is_subsequence(str1, str2[1:])

