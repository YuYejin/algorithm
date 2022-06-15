# 더블 링크드 리스트
class Node:
  def __init__(self, data, prev=None, next=None):
    self.prev = prev
    self.data = data
    self.next = next

class NodeMgmt:
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head

  def insert(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = self.head
      while node.next:
        node = node.next
      new = Node(data)
      node.next = new
      new.prev = node
      self.tail = new

  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

  def search_from_head(self, data):
    if self.head == None:
      return False

    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next
    return False

  def search_from_tail(self, data):
    if self.head == None:
      return False

    node = self.tail
    while node:
      if node.data == data:
        return node
      else:
        node = node.prev
    return False

  def insert_before(self, data, before_data):
    if self.head == None:
      self.head = Node(data)
      return True
    else:
      node = self.tail
      while node.data != before_data:
        node = node.prev
        if node == None:
          return False
      new = Node(data)
      before_new = node.prev
      before_new.next = new
      new.prev = before_new
      new.next = node
      node.prev = new
      return True

  def insert_after(self, data, after_data):
    if self.head == None:
      self.head = Node(data)
      return True
    else:
      node = self.head
      while node.data != after_data:
        node = node.next
        if node == None:
          return False
      new = Node(data)
      after_new = node.next
      new.next = after_new
      new.prev = node
      node.next = new
      if new.next == None:
        self.tail = new
      return True
        

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
  double_linked_list.insert(data)
double_linked_list.desc()

# 연습3 - 위 코드에서 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고, 테스트해보기
# (더블 링크드 리스트의 tail에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현)
# (테스트: 임의로 0~9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드 추가)

# class NodeMgmt에 def search_from_head, search_from_tail, insert_before 추가 생성

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

node_3 = double_linked_list.search_from_tail(3)
print(node_3.data)

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()

node_3 = double_linked_list.search_from_tail(1.5)
print(node_3.data)

# 연습4 - 위 코드에서 노드 데이터가 특정 숫자인 노드 뒤에 데이터를 추가하는 함수를 만들고, 테스트해보기
# (더블 링크드 리스트의 head에서부터 다음으로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현)
# (테스트: 임의로 0~9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 1인 노드 다음에 1.7 데이터 값을 가진 노드 추가)

# class NodeMgmt에 def insert_after 추가 생성

node_mgmt = NodeMgmt(0)
for data in range(1, 10):
  node_mgmt.insert(data)

node_mgmt.desc()

node_mgmt.insert_after(1.7, 1)
node_mgmt.desc()