class Node:
  def __init__(self,data):
    self.node = data
    self.next = None
class Linkedlist:
  def __init__(self):
    self.head = None
  def insertion_end(self,data):
    new_node = Node(data)
    curr = self.head
    if self.head == None:
      self.head = new_node 
    else:
       while curr.next != None:
        curr = curr.next
       curr.next = new_node
  def sort(self):
    cnt0,cnt1,cnt2 = 0,0,0
    curr = self.head
    while curr:
      if curr.node == 0:
        cnt0 += 1
      elif curr.node == 1:
        cnt1 += 1
      else:
        cnt2 += 1
      curr = curr.next
    curr = self.head
    while cnt0 > 0:
      curr.node = 0
      curr = curr.next
      cnt0 -= 1
    while cnt1 > 0:
      curr.node = 1
      curr = curr.next
      cnt1 -= 1
    while cnt2 > 0:
      curr.node = 2
      curr = curr.next
      cnt2 -= 1

    
  def traversal(self):
    curr = self.head
    while curr:
      print(curr.node,end = ' ')
      curr = curr.next
    print('\n')
ll = Linkedlist()
ll.insertion_end(1)
ll.insertion_end(0)
ll.insertion_end(2)
ll.insertion_end(2)
ll.insertion_end(1)
ll.insertion_end(0)
ll.insertion_end(0)
ll.insertion_end(2)
ll.traversal()
ll.sort()
ll.traversal()