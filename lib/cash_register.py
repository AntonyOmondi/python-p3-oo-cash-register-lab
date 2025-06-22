#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self._items = []
    self._last_transaction = {"titles": [], "price": 0}

  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self._last_transaction["price"] = price * quantity
    self._last_transaction["titles"] = [title] * quantity
    for _ in range(quantity):
      self._items.append(title)

  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * (self.discount/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  @property
  def items(self):
    return self._items

  def void_last_transaction(self):
    self.total -= self._last_transaction["price"]
    for _ in self._last_transaction["titles"]:
      if self._items:
        self._items.pop()
    self._last_transaction = {"titles": [], "price": 0}

  



cash_register = CashRegister()
cash_register_with_discount = CashRegister(20)