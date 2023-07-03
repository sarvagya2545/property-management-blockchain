# This is to add and remove money from accounts
class AccountModel:
  def __init__(self):
    self.names = {}
    self.accounts = []
    self.balances = {}
    
  def addAccount(self, name, publicKeyString):
    if not publicKeyString in self.accounts:
      self.accounts.append(publicKeyString)
      self.names[publicKeyString] = name
      self.balances[publicKeyString] = 0

  def getName(self, publicKeyString):
    if publicKeyString in self.accounts:
      return self.names[publicKeyString]
    return None
      
  # show all accounts    
  def showAccounts(self):
    for account in self.accounts:
      print(f"Name: {self.names[account]}")
      print(f"Account: {account}")
      print(f"Account Balance: {self.balances[account]}")
      print("----------------------")

  def accountExists(self, publicKeyString):
    return publicKeyString in self.accounts

  def getBalance(self, publicKeyString):
    if publicKeyString not in self.accounts:
      self.addAccount(publicKeyString)
    return self.balances[publicKeyString]

  def deposit(self, publicKeyString, amount):
    if publicKeyString not in self.accounts:
      self.addAccount(publicKeyString)
    self.balances[publicKeyString] += amount

  def withdraw(self, publicKeyString, amount):
    if publicKeyString not in self.accounts:
      self.addAccount(publicKeyString)

    if self.balances[publicKeyString] < amount:
      print("Not enough funds to withdraw")
      return False
      
    self.balances[publicKeyString] -= amount
    return True