# 탐욕 알고리즘
# -> 최적의 해에 가까운 값을 구하기 위해 사용
# -> 여러 경우 중 하나를 결정해야할 때마다, "매순간 최적이라고 생각되는 경우를 선택"하는 방식으로 진행해서 최종적인 값을 구하는 방식

# 탐욕 알고리즘 예
# 문제1 - 동전 문제
# 지불해야 하는 값이 4720원 일 때 1원, 50원, 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
coin_list = [1, 100, 50, 500]
print(coin_list)
coin_list.sort(reverse=True)
print(coin_list)

coin_list = [500, 100, 50, 1]

def min_coin_count(value, coin_list):
  total_coin_count = 0
  details = list()
  coin_list.sort(reverse=True)
  for coin in coin_list:
    coin_num = value // coin
    total_coin_count += coin_num
    value -= coin_num*coin
    details.append([coin, coin_num])
  return total_coin_count, details

print(min_coin_count(4720, coin_list))

# 문제2 - 부분 배낭 문제
# 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# (각 물건은 무게(w)와 가치(v)로 표현, 물건은 쪼갤 수 있으므로 일부분이 배낭에 넣어질 수 있음)
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)
print(data_list)

def get_max_value(data_list, capacity):
  data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)
  total_value = 0
  details = list()

  for data in data_list:
    if capacity - data[0] >= 0:
      capacity -= data[0]
      total_value += data[1]
      details.append([data[0], data[1], 1])
    else:
      fraction = capacity / data[0]
      total_value += data[1]*fraction
      details.append([data[0], data[1], fraction])
      break
  return total_value, details

print(get_max_value(data_list, 30)) # (24.5, [[10, 10, 1], [15, 12, 1], [20, 10, 0.25]])