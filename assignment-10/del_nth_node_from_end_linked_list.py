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

  def remove_nth_node_end(self,k):
    curr = self.head
    cnt = 0
    while curr:
      cnt += 1
      curr = curr.next
    n = cnt - k 
    print(n)
    curr = self.head
    cnt1 = 1
    while cnt1 < n:
      curr = curr.next
      cnt1 += 1
    curr.next = curr.next.next

  def traversal(self):
    curr = self.head
    while curr:
      print(curr.node,end = ' ')
      curr = curr.next
    print('\n')
ll = Linkedlist()
ll.insertion_end(10)
ll.insertion_end(20)
ll.insertion_end(11)
ll.insertion_end(100)
ll.insertion_end(11)
ll.insertion_end(20)
ll.insertion_end(10)
ll.traversal()
ll.remove_nth_node_end(2)
ll.traversal()