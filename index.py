class AdjacencyMatrix:

  def __init__(self, cities):
    self.graph = []
    self.cities = cities
    for i in range(len(cities)):
      self.graph.append([0] * len(cities))

  def printGraph(self):
    print("   ", end="")
    for i in range(len(self.graph)):
      print(self.cities[i], end="   ")
    print()
    for i in range(len(self.graph)):
      print(str(self.cities[i]) + ": ", self.graph[i])
    print()

  #O(1)
  def addEdge(self, i, j):
    self.graph[i][j] = 1
    self.graph[j][i] = 1

  #O(1)
  def deleteEdge(self, i, j):
    self.graph[i][j] = 0
    self.graph[j][i] = 0

  


class Drivers:
  def __init__(self):
    self.drivers = {}

  #ids initialized by 0 to avoid errors when using the max function
  def addDriver(self,name,city):
    if C.searchCity(city):
      ids=[0]
      #concatinating the list with the keys
      ids = ids + list(self.drivers.keys())
      id=max(ids)+1
      self.drivers[id]=[name,city]
    else:
      C.addEdge(city,None)

  def printDrivers(self):
    for k,v in self.drivers.items():
      print(f"{k} , {v[0]} , {v[1]}")

  def printDriversOfCity(self,city):
    for k,v in self.drivers.items():
      if v[1] == city:
        print("v[1] ,")
  

#class Cities:# using adjacency list
# class AdjacencyList:
  # def __init__(self,V):
  #   self.cities=[]
  #   for i in range(V):
  #     self.graph.append()

  # def addEdge(self):
  #   #O(V)
  #   if self.graph[i].search(j):
  #     return None
  #   else:
  #     self.graph[i].addToHead(j)
  # #O(V)
  # def deleteEdge(self,i,j):
  #   self.graph[i].removeNode(j)

  # def printGraph(self):
  #   for i in range(len(self.graph)):
  #     print(i,end=": ")
  #     self.graph[i].printLL()
  
  # def searchCity(self,city):
  #   for i in range(len(self.graph)):
  #     if i == city:
  #       return True
  #   return False
  
  # def printNeighboringCities(self,city):
  #   for i in range(len(self.graph)):
  #     if i == city:
  #       i.printLL()


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

def driversMenu():
  i = int(input("1. To view all the drivers\n2. To add a driver\n3. To go back to main menu\n"))
  if i==1:
    D.printDrivers()
  elif i==2:
    name = input("Enter the name of the driver:")
    city = input("Enter the name of his starting city:")
    D.addDriver(name,city)
  elif i==3:
    startMenu()
  else:
    driversMenu()

  


def citiesMenu():
  i = int(input("1. Show cities\n2. Print neighboring cities\n3. Print Drivers delivering to city\n"))
  if i==1:
    C.printGraph()
  elif i==2:
    city=input("Enter a city name:")
    if C.searchCity(city):
      C.printNeighboringCities(city)
    else:
      print("This city dose not exist")
  elif i==3:
    city=input("Enter a city name:")
    if C.searchCity(city):
      D.printDriversOfCity(city)
    else:
      print("This city dose not exist")
  else:
    startMenu()

  
# C = Cities(100)
# D = Drivers()

# C.addEdge("beirut","tyre")
# C.addEdge("akkar","beirut")


# D=Drivers()
# D.addDriver("hiba","beirut")
# D.addDriver("mohammad","akkar")
# D.addDriver("Ali","tyre")
# D.addDriver("sami","beirut")
# D.printDrivers()

# startMenu()

m=AdjacencyMatrix(["Beirut","Saida","Tyre"])
#m.printGraph()
m.addEdge(0,1)
m.addEdge(1,2)
m.printGraph()