# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 10-29-25
# Description:
# This module compares the performance of bubble sort and insertion sort 
# on randomly generated lists and plots the time taken for different list lengths.

import matplotlib.pyplot as pyplot
import random as rand
import time



def bubble_time(a_list):    
    """
    Sorts a_list in ascending order using bubble sort and returns the time taken.
    """
    start_time = time.perf_counter()  

    # Perform bubble sort
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):            
            if a_list[index] > a_list[index + 1]:                
                temp = a_list[index]                
                a_list[index] = a_list[index + 1]                
                a_list[index + 1] = temp

    end_time = time.perf_counter()  
    total_time_elapsed = end_time - start_time
    return total_time_elapsed

def insertion_time(a_list):    
    """
    Sorts a_list in ascending order using insertion sort and returns the time taken.
    """
    start_time = time.perf_counter()  

    # Perform insertion sort
    for index in range(1, len(a_list)):        
        value = a_list[index]        
        pos = index - 1        
        while pos >= 0 and a_list[pos] > value:            
            a_list[pos + 1] = a_list[pos]            
            pos -= 1        
        a_list[pos + 1] = value

    end_time = time.perf_counter()  
    total_time_elapsed = end_time - start_time
    return total_time_elapsed

def sort_times_for_random_list(items_in_list):
    """
    Generates a random list of given length and returns the time taken 
    for bubble sort and insertion sort.
    """
    # Create a list of random integers
    random_list = [rand.randint(1, items_in_list) for _ in range(items_in_list)]
    
    # Make a copy of the list to keep the original unsorted for the second sort
    list_copy = random_list.copy()

    # Measure time for each sorting algorithm
    total_time_insertion = insertion_time(random_list)
    total_time_bubble = bubble_time(list_copy)

    return (total_time_bubble, total_time_insertion)

def compare_sorts():
    """
    Compares bubble sort and insertion sort for lists of various lengths 
    and plots the time taken for each.
    """
    x_list = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    bubble_y_list = []
    insertion_y_list = []

    # Calculate sorting times for each list length
    for length in x_list:
        both_times = sort_times_for_random_list(length)
        bubble_y_list.append(both_times[0])
        insertion_y_list.append(both_times[1])

    # Plot bubble sort times
    pyplot.plot(x_list, bubble_y_list, 'ro--', linewidth=2, label='Bubble List')
    
    # Plot insertion sort times
    pyplot.plot(x_list, insertion_y_list, 'go--', linewidth=2, label='Insertion List')
        
    pyplot.xlabel("List length")
    pyplot.ylabel("Time taken")
    pyplot.legend(loc='upper left')
    pyplot.show()