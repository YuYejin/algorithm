N = input()
S = '1'*len(N)

print(N, S)

if int(N) >= int(S):
    print(len(N))
else:
    print(len(N)-1)