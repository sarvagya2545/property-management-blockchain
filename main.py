from User import User
from AccountModel import AccountModel
from ProofOfStake import ProofOfStake
from PropertyModel import PropertyModel
from Transaction import createTransaction, ADD_PROPERTY, DEPOSIT, WITHDRAW, ADD_STAKE, PROPERTY_EXCHANGE, GET_REWARD
from TransactionPool import TransactionPool
from Blockchain import Blockchain, Block
# initialize
accountModel = AccountModel()
propertyModel = PropertyModel()
pos = ProofOfStake()
txPool = TransactionPool()
blockchain = Blockchain()

# MINING REWARD
MINING_REWARD = 100

# helper function to add transaction to the txPool and
# mine a new block if required
def addTransaction(transaction):
  txPool.addTransaction(transaction)
  # check if mining a new block is required and mine the new block
  if txPool.miningRequired():
    # mine the block
    print("-----------------")
    print("Mining a new block")
    miner = pos.next_miner()
    transactionsInPool = txPool.getTransactions()
    lastHash = blockchain.getLastBlockHash()
    blockCount = blockchain.getBlockCount()

    print(f"Miner: {accountModel.getName(miner)}")
    print(f"Miner Address: {miner}")
    
    newBlock = Block(transactionsInPool, lastHash, miner, blockCount)
    txPool.removeFromPool(transactionsInPool)
    stake = pos.clear_stake(miner)

    print(f"BLOCK ADDED: {newBlock.payload()}")
    
    # add a new transaction about stake + mining reward
    rewardTx = createTransaction(None, miner, stake + MINING_REWARD, GET_REWARD, "")
    accountModel.deposit(miner, stake + MINING_REWARD)
    txPool.addTransaction(rewardTx)

    # add block
    blockchain.addBlock(newBlock)
    print("Block added")
    print("-----------------")

# main loop
while True:
  print("Welcome!")
  print("Choose action:")
  print("")
  print("0. Show all users")
  print("1. Register a new user")
  print("2. Deposit to wallet")
  print("3. Withdraw from wallet")
  print("4. Stake coins for mining")
  print("5. Buying / Selling of property")
  print("6. Add a property for sale")
  print("7. Show all properties")
  print("8. Get transaction history of a property")
  print("9. Show data")
  print("10. Exit")
  print("")

  try:
    action = int(input("Type in the number of the action: "))
  except ValueError:
    print("Please input a number")
    continue
    
  if action < 0 or action > 10:
    print("Wrong Action number! Try again:")
    
  # handle action
  # print(action)
  if action == 0:
    # show all users
    accountModel.showAccounts()
    
  elif action == 1:
    # Create user
    name = input("Enter the name of the user: ")

    if accountModel.accountExists(name):
      print("Duplicate account")
      continue
    
    new_user = User(name)
    
    print("Mining address of the user is: ")
    print("")

    # generate public key
    pub_key = new_user.publicKeyString()
    print(pub_key)
    print("")

    # add account
    accountModel.addAccount(name, pub_key)
    
  elif action == 2:
    # Deposit to user account
    user_address = input("Enter the address of the user: ")
    if not accountModel.accountExists(user_address):
      print("User account not found. Please try again")
      continue
    amount = int(input("Enter the amount to be deposited: "))
    accountModel.deposit(user_address, amount)

    print(f"Amount successfully added to {user_address}. \nCurrent balance = {accountModel.getBalance(user_address)}")
    addTransaction(createTransaction(None, user_address, amount, DEPOSIT, ""))

  elif action == 3:
    # withdraw from account
    user_address = input("Enter the address of the user: ")
    amount = int(input("Enter the amount to be withdrawn: "))
    if not accountModel.accountExists(user_address):
      print("User account not found. Please try again")
      continue

    if(accountModel.withdraw(user_address, amount) == True):
      addTransaction(createTransaction(user_address, None, amount, WITHDRAW, ""))
      print(f"Amount successfully withdrawn from {user_address}.")
      print(f"Current balance = {accountModel.getBalance(user_address)}")
    
  elif action == 4:
    # Stake coins from user
    user_address = input("Enter the address of the user: ")

    if not accountModel.accountExists(user_address):
      print("User account not found. Please try again")
      continue

    amount = int(input("Enter the amount which you wish to stake: "))
    
    if (accountModel.withdraw(user_address, amount) == False):
      continue

    pos.add_stake(user_address, amount)


    print("Added the amount to stake")
    print(f"Current balance: {accountModel.getBalance(user_address)}")
    print(f"Coins staked for mining: {pos.get_stake(user_address)}")
    
    addTransaction(createTransaction(user_address, None, amount, ADD_STAKE, ""))

  elif action == 5:
    # Buying / Selling of property
    buyer_address = input("Enter the address of the buyer: ")
    seller_address = input("Enter the address of the seller: ")
    property = input("Enter the property which is being sold: ")
    amount = int(input("Enter the amount of money transferred: "))

    if not accountModel.accountExists(buyer_address):
      print("Buyer account does not exist")
      continue

    if not accountModel.accountExists(seller_address):
      print("Seller account does not exist")
      continue

    if accountModel.getBalance(buyer_address) >= amount:
      if propertyModel.checkOwnerShip(seller_address, property):
        propertyModel.transferOwnerShip(property, buyer_address)
        accountModel.withdraw(buyer_address, amount)
        accountModel.deposit(seller_address, amount)

        print("Transaction completed")
        addTransaction(createTransaction(buyer_address, seller_address, amount, PROPERTY_EXCHANGE, property))
        continue
      else:
        print("Property not owned by the buyer!")

    print("Error in transaction!")
      
  elif action == 6:
    # List property
    property = input("Enter the property: ")
    owner_address = input("Enter the name of the person who owns this property: ")

    if not accountModel.accountExists(owner_address):
      print("User account does not exist")
      continue

    if propertyModel.addProperty(owner_address, property):
      print("Property added for sale")
      addTransaction(createTransaction(owner_address, None, 0, ADD_PROPERTY, property))

  elif action == 7:
    # Show all properties listed
    propertyModel.showAllProperties(accountModel)

  elif action == 8:
    # get transaction history of a property
    property = input("Enter the name of the property: ")

    # show transaction history
    blockchain.listPropertyTransactions(property, accountModel)
    txPool.listPropertyTransactions(property, accountModel)
  elif action == 9:
    # show all the data
    print("--------- ACCOUNT MODEL ----------\n")
    accountModel.showAccounts()
    print("\n--------- /ACCOUNT MODEL ----------\n")

    print("\n--------- STAKES ---------\n")
    pos.printStakes(accountModel)
    print("\n--------- /STAKES ---------\n")

    print("--------- PROPERTY MODEL ----------\n")
    propertyModel.showAllProperties(accountModel)
    print("--------- /PROPERTY MODEL ----------\n")

    print("\n--------- BLOCKCHAIN ---------\n")
    blockchain.print()
    print("\n--------- /BLOCKCHAIN ---------\n")

    print("\n--------- TRANSACTION POOL ---------\n")
    txPool.print()
    print("\n--------- /TRANSACTION POOL ---------\n")
  elif action == 10:
    break
  else:
    print("Invalid action")