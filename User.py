from Crypto.PublicKey import RSA

class User:
  def __init__(self, username):
    self.username = username
    self.keyPair = RSA.generate(2048)

  def publicKeyString(self):
    publicKeyString = self.keyPair.publickey().exportKey('OpenSSH').decode('utf-8')
    return publicKeyString