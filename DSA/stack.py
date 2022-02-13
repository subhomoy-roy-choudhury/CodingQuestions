class Node:
  def __init__(self,data):
    self.data = data  
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.buttom = None  
    self.length = 0
  def push(self,value):
    newNode = Node(value)
    ptr = self.top
    if ptr == None :
      self.top = newNode
      self.bottom = newNode
    else :
      self.top = newNode
      self.top.next = ptr 
    return self.peek()
  def pop(self):
    ptr = self.top 
    self.top = ptr.next
    print(ptr.data)
    return self.peek()

  def peek(self):
    ptr = self.top
    arr = []
    while(ptr!=None):
      arr.append(ptr.data)
      ptr = ptr.next
    return arr

if __name__ == '__main__':

    stack = Stack()
    print(stack.push(10))
    print(stack.push(5))
    print(stack.push(3))
    print(stack.pop())
    print(stack.pop())