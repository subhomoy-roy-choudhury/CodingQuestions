class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0
  def enqueue(self,value):
    newNode = Node(value)
    if self.length == 0 :
      self.first = newNode
      self.last = newNode
    else :
      self.last.next = newNode
      self.last = newNode
    self.length += 1
    return self.peek()

  def dequeue(self):
    if self.first is None :
      return None
    else :
      print(self.first.data)
      self.first = self.first.next
      return self.peek()

  def peek(self):
    ptr = self.first
    arr = []
    while(ptr!=None):
      arr.append(ptr.data)
      ptr = ptr.next
    return arr

if __name__ == '__main__':

  queue = Queue()
  print(queue.enqueue(0))
  print(queue.enqueue(5))
  print(queue.enqueue(10))
  print(queue.dequeue())
  print(queue.dequeue())