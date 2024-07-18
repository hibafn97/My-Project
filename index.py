class Node:

  def __init__(self, info, next):
    self.info = info
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0  #how many nodes are in my LL

  def addToHead(self, info):  #O(1)
    n = Node(info, None)
    if self.size == 0:  # LL is empty, I have no nodes inside
      self.head = n
      self.tail = n
      self.size = 1
    else:
      n.next = self.head
      self.head = n
      self.size += 1

  def addToTail(self, info):  #O(1)
    if self.size == 0:
      self.addToHead(info)
    else:
      n = Node(info, None)
      self.tail.next = n
      self.tail = n
      self.size += 1


  def deleteHead(self):  # O(1)
    if self.size == 0:  # empty
      return None
    elif self.size == 1:
      val = self.head.info
      self.head = None
      self.tail = None
      self.size = 0
      return val
    else:
      val = self.head.info
      self.head = self.head.next
      self.size -= 1
      return val


  def printLL(self):  #O(n), where n is the number of nodes in the list
    i = self.head
    while i != None:
      print(i.info, "->", end="")
      i = i.next
    print()


  def deleteTail(self): #O(n), where n is the length of my LL
    if self.size<=1:
      return self.deleteHead()
    else:
      val=self.tail.info
      #loop to find the element before the last
      i=self.head
      while i.next.next!=None: #I did not reach the node before the last
        i=i.next
      #update the tail and its next
      self.tail=i
      self.tail.next=None
      self.size-=1
      return val

  # remove the node that contains info
  def removeNode(self,info):
    pass
    
  # search for info in LL 
  def search(self,info):
    if self.size==0:
      return False
    current=self.head
    while current!=None:
      if current.info==info:
        return True
      current=current.next
    return False

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

  def printDriversOfCity(self,city):
    for k,v in self.drivers.items():
      if v[1] == city:
        print("v[1] ,")
  

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
      self.graph[i].addToHead(j)
  #O(V)
  def deleteEdge(self,i,j):
    self.graph[i].removeNode(j)

  def printGraph(self):
    for i in range(len(self.graph)):
      print(i,end=": ")
      self.graph[i].printLL()
  
  def searchCity(self,city):
    for i in range(len(self.graph)):
      if i == city:
        return True
    return False
  
  def printNeighboringCities(self,city):
    for i in range(len(self.graph)):
      if i == city:
        i.printLL()


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

  
C = Cities(0)
D = Drivers()

C.addEdge("beirut","tyre")
C.addEdge("akkar","beirut")


D=Drivers()
D.addDriver("hiba","beirut")
D.addDriver("mohammad","akkar")
D.addDriver("Ali","tyre")
D.addDriver("sami","beirut")
D.printDrivers()

startMenu()