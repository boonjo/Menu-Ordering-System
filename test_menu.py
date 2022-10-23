#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_menu.py: Tests for menu_ordering_system.py
"""
__author__ = "Joonbo Shim"
__email__= "joonbo@gmail.com"

# Standard Python Library
import unittest

from menu_ordering_system import findMenu

class TestMenuOrdering(unittest.TestCase):
    def test_standard_breakfast(self):
        """
        Tests standard breakfast order
        """
        self.assertEqual("Eggs, Toast, Coffee", findMenu("Breakfast 1,2,3"))
        
    def test_water_breakfast(self):
        """
        Tests standard breakfast without drink order, so just water
        """
        self.assertEqual("Eggs, Toast, Water", findMenu("Breakfast 1,2"))
        
    def test_disorder_breakfast(self):
        """
        Tests standard breakfast with random ordering of numbers
        """
        self.assertEqual("Eggs, Toast, Coffee", findMenu("Breakfast 2,3,1"))
        
    def test_multiple_breakfast(self):
        """
        Tests multiple drinks order for breakfast
        """
        self.assertEqual("Eggs, Toast, Coffee(3)", findMenu("Breakfast 1,2,3,3,3"))
    
    def test_error_multiple_breakfast(self):
        """
        Tests multiple orders for a breakfast item that should be an error
        """
        self.assertEqual("Unable to process: Eggs cannot be ordered more than once", findMenu("Breakfast 1,1,2,3"))
        
    def test_missing_breakfast(self):
        """
        Tests breakfast order with missing item
        """
        self.assertEqual("Unable to process: Side is missing", findMenu("Breakfast 1"))
        
    def test_standard_lunch(self):
        """
        Tests standard lunch order
        """
        self.assertEqual("Sandwich, Chips, Soda", findMenu("Lunch 1,2,3"))
        
    def test_water_lunch(self):
        """
        Tests standard lunch order without a drink, so just water
        """
        self.assertEqual("Sandwich, Chips, Water", findMenu("Lunch 1,2"))
        
    def test_error_multiple_lunch(self):
        """
        Tests lunch order with multiple items that is an error
        """
        self.assertEqual("Unable to process: Sandwich cannot be ordered more than once", findMenu("Lunch 1,1,2,3"))
        
    def test_error_multiples_lunch(self):
        """
        Tests lunch order with several multiple items that is an error
        """
        self.assertEqual("Unable to process: Sandwich and Soda cannot be ordered more than once", findMenu("Lunch 1,1,2,2,3,3"))
    
    def test_multiple_lunch(self):
        """
        Tests multiple side order for lunch
        """
        self.assertEqual("Sandwich, Chips(2), Water", findMenu("Lunch 1,2,2"))
        
    def test_missing_lunch(self):
        """
        Tests missing lunch order that is an error
        """
        self.assertEqual("Unable to process: Main is missing, Side is missing", findMenu("Lunch"))
    
    def test_standard_dinner(self):
        """
        Tets standard dinner order
        """
        self.assertEqual("Steak, Potatoes, Wine, Water, Cake", findMenu("Dinner 1,2,3,4"))
        
    def test_no_wine_dinner(self):
        """
        Tests standard dinner order with no drink, so just water
        """
        self.assertEqual("Steak, Potatoes, Water, Cake", findMenu("Dinner 1,2,4"))
        
    def test_multiple_dinner(self):
        """
        Tests dinner order with multiple items
        """
        self.assertEqual("Unable to process: Cake cannot be ordered more than once", findMenu("Dinner 1,2,3,4,4"))
        
    def test_multiples_dinner(self):
        """
        Tests dinner order with several multiple items
        """
        self.assertEqual("Unable to process: Steak and Cake cannot be ordered more than once", findMenu("Dinner 1,1,2,3,4,4"))
        
    def test_all_multiples_dinner(self):
        """
        Tests dinner order with all items being multiples
        """
        self.assertEqual("Unable to process: Steak, Potatoes, Wine, and Cake cannot be ordered more than once", findMenu("Dinner 1,1,2,2,3,3,4,4"))
        
    def test_missing_dinner(self):
        """
        Tests dinner order with missing item
        """
        self.assertEqual("Unable to process: Dessert is missing", findMenu("Dinner 1,2,3"))
        
    def test_missing_few_dinner(self):
        """
        Tests dinner order with several missing items
        """
        self.assertEqual("Unable to process: Side is missing, Dessert is missing", findMenu("Dinner 1,3"))
        
    def test_missing_all_dinner(self):
        """
        Tests dinner order with all items missing
        """
        self.assertEqual("Unable to process: Main is missing, Side is missing, Dessert is missing", findMenu("Dinner"))


if __name__ == '__main__':
    unittest.main()