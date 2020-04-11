class Node:
  def __init__(self, data=0):
    self.data = data
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.rear = node
    self.size = 1

  def append(self, node):
    self.rear.next = node
    node.prev = self.rear
    self.rear = node
    self.size += 1

  def add(self, node, idx):
    if idx == 0:
      self.head.prev = node
      node.next = self.head
      self.head = node
    elif idx == self.size:
      self.append(node)
    else:
      pointer = self.head
      for _ in range(idx):
        pointer = pointer.next
      node.next = pointer
      node.prev = pointer.prev
      node.prev.next = node
      node.next.prev = node
    self.size += 1
  
  def get(self, idx):
    try:
      pointer = self.head
      for _ in range(idx):
        pointer = pointer.next
      return pointer.data
    except:
      return -1

  def delete(self, idx):
    if idx == 0:
      self.head = self.head.next
      self.head.prev = None
    elif idx == self.size:
      self.rear = self.rear.prev
      self.rear.next = None
    else:
      pointer = self.head
      for _ in range(idx):
        pointer = pointer.next
      pointer.prev.next = pointer.next
      pointer.next.prev = pointer.prev
    self.size -= 1

  def change(self, idx, data):
    pointer = self.head
    for _ in range(idx):
      pointer = pointer.next
    pointer.data = data

def add_number():
  for tc in range(int(input())):
    n, m, l = list(map(int,input().split()))
    su_arr = list(map(int,input().split()))
    
    start_node = Node(su_arr[0])
    l_list = LinkedList(start_node)
    for i in range(1, len(su_arr)):
      tmp_node = Node(su_arr[i])
      l_list.append(tmp_node)

    add_arrs = [list(map(int,input().split())) for _ in range(m)]
    for add_arr in add_arrs:
      tmp_node = Node(add_arr[1])
      l_list.add(tmp_node, add_arr[0])
    
    print(f'#{tc+1} {l_list.get(l)}')


def edit_sequence():
  for tc in range(int(input())):
    n, m, l = list(map(int,input().split()))
    su_arr = list(map(int,input().split()))
    
    start_node = Node(su_arr[0])
    l_list = LinkedList(start_node)
    for i in range(1, len(su_arr)):
      tmp_node = Node(su_arr[i])
      l_list.append(tmp_node)

    add_arrs = [list(input().split()) for _ in range(m)]

    for add_arr in add_arrs:
      if add_arr[0] == "I":
        tmp_node = Node(int(add_arr[2]))
        l_list.add(tmp_node, int(add_arr[1]))
      elif add_arr[0] == "D":
        l_list.delete(int(add_arr[1]))
      else:
        l_list.change(int(add_arr[1]), int(add_arr[2]))
    
    print(f'#{tc+1} {l_list.get(l)}')

# 5108 숫자추가
# add_number()

# 5122 수열편집
# edit_sequence()