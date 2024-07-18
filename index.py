class Node:

  def __init__(self, info, next):
    self.info = info
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0  #how many element I have in my LL

  def addHead(self, info):  #O(1)
    n = Node(info, None)

    if self.size == 0:  # LL is empty
      self.head = n
      self.tail = n
      self.size += 1
    else:
      n.next = self.head
      self.head = n
      self.size += 1

  def addTail(self, info):  #O(1)
    n = Node(info, None)
    if self.size == 0:  # LL is empty
      self.head = n
      self.tail = n
      self.size += 1
    else:
      self.tail.next = n
      self.tail = n
      self.size += 1

class Drivers:
  def __init__(self):
    self.drivers = {}

  #ids initialized by 0 to avoid errors when using the max function
  def addDriver(self,name,city):
    
    ids=[0]
    #concatinating the list with the keys
    ids = ids + list(self.drivers.keys())
    id=max(ids)+1
    self.drivers[id]=[name,city]

  def printDrivers(self):
    for k,v in self.drivers.items():
      print(f"{k} , {v[0]} , {v[1]}")
  

class Cities:# using adjacency list
# class AdjacencyList:
  def __init__(self,V):
    self.graph=[]
    for i in range(V):
      self.graph.append(LinkedList())

  def addEdge(self,i,j):
    #O(V)
    if self.graph[i].search(j):
      return None
    else:
      self.graph[i].addHead(j)
  #O(V)
  def deleteEdge(self,i,j):
    self.graph[i].removeNode(j)

  def printGraph(self):
    for i in range(len(self.graph)):
      print(i,end=": ")
      self.graph[i].printLL()


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
  
  
C = Cities(500)
D = Drivers
startMenu()
  
# D=Drivers()
# D.addDriver("hiba","beirut")
# D.addDriver("mohammad","akkar")
# D.addDriver("Ali","tyre")
# D.addDriver("sami","beirut")
# D.printDrivers()