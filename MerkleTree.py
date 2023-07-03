from utils import calculate_hash

class Node:
  def __init__(self, val: int, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def buildMerkleTree(node_data: [str]) -> None:
  node_list = [Node(node_str) for node_str in node_data ]
  new_node_list = []

  if len(node_list) == 0:
    return None
  
  while len(node_list) != 1:
    # duplicate last node if odd number of nodes
    if len(node_list) % 2 != 0:
      node_list.append(node_list[-1])

    # combine nodes in pairs of 2 and create a new list
    for j in range(0, len(node_list), 2):
      left = node_list[j]
      right = node_list[j + 1]
      new_node = Node(
        val = calculate_hash(f"{left.val}{right.val}"),
        left = left,
        right = right
      )
      new_node_list.append(new_node)

    node_list = new_node_list
    new_node_list = []

  # returns the merkle root
  return node_list[0]

