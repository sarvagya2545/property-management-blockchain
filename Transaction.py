 # Transaction types
DEPOSIT = "DEPOSIT"
WITHDRAW = "WITHDRAW"
ADD_STAKE = "ADD_STAKE"
PROPERTY_EXCHANGE = "PROPERTY_EXCHANGE"
GET_REWARD = "GET_REWARD"     
ADD_PROPERTY = "ADD_PROPERTY"

import uuid
import time
import copy

class Transaction:
  def __init__(self, buyerPublicKey, sellerPublicKey, amount, type, property = ""):
    self.buyerPublicKey = buyerPublicKey
    self.sellerPublicKey = sellerPublicKey
    self.amount = amount
    self.type = type
    # money is transferred from sender to reciever
    # but property is transferred from reciever to sender
    self.property = property
    self.id = (uuid.uuid1()).hex
    self.timestamp = time.time()

  def toJson(self):
    return self.__dict__

  def payload(self):
    jsonRepresentation = copy.deepcopy(self.toJson())
    return jsonRepresentation

  def print(self):
    print(self.payload())

  def equals(self, transaction):
    if self.id == transaction.id:
      return True
    else:
      return False

  def printPropertyTransaction(self, accountModel):
    if self.type == ADD_PROPERTY:
      print("PROPERTY LISTED")
      print(f"Owner: {accountModel.getName(self.buyerPublicKey)}")
      print(f"Owner wallet: \n{self.buyerPublicKey}")
      print(f"Time: {self.timestamp}")
      print("-----------------------------")
    elif self.type == PROPERTY_EXCHANGE:
      print("PROPERTY SOLD")
      print(f"Amount: {self.amount}")
      print(f"Buyer: {accountModel.getName(self.buyerPublicKey)}")
      print(f"Buyer wallet: \n{self.buyerPublicKey}")
      print(f"Seller: {accountModel.getName(self.sellerPublicKey)}")
      print(f"Seller wallet: \n{self.sellerPublicKey}")
      print(f"Time: {self.timestamp}")
      print("-----------------------------")


def createTransaction(buyAddress, sellAddress, amt, type, property):
  tx = Transaction(buyAddress, sellAddress, amt, type, property)
  return tx