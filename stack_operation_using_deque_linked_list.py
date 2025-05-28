## stack operations on list using deque(acts as linked list)

from collections import deque
class stack:
  def __init__(self):
    self.container = deque()
  def push(self,x):
    return self.container.append(x)
  def pop(self):## deletes the last element
    return self.container.pop()
  def peak(self):## returns the last element
    return self.container[-1]
  def isEmpty(self):
    return len(self.container) == 0
  def size(self):
    return len(self.container)
s = stack()
s.push(90)
s.push(90)
s.push(90)
s.peak()
## stack operations on linked list

from io import TextIOWrapper
class Node :
  def __init__(self,val):
    self.data = val
    self.next = None
class stack :
  def __init__(self):
    self.top = None
  def push(self,val):
    newnode = Node(val)
    newnode.next = self.top
    self.top = newnode
  def pop(self):
    if self.top is None:
      raise IndexError("popping from empty list")
    self.top = self.top.next
  def peak(self):
    if self.top is None:
      raise IndexError("peak doesn't exits")
    return self.top.data
  def isempty(self) :
    return self.top is None
  def display(self):
    curr = self.top
    while curr:
      print(curr.data,end = ' ')
      curr = curr.next
    print('\n')
s = stack()
s.push(8)
s.push(10)
s.push(11)
s.pop()
s.pop()
s.pop()
s.push(90)
s.peak()
print(s.isempty())
s.display()