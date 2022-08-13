# 비트마스크를 이용한 풀이
import copy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
Q = [tuple(map(int, input().split())) for i in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def arr_min(arr):
    return min([sum(i) for i in arr])


def rotate(a, q):
    (r, c, s) = q
    r, c = r - 1, c - 1
    ret = copy.deepcopy(a)
    for d in range(1, s + 1):
        rr, cc = r - d, c + d
        for way in range(4):
            for dd in range(2 * d):
                ret[rr + dx[way]][cc + dy[way]] = a[rr][cc]
                rr, cc = rr + dx[way], cc + dy[way]
    return ret


def dfs(a, q, st):
    if st == (1 << K) - 1: return arr_min(a)
    ret = 50000
    for i in range(K):
        if st & 1 << i == 0: ret = min(ret, dfs(rotate(a, q[i]), q, st | 1 << i))
    return ret


print(dfs(A, Q, 0))
