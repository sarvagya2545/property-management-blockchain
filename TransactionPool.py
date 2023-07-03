# limit on the number of transactions that are held in the transaction pool
TRANSACTION_POOL_LIMIT = 6


class TransactionPool:
  """
    set of transactions that have not been mined but have been validated by a miner
    """

  def __init__(self):
    self.transactions = []

  def addTransaction(self, transaction):
    self.transactions.append(transaction)

  def transactionExists(self, transaction):
    for poolTransaction in self.transactions:
      if poolTransaction.equals(transaction):
        return True
    return False

  def removeFromPool(self, transactions):
    newPoolTransactions = []
    for poolTransaction in self.transactions:
      insert = True
      for transaction in transactions:
        if poolTransaction.equals(transaction):
          insert = False
      if insert == True:
        newPoolTransactions.append(poolTransaction)
    self.transactions = newPoolTransactions

  def listPropertyTransactions(self, property, accountModel):
    for transaction in self.transactions:
      if transaction.property == property:
        transaction.printPropertyTransaction(accountModel)

  def getTransactions(self):
    return self.transactions

  def print(self):
    for transaction in self.transactions:
      transaction.print()
  
  def miningRequired(self):
    return len(self.transactions) >= TRANSACTION_POOL_LIMIT