class PropertyModel:
  def __init__(self):
    self.property_list = []
    self.property_owner = {}

  """
  add a new property with an owner
  """
  def addProperty(self, owner_address, property):
    if property not in self.property_list:
      self.property_list.append(property)
      self.property_owner[property] = owner_address
      return True
    else:
      print("Property already present in the system")
      return False


  def checkOwnerShip(self, owner_address, property):
    if property not in self.property_list:
      print("Property not present in the system")
      return False

    return self.property_owner[property] == owner_address

  """
  Change owner
  """
  def transferOwnerShip(self, property, owner_to):
    if property in self.property_list:
      self.property_owner[property] = owner_to
      return True
    else:
      print("Property not present in the system")
      return False

  """
  Show all the properties listed
  """
  def showAllProperties(self, accounts):
    for property in self.property_list:
      print(f"Property: {property}")
      print(f"Owner address: {self.property_owner[property]}")
      print(f"Owner name: {accounts.names[self.property_owner[property]]}")
      print("----------------------")
      print("")