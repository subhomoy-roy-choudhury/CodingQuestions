class Graph:
  def __init__(self):
    self.no = 0
    self.adjacentList = {}
  def addVertex(self,node):
    self.adjacentList[node] = []
    return self.showConnections()
  def addEdge(self,node1,node2):
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)
    return self.showConnections()
  def showConnections(self):
    for key,val in self.adjacentList.items() :
      print(f'{key} --> {val}')

if __name__ == '__main__':
  graph = Graph()
  print(graph.addVertex('5'))
  print(graph.addVertex('6'))
  print(graph.addVertex('7'))
  print(graph.addEdge('5','6'))
  print(graph.addEdge('6','7'))
  print(graph.addEdge('5','7'))