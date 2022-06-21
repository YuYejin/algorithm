# 객체지향 프로그래밍으로 링크드 리스트 구현하기
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    
class NodeMgmt:
  def __init__(self, data):
    self.head = Node(data)
  
  def add(self, data):
    if self.head == '':
      self.head = Node(data)
    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)
  
  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

  def delete(self, data):
    if self.head == '':
      print("해당 값을 가진 노드가 없습니다.")
      return

    if self.head.data == data: # head 삭제
      temp = self.head
      self.head = self.head.next
      del temp
    else: # 마지막 or 중간 노드 삭제
      node = self.head
      while node.next:
        if node.next.data == data:
          temp = node.next
          node.next = node.next.next
          del temp
        else:
          node = node.next

  def search_node(self, data):
    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1, 10):
  linkedlist1.add(data)
linkedlist1.desc()

# 링크드 리스트의 복잡한 기능2 - 노드 삭제
# (1) 위의 class NodeMgmt에 def delete 추가

# (2) 테스트 위해 1개 노드 생성
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# (3) head가 살아있음을 확인
print(linkedlist1.head)

# (4) head를 지워봄
linkedlist1.delete(0)

# (5) 정상적으로 삭제되었음을 확인
print(linkedlist1.head) # None

# (6) 여러 노드 추가
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1, 10):
  linkedlist1.add(data)
linkedlist1.desc()

# (7) 노드 중 한 개 삭제
linkedlist1.delete(4)
linkedlist1.desc()

linkedlist1.delete(9)
linkedlist1.desc()

# 연습1 - 위 코드에서 노드 데이터가 2인 노드 삭제해보기
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
  node_mgmt.add(data)
node_mgmt.desc()

node_mgmt.delete(2)
node_mgmt.desc()

# 연습2 - 위 코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수 만들고, 테스트 해보기
# (테스트: 임의로 1~9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 4인 노드의 데이터 값 출력해보기)
# (1) 위의 class NodeMgmt에 def search_node 추가

# (2) 테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
  node_mgmt.add(data)

node = node_mgmt.search_node(4)
print(node.data)