# x, y, z = map(int, input().split())
#
# def ck(x, y, z):
#     if x == y and y == z:
#         return 10000+x*1000
#
#     if x == y:
#         return 1000+x*100
#     elif x == z:
#         return 1000 + x * 100
#     elif y == z:
#         return 1000 + y * 100
#     else:
#         return max(x, y, z)*100
#
# print(ck(x, y, z))

lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:
    print(10000+lst[0]*1000)
elif len(set(lst)) == 2:
    print(1000+lst[1]*100)
else:
    print(lst[2]*100)