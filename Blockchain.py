from Block import Block

class Blockchain: 
  def __init__(self):
    self.blocks = [Block.genesis()]

  def getLastBlockHash(self):
    return self.blocks[len(self.blocks) - 1].currentHash

  def getBlockCount(self):
    return len(self.blocks)
    
  def addBlock(self, block):
    """
    appends block to the chain 
    """
    self.blocks.append(block)

  def print(self):
    for block in self.blocks:
      block.print()

  def listPropertyTransactions(self, property, accountModel):
    # execute all the blocks and find the transactions with property exchanged
    for block in self.blocks:
      block.list_property_transactions(property, accountModel)