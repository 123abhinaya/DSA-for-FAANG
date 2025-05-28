class Node:
  def __init__(self,data):
    self.node = data
    self.next = None
class Linkedlist:
  def __init__(self):
    self.head = None


  def insertion_beg(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node



  def insertion_at_index(self,data,k):
    new_node = Node(data)
    if k == 0:
      new_node.next = self.head
      self.head = new_node
    else:
      curr = self.head
      cnt = 0
      while(cnt < k-1 and curr):
        curr = curr.next
        cnt += 1
      new_node.next = curr.next
      curr.next = new_node



  def insertion_end(self,data):
    new_node = Node(data)
    curr = self.head
    while curr.next != None:
      curr = curr.next
    curr.next = new_node



  def delete_beg(self):
    if self.head == None:
      print("no ele to remove")
      return
    curr = self.head
    self.head = self.head.next



  def delete_index(self,x):
    curr = self.head
    if x == 0:
      self.delete_beg()
      return
    elif self.head is None:
      return
    else:
      cnt = 0
      while(cnt < x-1 and curr):
        curr = curr.next
        cnt += 1
      if curr.next == None:
        print("list index out of bound")
        return
      curr.next = curr.next.next


  def reversal(self):## my method
    x = self.head
    t = None
    while(x.next and x.next.next):
      y = x.next.next
      x.next.next = x
      k = x.next
      x.next = t
      x = y
      t = k
    else:
      k = x.next
      k.next = x
      x.next = t
    self.head = k
  def reversal1(self):### mam's method
    prev = None
    curr = self.head
    while curr:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    self.head = prev
  def search(self,x):
    curr = self.head
    while curr:
      if curr.node == x:
        return True
      curr = curr.next
    return False
  def merge(x,y):
    curr = x
    while curr.next != None:
      curr = curr.next

  def traversal(self):
    curr = self.head
    while curr:
      print(curr.node,end = " ")
      curr = curr.next
    print('\n')




ll = Linkedlist()
ll.insertion_beg(10)
ll.insertion_beg(46)
ll.insertion_beg(45)
ll.insertion_beg(89)
ll.insertion_beg(71)
ll.insertion_beg(87)
ll.traversal()
ll.reversal1()
ll.traversal()