import sys
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
DATABASE
"""

# SQL CONNECTION goes here

"""
CLASSES
"""

# base class for all table-related classes
Base = declarative_base()

# PRODUCT CLASS goes here

"""
FUNCTIONS
"""
def list_all_products():
  print()
  print('All products:')

  # LIST ALL code goes here

  print()
  input('Press Enter to return to menu...')


def search_for_product():
  print()
  search_term = input('Please enter a search term: ')
  
  # SEARCH code goes here
  
  print()
  input('Press Enter to return to menu...')

def add_new_product():
  print()
  print('Add a new product:')

  # NEW PRODUCT code goes here

  print()
  input('Press Enter to return to menu...')

def delete_product():
  print()
  print('Delete product:')

  # DELETE code goes here

  print()
  input('Press Enter to return to menu...')

"""
MAIN MENU
"""

print('Hello! Welcome to the Cake Shop!')

while True:
  print()
  print('What would you like to do?')
  print('1. List all products')
  print('2. Search for a product')
  print('3. Add a new product')
  print('4. Delete product')
  print('5. Quit')
  print()

  user_choice = input('Please enter a number: ')

  if user_choice == '1':
    list_all_products()
  elif user_choice == '2':
    search_for_product()
  elif user_choice == '3':
    add_new_product()
  elif user_choice == '4':
    delete_product()
  elif user_choice == '5':
    print()
    print('Goodbye!')
    sys.exit(0)
  else:
    print()
    print('Sorry that is not a valid number')