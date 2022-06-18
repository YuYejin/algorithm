# 충돌(collision) 해결 알고리즘 (좋은 해쉬 함수 사용하기)

# chaining 기법
# 연습2 - 연습1의 해쉬 테이블 코드에 chaining 기법으로 충돌 해결 코드 추가
hash_table = list([0 for i in range(8)])

def get_key(data):
  return hash(data)

def hash_function(key):
  return key % 8

def save_data(data, value):
  index_key = get_key(data)
  hash_address = hash_function(index_key)
  
  if hash_table[hash_address] != 0:
    for index in range(len(hash_table[hash_address])):
      if hash_table[hash_address][index][0] == index_key:
        hash_table[hash_address][index][1] = value
        return
    hash_table[hash_address].append([index_key, value])
  else:
    hash_table[hash_address] = list([index_key, value])

def read_data(data):
  index_key = get_key(data)
  hash_address = hash_function(index_key)
  
  if hash_table[hash_address] != 0:
    for index in range(hash_address, len(hash_table)):
      if hash_table[index] == 0:
        return None
      elif hash_table[index][0] == index_key:
        return hash_table[index][1]
  else:
    return None

print(hash('dk') % 8)
print(hash('da') % 8)
print(hash('dc') % 8)

save_data('dk', '01022225555')
save_data('da', '01077778888')
print(read_data('dc')) # None