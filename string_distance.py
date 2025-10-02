# Author: Gerardo Villegas
# GitHub username: villegag-droid
# Date: Oct 1st, 2025
# Description: 
#   This program asks the user for 3 words to be inputted then it asks for the word to compare those previous ones to.
#   It then compares the words and assigns a value of how alike that word is and adds the word plus that value to a dictionary that gets printed

from fuzzywuzzy import fuzz  # import fuzz from fuzzywuzzy for string similarity

def main():
    """
    main function which gets both inputs which are a list and a single str 
    which then get compared and assigned a value in a new list called dictionary_list
    """
    
    # Prompt user to enter 3 words separated by spaces
    word_0, word_1, word_2 = input("Enter 3 words separated by one space: ").split()
    
    # words added to list
    fuzzy_list = [word_0, word_1, word_2]
    
    # Start a new list to intake previous list plus values to those words
    dictionary_list = {}
    
    # Prompt user for the word to compare against the list
    compare_word = input("Compare to what word? ")
    
    # Loop through each word in the list and calculate similarity
    for word in fuzzy_list:

    # calculate similarity
        similarity = fuzz.ratio(word, compare_word)  

    # store in dictionary
        dictionary_list[word] = similarity           

    # Print the final dictionary adding words to their similarity scores
    print(dictionary_list)

# Call the main function to execute the program
main()