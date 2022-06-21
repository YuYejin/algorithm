# 간단한 해쉬 예
# hash table 만들기
hash_table = list(i for i in range(10)) # list comprehension
print(hash_table)

# 간단한 해쉬 함수 만들기
# 다양한 해쉬 함수 고안 기법이 있으며, 가장 간단한 방식이 Devision법 (나누기를 통한 나머지 값을 사용하는 기법)
def hash_func(key):
  return key % 5

# 해쉬 테이블에 저장
data1 = "Andy"
data2 = "Dave"
data3 = "Trump"
# ord(): 문자의 아스키 코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))

# 해쉬 테이블에 값 저장 예
def storage_data(data, value):
  key = ord(data[0])
  hash_address = hash_func(key)
  hash_table[hash_address] = value

# 해쉬 테이블에서 특정 주소의 데이터 가져오는 함수 만들기
storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01033332222')

# 실제 데이터 저장하고 읽어보기
def get_data(data):
  key = ord(data[0])
  hash_address = hash_func(key)
  return hash_table[hash_address]
print(get_data('Andy'))

# 연습1 - 리스트 변수를 활용해서 해쉬 테이블 구현
hash_table = list([0 for i in range(8)])

def get_key(data):
  return hash(data)

def hash_function(key):
  return key % 8

def save_data(data, value):
  hash_address = hash_function(get_key(data))
  hash_table[hash_address] = value

def read_data(data):
  hash_address = hash_function(get_key(data))
  return hash_table[hash_address]

save_data('Dave', '01020302000')
save_data('Andy', '01032322000')
print(read_data('Dave'))
print(hash_table)