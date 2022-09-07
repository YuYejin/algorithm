N = input()
S = '1'*len(N)

if len(N) == 1:
    print(1)
elif int(N) >= int(S):
    print(len(N))
else:
    print(len(N)-1)

# 0 1 2 3 4 5 6 7 8 9 (<11)
# 0 1 2 3 4 5 6 7 8 9 (<111)
# 0 1 2 3 4 5 6 7 8 9 (<1111)