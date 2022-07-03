# 힙과 배열
# 일반적으로 힙 구현시 배열 자료구조를 활용
# 배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면 구현이 좀 더 수월
# - 부모 노드 인덱스 번호 = 자식 노드 인덱스 번호 // 2
# - 왼쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2
# - 오른쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2 + 1

# 힙 클래스 구현 1
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 배열 인덱스를 1로 시작하기 위해
        self.heap_array.append(data)

heap = Heap(1)
print(heap.heap_array) # [None, 1]

# 힙 클래스 구현 2 - insert
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 배열 인덱스를 1로 시작하기 위해
        self.heap_array.append(data)

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        return True

# 힙 클래스 구현 3 - insert2
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 배열 인덱스를 1로 시작하기 위해
        self.heap_array.append(data)

    def move_up(self, inserted_idx): # 자식노드와 부모노드 교환 여부
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self .heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

heap = Heap(15) # 초기 데이터
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array) # [None, 20, 10, 15, 5, 4, 8]