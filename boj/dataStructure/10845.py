import sys

# n = int(input()) -> 시간 초과 에러
n = int(sys.stdin.readline())
que = []

for i in range(n):
    # a = input().split() -> 시간 초과 에러
    a = sys.stdin.readline().split()

    if a[0] == "push":
        que.append(a[1])
    elif a[0] == "pop":
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif a[0] == "size":
        print(len(que))
    elif a[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif a[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])