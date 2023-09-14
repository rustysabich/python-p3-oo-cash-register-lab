#!/usr/bin/env python3

class CashRegister:
  
  # initialize variables
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    
  # add add_item() method
  def add_item(self, title, price, quantity=1):
    # add items to the list
    for i in range(quantity):
      self.items.append(title)
    # increase the total
    self.total += price * quantity
    
  # add apply_discount() method
  def apply_discount(self):
    if self.discount > 0:
      self.total -= (self.discount /100) * self.total
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    
  # void_last_transaction() method
  def void_last_transaction(self):
    pass
