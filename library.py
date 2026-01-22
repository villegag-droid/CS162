# Author: Gerardo Villegas
# GitHub username: Villegag-droid
# Date: 11-19-25
# Description: This program models a library system with Books, Albums, Movies, and Patrons. 
#              It allows adding items and patrons, checking out and returning items, requesting items, 
#              paying fines, and tracking overdue items.


class LibraryItem:
    
    """Represents a general library item."""

    def __init__(self, library_item_id, title):
        self.library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        return self.library_item_id
    
    def get_checked_out_by(self):
        return self._checked_out_by
    
    def set_checked_out_by(self, patron):
        self._checked_out_by = patron

    def set_requested_by(self, patron):
        self._requested_by = patron

    def get_requested_by(self):
        return self._requested_by
    
    def get_location(self):
        return self._location
    
    def set_location(self, location):
        self._location = location

    def get_title(self):
        return self._title
    
    def set_date_checked_out(self, date):
        self._date_checked_out = date

    def get_date_checked_out(self):
        return self._date_checked_out

class Book(LibraryItem):

    """Represents a book in the library."""

    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        return self._author
    
    def get_check_out_length(self):
        return 21
    
class Album(LibraryItem):
    """Represents a music album in the library."""

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        return self._artist
    
    def get_check_out_length(self):
        return 14
    
class Movie(LibraryItem):
    """Represents a movie in the library."""

    def __init__(self, library_item_id, title, director):

        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        return self._director
    
    def get_check_out_length(self):
        return 7


class Patron:
    """Represents a library patron."""

    def __init__(self, patron_id, name):

        self.patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def get_patron_id(self):
        return self.patron_id
    
    def get_name(self):
        return self._name
    
    def get_checked_out_items(self):
        return self._checked_out_items

    def get_fine_amount(self):
        return self._fine_amount
    
    def set_fine_amount(self, amount):
        self._fine_amount = amount

    def add_library_item(self, library_item):
        """Adds a library item to the patron's checked out items."""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Removes a library item from the patron's checked out items if it exists."""
        if library_item in self._checked_out_items:
            self._checked_out_items.remove(library_item)

    def amend_fine(self, amount):
        """Adjusts the patron's fine by a specified amount."""
        self._fine_amount += amount


class Library:
    """Represents the library system containing items and patrons."""

    def __init__(self):

        self.holdings = {}
        self.members = {}
        self.current_date = 0

# add_library_item - takes a LibraryItem object as a parameter and adds it to the holdings
    def add_library_item(self, library_item):
        """Adds a library item to the library holdings."""

        self.holdings[library_item.get_library_item_id()] = library_item

# add_patron - takes a Patron object as a parameter and adds it to the members
    def add_patron(self, patron):
        """Adds a patron to the library members."""

        self.members[patron.get_patron_id()] = patron

# lookup_library_item_from_id - returns the LibraryItem object corresponding to the ID parameter, or None if no such LibraryItem is in the holdings
    def lookup_library_item_from_id(self, library_item_id):
        """Returns the Patron corresponding to the ID, or None if not found."""
       

        if library_item_id in self.holdings:
            return self.holdings[library_item_id]
        
        else:
            return None
        
# lookup_patron_from_id - returns the Patron object corresponding to the ID parameter, or None if no such Patron is a member
    def lookup_patron_from_id(self, patron_id):

        if patron_id in self.members:
            return self.members[patron_id]
        
        else:
            return None
        
# check_out_library_item
    def check_out_library_item(self, patron_id, library_item_id):
        """Allows a patron to check out a library item."""

        patron = self.lookup_patron_from_id(patron_id)

        if patron is None:
            return "patron not found"
        
        library_item = self.lookup_library_item_from_id(library_item_id)

        if library_item is None:
            return "item not found"
        
        if library_item.get_location() == "CHECKED_OUT":
            return "item already checked out"
        
        if (library_item.get_requested_by() is not None and 
            library_item.get_requested_by() != patron):
            return "item on hold by other patron"
        
        library_item.set_date_checked_out(self.current_date)
        library_item.set_location("CHECKED_OUT")
        library_item.set_checked_out_by(patron)
        
        if library_item.get_requested_by() == patron:
            library_item.set_requested_by(None)
        
        patron.add_library_item(library_item)
        
        return "check out successful"
    

    def return_library_item(self, library_item_id):
         
        # """Returns the LibraryItem corresponding to the ID, or None if not found."""
        
        library_item = self.lookup_library_item_from_id(library_item_id)

        if library_item is None:
            return "item not found"
        
        if library_item.get_location() != "CHECKED_OUT":
            return "item already in library"
        
        patron = library_item.get_checked_out_by()
        patron.remove_library_item(library_item)
        
        if library_item.get_requested_by() is not None:
            library_item.set_location("ON_HOLD_SHELF")

        else:
            library_item.set_location("ON_SHELF")
        
        library_item.set_checked_out_by(None)
        
        return "return successful"


    def request_library_item(self, patron_id, library_item_id):

        patron = self.lookup_patron_from_id(patron_id)

        if patron is None:
            return "patron not found"
        
        library_item = self.lookup_library_item_from_id(library_item_id)

        if library_item is None:
            return "item not found"
        
        if library_item.get_requested_by() is not None:
            return "item already on hold"
        
        library_item.set_requested_by(patron)
        
        if library_item.get_location() == "ON_SHELF":
            library_item.set_location("ON_HOLD_SHELF")

        
        return "request successful"
    

    def pay_fine(self, patron_id, amount):

        patron = self.lookup_patron_from_id(patron_id)

        if patron is None:
            return "patron not found"
        
        patron.amend_fine(-amount)
        return "payment successful"
    

    def increment_current_date(self):

        self.current_date += 1

        for patron in self.members.values():
            for item in patron.get_checked_out_items():

                due_date = item.get_date_checked_out() + item.get_check_out_length()

                if self.current_date > due_date:
                    patron.amend_fine(0.10)



     