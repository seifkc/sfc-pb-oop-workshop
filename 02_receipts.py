"""
You are tasked with developing a system to manage shopping receipts.
The system should allow for adding items to a receipt, calculating subtotals,
and applying tax rates to get the total amount due.
You will need multiple classes in order to accomplish this and one will utilize the other when being invoked.
See example:

receipt = Receipt(.1)
receipt.add_item(ReceiptItem(4, 2.50))
receipt.add_item(ReceiptItem(2, 5.00))

print(receipt.get_subtotal())     # Prints 20
print(receipt.get_total())        # Prints 22


Once your classes are complete, copy and paste the above example below them in order to test their functionality
"""

class ReceiptItem #individual products
   def __init__ (self, quantity, price):
      self.quantity = quantity
      self.price = price
   def get_total(self):
      return f"{self.quantity} * {self.price}"

"""
Write a class that meets these requirements.

Name:       Receipt

Required state:
   * tax rate, the percentage tax that should be applied to the total

Behavior:
   * add_item(item)   # Add a ReceiptItem to the Receipt
   * get_subtotal()   # Returns the total of all of the receipt items
   * get_total()      # Multiplies the subtotal by the 1 + tax rate

"""
class Receipt(ReceiptItem):
   def __init__ (self, tax_rate):
      self.tax_rate = tax_rate
      self.items = [] #emptylist
   def add_item(self, item):
      self.items.append(item) # add each item that to made list above
   def get_subtotal(self):
      return sum(super().get_total() for item in self.items) #referencing get_total in receipt item class for every item added to list reference receipt items and add total
   def get_total(self):
      return self.get_total() * (1 + self.tax_rate)   #one is to keep the cost and tax rate was defined in init above
"""







