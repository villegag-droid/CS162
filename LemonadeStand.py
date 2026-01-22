# Author: Gerardo Villegas
# Github username: villegag-droid
# Date: Oct 22nd, 2025
# Description: 
# This module implements a Lemonade Stand management system with MenuItem and 
# LemonadeStand classes to track inventory, sales, and profits.

class MenuItem:
    """
    Represents a menu item with name, wholesale cost, and selling price.
    Provides getter methods to access item properties.
    """
    
    def __init__(self, item_name, wholesale_cost, selling_price):
        """
        Initialize a MenuItem with name, wholesale cost, and selling price.
        
        Parameters:
            item_name (str): Name of the menu item
            wholesale_cost (float): Cost to acquire the item
            selling_price (float): Price at which the item is sold
        """
        self._item_name = item_name
        self._wholesale_cost = float(wholesale_cost)
        self._selling_price = float(selling_price)

    def get_item_name(self):
        
        return self._item_name

    def get_wholesale_cost(self):
        
        return self._wholesale_cost

    def get_selling_price(self):
        
        return self._selling_price


class DuplicateMenuItemError(Exception):
    """Exception raised when attempting to add a duplicate menu item."""
    pass


class MissingMenuItemError(Exception):
    """Exception raised when attempting to access a non-existent menu item."""
    pass


class LemonadeStand:
    """
    Manages a lemonade stand with menu items, sales tracking, and profit calculations.
    Maintains dictionaries for menu items and their sales records.
    """
    
    def __init__(self, stand_name):
        """
        Initialize a LemonadeStand with a name and empty dictionaries for menu and sales.
        
        Parameters:
            stand_name (str): Name of the lemonade stand
        """
        self._stand_name = stand_name
        # Dictionary mapping item names to MenuItem objects
        self._menu_dictionary = {}
        # Dictionary mapping item names to sales counts
        self._sales_dictionary = {}

    def get_name(self):
        """Return the name of the lemonade stand."""
        return self._stand_name

    def add_menu_item(self, menu_object):
        """
        Add a menu item to the stand's menu and initialize its sales count to 0.
        
        Parameters:
            menu_object (MenuItem): The menu item to add
            
        Raises:
            DuplicateMenuItemError: If the item name already exists in the menu
        """
        item_name = menu_object.get_item_name()
        
        if item_name not in self._menu_dictionary:
            self._menu_dictionary[item_name] = menu_object
            self._sales_dictionary[item_name] = 0
        else:
            raise DuplicateMenuItemError

    def enter_sales(self, menu_str, amount_sold):
        """
        Record sales for a menu item by adding to its sales count.
        
        Parameters:
            menu_object (MenuItem): The menu item being sold
            amount_sold (int): Number of items sold
            
        Raises:
            MissingMenuItemError: If the item is not in the menu
        """
       
        
        
        if menu_str in self._sales_dictionary:
            self._sales_dictionary[menu_str] += amount_sold
        else:
            raise MissingMenuItemError

    def number_of_item_sold(self, menu_item):
        """
        Return the total number of items sold for a given menu item.
        
        Parameters:
            menu_item (MenuItem): The menu item to check sales for
            
        Returns:
            int: Total number of items sold
            
        Raises:
            MissingMenuItemError: If the item is not in the menu
        """
        
        
        if menu_item in self._menu_dictionary:
            return self._sales_dictionary[menu_item]
        else:
            raise MissingMenuItemError

    def profit_margin_for_item(self, menu_item):
        """
        Calculate and return the profit margin for a menu item.
        
        Parameters:
            menu_item (MenuItem): The menu item to calculate profit margin for
            
        Returns:
            float: Profit margin (selling price - wholesale cost)
            
        Raises:
            MissingMenuItemError: If the item is not in the menu
        """
       
        
        if menu_item in self._menu_dictionary:
            item = self._menu_dictionary[menu_item]  
            return (item.get_selling_price() - item.get_wholesale_cost())
        else:
            raise MissingMenuItemError

    def total_profit_for_stand(self):
        """
        Calculate and return the total profit for the entire stand.
        
        Returns:
            float: Total profit from all items sold
        """
        profit = 0
        # Calculate profit for each item and sum them
        for item_name in self._menu_dictionary:  
            profit += (self.number_of_item_sold(item_name) * self.profit_margin_for_item(item_name))
        return profit




if __name__ == "__main__":
    try:
        stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
        item_1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
        stand.add_menu_item(item_1)  # Add lemonade to the menu for 'Lemons R Us'
        item_2 = MenuItem('egg tart', 0.8, 1.7)  # Create egg tart as a menu item (wholesale cost 80 cents, selling price $1.70)
        stand.add_menu_item(item_2)  # Add egg tart to the menu for 'Lemons R Us'
        item_3 = MenuItem('lokum', 0.2, 0.8)  # Create lokum as a menu item (wholesale cost 20 cents, selling price 80 cents)
        stand.add_menu_item(item_3)  # Add lokum to the menu for 'Lemons R Us'

        stand.enter_sales('lemonade', 18)
        stand.enter_sales('egg tart', 11)
        stand.enter_sales('Jimmy Johns', 9)

        num_lemonades_sold = stand.number_of_item_sold('lemonade')
        print(f"total profit = {stand.total_profit_for_stand()}")  # print the total profit so far
    except MissingMenuItemError:
        print("Menu item not found correct values")


