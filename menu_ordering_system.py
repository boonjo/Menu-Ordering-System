#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
menu_ordering_system.py: Evive engineering take home assessment dealing with a menu ordering system.
"""
__author__ = "Joonbo Shim"
__email__= "joonbo@gmail.com"

# Standard Python Library
from collections import Counter

# Global lists for menu items
BREAKFAST = ["Eggs", "Toast", "Coffee"] 
LUNCH = ["Sandwich", "Chips", "Soda"]
DINNER = ["Steak", "Potatoes", "Wine", "Cake"]

class Breakfast:
    """
    A class used to represent breakfast orders

    ...

    Attributes
    ----------
    main : str
        String to represent that there was an order for main dish
    side : str
        String to represent that there was an order for side dish
    drink : str
        String to represent that there was an order for a drink or water
    """
        
    def __init__(self, main, side, drink):
        self.main = main
        self.side = side
        self.drink = drink
        
    def __str__(self):
        # If no drink is ordered, add water
        if self.drink == "Water":
            return f"{BREAKFAST[0]}, {BREAKFAST[1]}, {self.drink}"
        
        # Multiple cups of coffee can be ordered; indicate the number of drinks
        elif self.drink > 1:
            return f"{BREAKFAST[0]}, {BREAKFAST[1]}, {BREAKFAST[2]}({self.drink})"
        
        # Return items in the following order: meal, side, drink
        return f"{BREAKFAST[0]}, {BREAKFAST[1]}, {BREAKFAST[2]}"
    
class Lunch:
    """
    A class used to represent lunch orders

    ...

    Attributes
    ----------
    main : str
        String to represent that there was an order for main dish
    side : str
        String to represent that there was an order for side dish
    drink : str
        String to represent that there was an order for a drink and/or water
    """
    
    def __init__(self, main, side, drink):
        self.main = main
        self.side = side
        self.drink = drink
        
    def __str__(self):
        # If no drink is ordered, add water
        # and if multiple sides are ordered, indicate the number of sides
        if self.drink == "Water" and self.side > 1:
            return f"{LUNCH[0]}, {LUNCH[1]}({self.side}), {self.drink}"
        
        # If no drink is ordered, add water
        elif self.drink == "Water":
            return f"{LUNCH[0]}, {LUNCH[1]}, {self.drink}"
        
        # If multiple sides are ordered, indicate the number of sides
        elif self.side > 1:
            return f"{LUNCH[0]}, {LUNCH[1]}({self.side}), {LUNCH[2]}"
        
        # Return items in the following order: meal, side, drink
        return f"{LUNCH[0]}, {LUNCH[1]}, {LUNCH[2]}"
    
class Dinner:
    """
    A class used to represent dinner orders

    ...

    Attributes
    ----------
    main : str
        String to represent that there was an order for main dish
    side : str
        String to represent that there was an order for side dish
    drink : str
        String to represent that there was an order for a drink and/or water
    dessert : str
        String to represent that there was an order for a dessert
    """
    
    def __init__(self, main, side, drink, dessert):
        self.main = main
        self.side = side
        self.drink = drink
        self.dessert = dessert
    
    def __str__(self):
        # If no drink is ordered, add water
        if self.drink == 0:
            return f"{DINNER[0]}, {DINNER[1]}, Water, {DINNER[3]}"
        
        # Return items in the following order: meal, side, drink, Water, dessert
        return f"{DINNER[0]}, {DINNER[1]}, {DINNER[2]}, Water, {DINNER[3]}"

def findDuplicates(x):
    """
    Returns duplicate items in given string of numbers

    Parameters
    ----------
    x : str
        String of numbers

    Returns
    -------
    list
        List of duplicate strings that are in x
    """
    
    dups = []
    for key,val in Counter(x).items():
        if (val > 1):
            dups.append(key)
    return dups

def checkMissing(order):
    """
    Returns an error message is there is a invalid missing menu item. 
    Returns 0 if all items are valid. 

    Parameters
    ----------
    order : str
        String of numbers that represent the order

    Returns
    -------
    Literal
        String of error message if missing item is detected. Else, returns 0
    """
    
    if '1' not in order and '2' not in order:
        return "Unable to process: Main is missing, Side is missing"
    elif '1' not in order:
        return "Unable to process: Main is missing"
    elif '2' not in order:
        return "Unable to process: Side is missing"
    return 0

def findMenu(order):
    """
    Detects whether order is for breakfast, lunch, or dinner and checks the validity of the order.
    Then, returns the appropriate names for the items that were ordered.

    Parameters
    ----------
    order : str
        An order consisting of a meal and collection of comma separated item Ids.

    Returns
    -------
    class
        returns the appropriate meal or an error message regarding the order.
    """
    
    if 'Breakfast' in order:
        # Isolate the numbers
        order = order.replace('Breakfast', '')
        order = order.replace(',', '')
        order = order.replace(' ', '')

        
        # Check if order doesn't contains main or side
        missing = checkMissing(order)
        if missing != 0:
            return missing
        
        # Check for multiple items
        # At breakfast, only multiple cups of coffee can be ordered
        dups = findDuplicates(order)
        if '1' and '2' in dups:
            return "Unable to process: Eggs and Toast cannot be ordered more than once"
        elif '1' in dups:
            return "Unable to process: Eggs cannot be ordered more than once"
        elif '2' in dups:
            return "Unable to process: Toast cannot be ordered more than once"        
        
        main = 1
        side = 1
        drink = len(order) - 2
        # If no drink is ordered, return water
        if '3' not in order:
            drink = 'Water'
        bOrder = str(Breakfast(main, side, drink))
        return bOrder
    
    elif 'Lunch' in order:
        # Isolate the numbers
        order = order.replace('Lunch', '')
        order = order.replace(',', '')
        order = order.replace(' ', '')
        
        # Check if order doesn't contains main or side
        missing = checkMissing(order)
        if missing != 0:
            return missing
        
        # Check for multiple items
        # At lunch, only multiple sides can be ordered
        dups = findDuplicates(order)
        if '1' and '3' in dups:
            return "Unable to process: Sandwich and Soda cannot be ordered more than once"
        elif '1' in dups:
            return "Unable to process: Sandwich cannot be ordered more than once"
        elif '3' in dups:
            return "Unable to process: Soda cannot be ordered more than once"        
        
        main = 1
        side = len(order) - 2
        drink = 1
        # If no drink is ordered, return water
        if '3' not in order:
            drink = 'Water'
            side = len(order) - 1
        
        lOrder = str(Lunch(main, side, drink))
        return lOrder
    
    elif 'Dinner' in order:
        # Isolate the numbers
        order = order.replace('Dinner', '')
        order = order.replace(',', '')
        order = order.replace(' ', '')
        
        # Check if order doesn't contains main, side, or dessert
        missing = checkMissing(order)
        if missing != 0:                        
            if '4' not in order and '1' not in order and '2' not in order:
                return "Unable to process: Main is missing, Side is missing, Dessert is missing"
            elif '4' not in order and '1' not in order:
                return "Unable to process: Main is missing, Dessert is missing"
            elif '4' not in order and '2' not in order:
                return "Unable to process: Side is missing, Dessert is missing"
            elif '4' not in order:
                return "Unable to process: Dessert is missing"
            return missing
        if '4' not in order:
            return "Unable to process: Dessert is missing"
        
        # Check for multiple items
        # No multiples can be ordered
        dups = findDuplicates(order)
        if len(dups) == 4:
            return "Unable to process: Steak, Potatoes, Wine, and Cake cannot be ordered more than once"
        if len(dups) == 3 and '1' and '2' and '3' in dups:
            return "Unable to process: Steak, Potatoes, and Wine cannot be ordered more than once"
        if len(dups) == 3 and '1' and '2' and '4' in dups:
            return "Unable to process: Steak, Potatoes, and Cake cannot be ordered more than once"
        if len(dups) == 3 and '2' and '3' and '4' in dups:
            return "Unable to process: Potatoes, Wine, and Cake cannot be ordered more than once"
        if len(dups) == 2 and '1' and '2' in dups:
            return "Unable to process: Steak and Potatoes cannot be ordered more than once"
        if len(dups) == 2 and '1' and '3' in dups:
            return "Unable to process: Steak and Wine cannot be ordered more than once"
        if len(dups) == 2 and '1' and '4' in dups:
            return "Unable to process: Steak and Cake cannot be ordered more than once"
        if len(dups) == 2 and '2' and '3' in dups:
            return "Unable to process: Potatoes and Wine cannot be ordered more than once"
        if len(dups) == 2 and '2' and '4' in dups:
            return "Unable to process: Potatoes and Cake cannot be ordered more than once"
        if len(dups) == 2 and '3' and '4' in dups:
            return "Unable to process: Wine and Cake cannot be ordered more than once"
        if '1' in dups:
            return "Unable to process: Steak cannot be ordered more than once"
        if '2' in dups:
            return "Unable to process: Potatoes cannot be ordered more than once"
        if '3' in dups:
            return "Unable to process: Wine cannot be ordered more than once"  
        if '4' in dups:
            return "Unable to process: Cake cannot be ordered more than once"
        
        main = 1
        side = 1
        drink = 1
        dessert = 1
        if '3' not in order:
            drink = 0
        
        dOrder = str(Dinner(main, side, drink, dessert))
        return dOrder