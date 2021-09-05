class Graph:
  def __init__(self):
    self.no = 0
    self.adjacentList = []
  def addVertex(self,node):
    self.adjacentList[node] = []
    return self.showConnections()
  def addEdge(self,node1,node2):
    self.adjacentList[node1].push(node2)
    self.adjacentList[node2].push(node1)
    return self.showConnections()
  def showConnections(self):
    for key,val in self.adjacentList :
      print(f'{key} --> {val}')

if __name__ == '__main__':
  graph = Graph()
  print(graph.addVertex('5'))