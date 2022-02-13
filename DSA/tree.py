class Node:
  def _init__(self,data):
    self.data = data
    self.left = None
    self.right = None
  
class Tree:
  def __init__(self):
    self.root = None
  def insert(self,value):
    if self.root is None:
      newNode = Node(value)
      self.root = newNode
    else :
      currentNode = self.root
      if value > currentNode.data:
        if currentNode.right is None :
          currentNode.right = newNode
        else :
          currentNode = currentNode.right
      else :
        if currentNode.left is None :
          currentNode.left = newNode
        else :
          currentNode = currentNode.left