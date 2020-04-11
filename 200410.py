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

  def find_idx(self, idx):
    pointer = self.head
    for _ in range(idx):
      pointer = pointer.next
    return pointer

  def add(self, node, idx):
    if idx == 0:
      self.head.prev = node
      node.next = self.head
      self.head = node
    elif idx == self.size:
      self.append(node)
    else:
      pointer = self.find_idx(idx)
      node.next = pointer
      node.prev = pointer.prev
      node.prev.next = node
      node.next.prev = node
    self.size += 1
  
  # def get(self, idx):
  #   try:
  #     pointer = self.find_idx(idx)
  #     return pointer.data
  #   except:
  #     return -1

  # def delete(self, idx):
  #   if idx == 0:
  #     self.head = self.head.next
  #     self.head.prev = None
  #   elif idx == self.size:
  #     self.rear = self.rear.prev
  #     self.rear.next = None
  #   else:
  #     pointer = self.find_idx(idx)
  #     pointer.prev.next = pointer.next
  #     pointer.next.prev = pointer.prev
  #   self.size -= 1

  # def change(self, idx, data):
  #   pointer = self.find_idx(idx)
  #   pointer.data = data
  
  def find_large_value(self, value):
    pointer = self.head
    for _ in range(self.size):
      if pointer.data > value:
        return pointer
      pointer = pointer.next
    return -1

  def return_list(self):
    return_box = []
    pointer = self.head
    for _ in range(self.size):
      return_box.append(pointer.data)
      pointer = pointer.next
    return return_box

  def main_merge(self, seq_head, seq_rear, value, size):
    pointer = self.find_large_value(value)
    if pointer == self.head:
      self.head.prev = seq_rear
      seq_rear.next = self.head
      self.head = seq_head
    elif pointer == -1:
      self.rear.next = seq_head
      seq_head.prev = self.rear
      self.rear = seq_rear
    else:
      seq_head.prev = pointer.prev
      seq_rear.next = pointer
      pointer.prev.next = seq_head
      pointer.prev = seq_rear
    self.size += size

class CircularList:
  def __init__(self, node):
    self.head = node
    self.head.next = self.head
    self.head.prev = self.head
    self.size = 1
  
  def add_node_in_pnt(self, node, pointer):
    node.prev = pointer.prev
    node.next = pointer
    pointer.prev.next = node
    pointer.prev = node

    self.size += 1
  
  def append(self, node):
    node.prev = self.head.prev
    node.next = self.head
    node.prev.next = node
    node.next.prev = node
    self.size += 1

  def jump_to_next(self, pointer, distance):
    for _ in range(distance):
      pointer = pointer.next
    return pointer

  def return_list(self):
    return_box = []
    pointer = self.head
    for _ in range(self.size):
      return_box.append(pointer.data)
      pointer = pointer.next
    return return_box

# 5110 수열합치기
def merge_sequence():
  for tc in range(int(input())):
    n, m = list(map(int,input().split()))
    seq_arrs = [list(map(int,input().split())) for _ in range(m)]
    seq_box = []
    for seq_arr in seq_arrs:
      start_node = Node(seq_arr[0])
      tmp_ll = LinkedList(start_node)
      for i in range(1, n):
        tmp_node = Node(seq_arr[i])
        tmp_ll.append(tmp_node)
      seq_box.append(tmp_ll)
    
    main_seq = seq_box[0]
    for i in range(1, n):
      main_seq.main_merge(seq_box[i].head, seq_box[i].rear, seq_box[i].head.data, seq_box[i].size)
    res = list(reversed(main_seq.return_list()))
    print(f'#{tc+1}', *res[:10])


# 5120 암호
def password():
  for tc in range(int(input())):
    n, m, k = list(map(int,input().split()))
    seq_arr = list(map(int,input().split()))
    
    start_node = Node(seq_arr[0])
    circle_list = CircularList(start_node)
    for i in range(1, n):
      tmp_node = Node(seq_arr[i])
      circle_list.append(tmp_node)
    
    pointer = circle_list.head
    for _ in range(k):
      pointer = circle_list.jump_to_next(pointer, m)
      tmp_node = Node(pointer.prev.data + pointer.data)
      circle_list.add_node_in_pnt(tmp_node, pointer)
      pointer = pointer.prev
    res = list(reversed(circle_list.return_list()))
    print(f'#{tc+1}', *res[:10])

# 5110 수열합치기
# merge_sequence()

# 5120 암호
# password()
