# 1차원 배열 리스트로 구현시
data = [1, 2, 3]
print(data)

# 2차원 배열 리스트로 구현시
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data[0])
print(data[0][0])
print(data[0][1])
print(data[0][2])

# 프로그래밍 연습1 - 9, 8, 7 순서대로 출력하기
print(data[2][2], data[2][1], data[2][0])

# 프로그래밍 연습2 - dataset에서 전체 이름 안에 M이 몇 번 나왔는지 빈도수 출력하기
dataset = ['Masdfasd', 'asdfMasdf', 'sdafsd']
m_count = 0
for data in dataset:
  for index in range(len(data)):
    if data[index] == 'M':
      m_count += 1
print(m_count)