# Author: Gerardo Villegas
# GitHub username: villegag-droid
# Date: Oct 7th, 2025
# Description: 
#               This program has a class for students and their grades adn has another function which takes
#                the grades of the studets and gives a tuple of mean, median, and mode


import statistics



class Student:


#    ""
#        Starts Student
#        
#        Arguments: name - adds a name onto the student list
#                   grade - adds a grade onto the student list
#                                                                     ""


    def __init__(self, name, grade):


        self._name = name


        self._grade = grade


    def get_grade(self):


        return self._grade



# Returns mean median and mode in a tuple I think...


def basic_stats(student_list):


# finds the mean, median, and mode of grades from a list of Students

# Arguments: student_list - list of Student instances

# Returns: A tuple containing mean, median, and mode of the students' grades.


    grade_list = []


    for student in student_list:


        grade_list.append(student.get_grade())


    grade_mean = statistics.mean(grade_list) 


    grade_median = statistics.median(grade_list) 


    grade_mode = statistics.mode(grade_list)


    return (grade_mean, grade_median, grade_mode )

