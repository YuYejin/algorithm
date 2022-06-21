# stack : 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 구조(LIFO 방식)

# 주요 기능 : push(), pop()

# 재귀 함수
def recursive(data):
  if data < 0:
    print("ended")
  else:
    print(data)
    recursive(data - 1)
    print("returned", data)
print(recursive(4))

# 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기 - append(push), pop 메서드 제공
data_stack = list()
data_stack.append(1)
data_stack.append(2)
print(data_stack) # [1, 2]
print(data_stack.pop()) # 2

# 프로그래밍 연습1 - pop, push 함수 사용하지 않고 구현해보기
stack_list = list()

def push(data):
  stack_list.append(data)

def pop():
  data = stack_list[-1]
  del stack_list[-1]
  return data

for index in range(10):
  push(index)

print(pop())