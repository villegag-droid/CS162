# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 10-29-25
# Description:
# This module sorts a list of strings alphabetically (case-insensitive) 
# using insertion sort and demonstrates the sorting with a sample list.

def string_sort(list):
    """
    Sorts a list of strings in alphabetical order using insertion sort.

    """
    for index in range(len(list)):
        value = list[index]
        pos = index - 1

        # Shift elements that come after 'value' alphabetically
        while pos >= 0 and list[pos].lower() > value.lower():
            list[pos + 1] = list[pos]
            pos -= 1

        # Place 'value' in its correct position
        list[pos + 1] = value