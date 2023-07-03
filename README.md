Group 7 - Proof of Stake
Sarvagya Sharma     2019A7PS0037H
Kshitij Nayyar      2019A8PS0420H
Nikhil Sachdeva     2019B5A71079H
Vartika Gupta       2019B3A70729H

Operation:
AccountModel.py: To add new users, Deposit, withdraw money from their accounts, functions are implemented along with showing account details.

User.py: For each user it's mining address is generated using hashing algo.

Transaction.py: For every transaction (depositing coins to accounts, exachange of property, getting reward for generating block)is done here.

TransactionPool.py: Transactions are added to transaction pool, when a threshold of 6 transaction is reached, merkle tree is generated and block is mined.

Block.py: Every block has block header which contains count of block, merkleRoot, lastHash, timestamp, current hash and miner address. Merkle root is calculated using merkle tree.py.

MerkleTree.py: Every couple of transactions in list are paired and hashed. At every stage of iteration two pairs of hash value are combined until one hash value is left which is merkle root.

PropertyModel.py: Name of property, with it's owner is stored here. Functions are implemented to add property, show properties and change owner. Buying and selling is implemented in transction.py.

Adding a new block to blockchain:
ProofOfStake.py: Stake for each user is stored in list. Function to add stake, clear stake are implemented. Winner is decided randomly and more weight given to whom who has put more stake.

main.py: Main code to call above functions, winner of proof of stake will add the block, if block addtion is required (will checking this in transaction.py) Block is added and linked using blockchain.py. 

Blockchain.py:
Function to link block with previous block

Utils.py
Utility function to calucate SHA256hash













