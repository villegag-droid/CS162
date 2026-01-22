# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 11-12-25
# Description: 
# This program contains two classes that generates a Linked list that can call on the head of list, add a node, remove a ndoe,
# return true or false if any node contains a certain value, reverse the list, and make the list into a normal list


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Represents a singly linked list with recursive operations.

    Attributes:
        _head: The first Node in the list (private).

    Methods:
        get_head(self):
        
        add(self, val):
        
        remove(self, val):
        
        contains(self, val):
        
        insert(self, val, position):
        
        reverse(self):
        
        to_plain_list(self):
    """

    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head

    def add(self, val):
        """
        Adds a value to the end of the linked list recursively.
        """
        def add_helper(current):

            if current.next is not None:
                current = current.next
                return add_helper(current)
        
            current.next = Node(val)

        if self._head is None:
            self._head = Node(val)

        else:
            add_helper(self._head)



    def remove(self,val):
        """
        Removes the first occurrence of a value from the linked list recursively.
        """

        def remove_helper(current, previous):

            if current is not None and current.data != val:

                
                return remove_helper(current.next, current)
            
            if current is not None:

                previous.next = current.next


        if self._head is None:
            return
        if self._head.data == val:
            self._head = self._head.next
        else:
            remove_helper(self._head.next, self._head )



#if value in list returns true otherwise false
    def contains(self, val):
        """
        Checks if a value exists in the linked lits recursively.
        """
        def contain_helper(current, val):
            if current is None:
                return False
            
            if current.data == val:
                return True
            
            return contain_helper(current.next, val)
            
           
            
        if self._head is None:
            return False
        
        return contain_helper(self._head, val)



#insert a value at a certain count of node 4 parameters for helper current node, value, position, count
    def insert(self,val, position):
        """
        Inserts a value at the specified position recursively.
        """
#recursive function that makes the previous node go to the new node then new node leads to next node

        def insert_helper(current, value, position, count, previous):

            if count == position or current is None:

                new_node = Node(value)

                if previous is not None:
                    previous.next = new_node

                new_node.next = current
                
                return
            
            count += 1
            return insert_helper(current.next, value, position, count, current)

        if position == 0:

            new_head = Node(val)
            new_head.next = self._head
            self._head = new_head
            return

        count = 0

        if self._head is None:

            self._head = Node(val)
            return

        return insert_helper(self._head, val, position, count,None )



#reverses list
    def reverse(self):
        """
        Reverses the linked list recursivley.
        """
        if self._head is None:
            return

        def reverse_helper(current):

            if current is None or current.next is None:
                return current
            
            new_head = reverse_helper(current.next)

            current.next.next = current

            current.next = None

            return new_head
            
        
        self._head = reverse_helper(self._head)



#makes node list into normal list
    def to_plain_list(self):
        """
        Converts the linked list into a standard Python list recursively.
        """
        plain_list = []
      
        
        
        def plain_list_helper(current):

            if current is None:
                return
            
            plain_list.append(current.data)
            plain_list_helper(current.next)

        plain_list_helper(self._head)
        return plain_list




