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
  def addEdge(self, i, j, weight):
    self.graph[i][j] = weight
    self.graph[j][i] = weight

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


# def citiesMenu():
#   i = int(input("1. Show cities\n2. Print neighboring cities\n3. Print Drivers delivering to city\n"))
  

# def driversMenu():
#   i = int(input("1. To view all the drivers\n2. To add a driver\n3. To go back to main menu\n"))
  
drivers = {"ID0010":["Ali Tarhini","Beirut"],"ID002":["Salim Mhanna","Saida"],"ID003":["Sara jaber","Batroun"]}
C = Cities(500)

  
