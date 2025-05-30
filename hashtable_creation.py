class hashTable :
  def __init__(self):
    self.max = 10
    self.arr = [None for i in range(self.max)]
  def hashfunction(self,s):
    res = 0
    m = 10
    for i in s:
      res += ord(i)
    return res%m
  def setItem(self,key,val):
    h = self.hashfunction(key)
    self.arr[h] = val
  def getItem(self,key):
    h = self.hashfunction(key)
    return self.arr[h]
p = hashTable()
p.setItem('abhi',10)
p.setItem('chitti',18)
print(p.getItem('chitti'))
## method onerloadind and method overriding
class hashTable :
  def __init__(self):
    self.max = 10
    self.arr = [None for i in range(self.max)]
  def hashfunction(self,s):
    res = 0
    m = 10
    for i in s:
      res += ord(i)
    return res%m
  def __setitem__(self,key,val):
    h = self.hashfunction(key)
    self.arr[h] = val
  def __getitem__(self,key):
    h = self.hashfunction(key)
    return self.arr[h]
d = hashTable()
d['chitti'] = 90
d['poori'] = 100
print(d['chitti'])