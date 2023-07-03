import time
import copy
from MerkleTree import buildMerkleTree
from utils import calculate_hash
from Transaction import ADD_PROPERTY, PROPERTY_EXCHANGE

class Block:
  """
    block parameters
    blockCount: serial number of blocks mined
    transactions: transactions stored in a block
    lastHash: hash of the previous block in the blockchain
    timestamp: time of creation of the block
    miner: validator who mined the block
    """

  def __init__(self, transactions, lastHash, miner, blockCount):
    self.blockCount = blockCount
    self.transactions = transactions
    self.merkleRoot = buildMerkleTree(transactions)
    self.lastHash = lastHash
    self.timestamp = time.time()
    self.currentHash = self.current_hash()
    self.miner = miner

  """
    Genesis block details
    timestamp = 0. Time of creation of blockchain.
    returns genesis block
    """
 #genesis block
  @staticmethod
  def genesis():
    genesisBlock = Block([], 'genesisHash', 'genesis', 0)
    genesisBlock.timestamp = 0
    return genesisBlock

  def current_hash(self):
    if self.merkleRoot == None:
      merkle_hash = ""
    else:
      merkle_hash = self.merkleRoot.val
    return calculate_hash(self.lastHash + merkle_hash + str(self.timestamp))

  def list_property_transactions(self, property, accountModel):
    # execute transactions in the block related to property
    for transaction in self.transactions:
      if transaction.property == property:
        transaction.printPropertyTransaction(accountModel)

  """
    returns the data of the block in json format
    """
  def toJson(self):
    data = {}
    data['blockCount'] = self.blockCount
    data['lastHash'] = self.lastHash
    data['currentHash'] = self.currentHash
    data['miner'] = self.miner
    data['timestamp'] = self.timestamp
    jsonTransactions = []
    for transaction in self.transactions:
      jsonTransactions.append(transaction.toJson())
    data['transactions'] = jsonTransactions
    return data

  def print(self):
    print(self.payload())

  def payload(self):
    jsonRepresentation = copy.deepcopy(self.toJson())
    return jsonRepresentation
