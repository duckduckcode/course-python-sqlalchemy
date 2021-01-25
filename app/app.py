import sys
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
DATABASE
"""
# connect the sqlalchemy database engine
db_engine = create_engine('sqlite:///database.db')

# test the connection by getting the table names
db_tables = db_engine.table_names()
print('tables:', db_tables)

# create a configured "Session" class
Session = sessionmaker(bind=db_engine)
session = Session()

"""
CLASSES
"""

# declarative base class
Base = declarative_base()

# Product class for the products table
class Product(Base):
  __tablename__ = 'products'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  description = Column(String)
  price = Column(Float)
  stock = Column(Integer)

  def __repr__(self):
    return "<Product(id='%d', name='%s')>" % (self.id, self.name)

"""
FUNCTIONS
"""
def list_all_products():
  print()
  print('All products:')

  products = session.query(Product).all()

  for product in products:
    print(product)

  print()
  input('Press Enter to return to menu...')


def search_for_product():
  print()
  search_term = input('Please enter a search term: ')
  
  search_filter = Product.name.like('%'+search_term+'%')
  products = session.query(Product).filter(search_filter).all()

  print()
  print('Matching products:')

  for product in products:
    print(product)
  
  print()
  input('Press Enter to return to menu...')

def add_new_product():
  print()
  print('Add a new product:')

  new_name = input('What is the product name? ')
  new_description = input('What is the description? ')
  new_price = input('What is the price per unit? ')
  new_stock = input('What is the current number in stock? ')
  
  new_product = Product(
    name = new_name,
    description = new_description,
    price = new_price,
    stock = new_stock
  )

  session.add(new_product)
  session.commit()

  print()
  print('Added new product:')
  
  message = f'{new_product.name} ${new_product.price}'
  print(message)

  print()
  input('Press Enter to return to menu...')


def delete_product():
  print()
  print('Delete product:')

  products = session.query(Product).all()

  for product in products:
    print(product)

  user_input = input('Enter the ID of the product you want to delete: ')
  product_id = int(user_input)

  product = session.query(Product).filter_by(id = product_id).one()
  session.delete(product)
  session.commit()

  print()
  print('Deleted product:')

  message = f'{product.name}'
  print(message)

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