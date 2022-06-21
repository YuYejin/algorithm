# linked list : 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

# 기본 구조
# 노드 : 데이터 저장 단위(데이터값, 포인터)로 구성
# 포인터 : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# 간단한 링크드 리스트 예시
# 노드 구현
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    
# 노드와 노드 연결하기(포인터 활용)
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

# 링크드 리스트로 데이터 추가하기
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    
def add(data):
  node = head
  while node.next: # node에 next가 있다면!
    node = node.next
  node.next = Node(data)
  
node1 = Node(1)
head = node1

for index in range(2, 10):
  add(index)

# 링크드 리스트 데이터 출력하기(검색하기)
node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data)

# 링크드 리스트의 복잡한 기능1 - 링크드 리스트 데이터 사이에 데이터를 추가
node3 = Node(1.5)
node = head
search = True
while search:
  if node.data == 1:
    search = False
  else:
    node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data)