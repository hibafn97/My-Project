class Drivers:
  def __init__(self):
    self.drivers = {}

  def addDriver(self,name,city):
    ids=[0]
    ids = ids + list(self.drivers.keys())
    id=max(ids)+1
    self.drivers[id]=[name,city]

  def printDrivers(self):
    for k,v in self.drivers.items():
      print(f"{k} , {v[0]} , {v[1]}")
  

class Cities:# using adjacency matrix

  def __init__(self, V):
    self.graph = []
    for i in range(V):
      self.graph.append([0] * V)

  def printGraph(self):
    print("   ", end="")
    for i in range(len(self.graph)):
      print(i, end="   ")
    print()
    for i in range(len(self.graph)):
      print(str(i) + ": ", self.graph[i])
    print()

  #O(1)
  def addEdge(self, i, j):
    self.graph[i][j] = 1
    self.graph[j][i] = 1

  #O(1)
  def deleteEdge(self, i, j):
    self.graph[i][j] = 0
    self.graph[j][i] = 0


def startMenu():
  i = int(input("1. To go to the drivers menu\n2. To go to the cities menu\n3. To exit the system\n"))
  if i==1:
    driversMenu()
  elif i==2:
    citiesMenu()
  elif i==3:
    print("Visit us again ^_^")
  else:
    startMenu()



  


def citiesMenu():
  i = int(input("1. Show cities\n2. Print neighboring cities\n3. Print Drivers delivering to city\n"))
  
  
C = Cities(500)
D = Drivers
startMenu()
  
# D=Drivers()
# D.addDriver("hiba","beirut")
# D.addDriver("mohammad","akkar")
# D.addDriver("Ali","tyre")
# D.addDriver("sami","beirut")
# D.printDrivers()