# queue : 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조(FIFO 방식)

# 파이썬 queue 라이브러리 - Queue(), LifoQueue(), PriorityQueue()
import queue

# Queue()
data_queue = queue.Queue()
data_queue.put("funcoding")
data_queue.put(1)
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())

# LifoQueue() -> LILO
data_queue = queue.LifoQueue() 
data_queue.put("funcoding")
data_queue.put(1)
print(data_queue.qsize())
print(data_queue.get())

# PriorityQueue()
data_queue = queue.PriorityQueue()
data_queue.put((10, "korea")) # 튜플 형식((우선순위, 데이터))
data_queue.put((5, 1))
data_queue.put((15, "china"))
print(data_queue.qsize()) # 3
print(data_queue.get()) # (5, 1)
print(data_queue.get()) # (10, 'korea')

# 프로그래밍 연습 - 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현
queue_list = list()

def enqueue(data):
  queue_list.append(data)

def dequeue():
  data = queue_list[0]
  del queue_list[0]
  return data

for index in range(10):
  enqueue(index)

print(dequeue()) # 0
print(dequeue()) # 1
print(dequeue()) # 2