## tree traversals using recurrsions
from collections import deque
class Node :
  def __init__(self,x):
    self.data = x
    self.left = None
    self.right = None
class Traversal:
  def __init__(self):
    self.stk = deque()
  def preorder(self,root):
    if root:
      print(root.data,end = " ")
      self.preorder(root.left)
      self.preorder(root.right)
  def inorder(self,root):
    if root:
      self.inorder(root.left)
      print(root.data,end = " ")
      self.inorder(root.right)
  def postorder(self,root):
    if root:
      self.inorder(root.left)
      self.inorder(root.right)
      print(root.data,end=" ")
t = Traversal()
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(67)
t.preorder(root)
print("\n")
t.inorder(root)
print("\n")
t.postorder(root)
#------------------------------------
## tree traversals using iteration
from collections import deque
class Node :
  def __init__(self,x):
    self.data = x
    self.left = None
    self.right = None
class Traversal:
  def __init__(self):
    self.stk = deque()
    self.out = deque()
  def preorder(self,root):## root->left->right
    if root is None :
      return
    self.stk.append(root)
    while self.stk:
      popped = self.stk.pop()
      print(popped.data)
      if popped.right:
        self.stk.append(popped.right)
      if popped.left:
        self.stk.append(popped.left)
  def inorder(self, root):
    curr = root
    while True:
      if curr is not None:
        self.stk.append(curr)
        curr = curr.left
      elif self.stk:
        curr = self.stk.pop()
        print(curr.data)
        curr = curr.right
  def postorder(self, root):
        if root is None:
            return

        self.stk.append(root)

        while self.stk:
            curr = self.stk.pop()
            self.out.append(curr)

            # Push left and right children
            if curr.left:
                self.stk.append(curr.left)
            if curr.right:
                self.stk.append(curr.right)

        # Reverse order: left → right → root
        while self.out:
            print(self.out.pop().data)

t = Traversal()
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(67)
t.postorder(root)
