import random

class ProofOfStake:
  def __init__(self):
    self.stakers = {}

  def add_stake(self, staker_address, stake):
    if staker_address not in self.stakers:
      self.stakers[staker_address] = stake
    else:
      self.stakers[staker_address] += stake

  def get_stake(self, staker_address):
    if staker_address in self.stakers:
      return self.stakers[staker_address]
    return 0

  def clear_stake(self, staker_address):
    if staker_address in self.stakers:
      stake = self.stakers[staker_address]
      self.stakers[staker_address] = 0
      return stake
    return 0

  def next_miner(self):
    staker_list = []
    for staker in self.stakers.keys():
      stake = self.stakers[staker]
      while stake > 0:
        staker_list.append(staker)
        stake -= 1

    if len(staker_list) == 0:
      return 'genesis'

    #winner is decided here
    random_index = random.randint(0, len(staker_list) - 1)
    return staker_list[random_index]

  def printStakes(self, accountModel):
    for staker in self.stakers.keys():
      print(f"Staker: {accountModel.getName(staker)}")
      print(f"Staker Address: {staker}")
      print(f"Stake: {self.stakers[staker]}")
      print("---------------")