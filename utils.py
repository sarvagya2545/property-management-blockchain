from Crypto.Hash import SHA256
import math
import hashlib

def calculate_hash(data: bytes) -> str:
  bytes_data = bytearray(data, "utf-8")
  h = SHA256.new()
  h.update(bytes_data)
  return h.hexdigest()