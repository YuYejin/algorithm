# N = int(input())
# m_lst = []
#
# def func(lst):
#     if len(set(lst) == 1):
#         return 50000+lst[0]*5000
#     elif len(set(lst) == 2):
#         if :
#
#         else:
#
#     elif len(set(lst) == 3):
#
#     else:
#         return lst[3]*100
#
# for i in range(N):
#     lst = sorted(list(map(int, input().split())))
#     m_lst.append(func(lst))
#
# print(max(m_lst))

def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return 50000 + lst[0] * 5000
    if len(set(lst)) == 2: # 3, 1의 조합이거나 2, 2의 조합
        if lst[1] == lst[2]: # 3, 1의 조합
            return 10000 + lst[1] * 1000
        else: # 2, 2의 조합
            return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3): # 하나만 같을 경우
        if lst[i] == lst[i+1]:
            return 1000 + lst[i] * 100
    return lst[-1] * 100 # 모두 다를 경우

N = int(input())

print(max(money() for i in range(N)))