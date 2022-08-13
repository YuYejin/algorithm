## 목차
+ [1012번 - 유기농 배추](#1012번---유기농-배추)
+ [16768번 - Mooyo Mooyo](#16768번---mooyo-mooyo)
+ [12100번 - 2048](#12100번---2048)
+ [17406번 - 배열 돌리기4](#17406번---배열-돌리기4)

---

## 1012번 - 유기농 배추
<details>
<summary>문제 및 입출력 펼쳐보기</summary>

### 문제
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

![image](https://user-images.githubusercontent.com/98029695/183277425-3cd41ee5-e1b6-42b9-81de-6b7462b732c2.png)

---

### 입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

### 출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

### 예제 입력1
```python
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
```

### 예제 출력1
```python
5
1
```
</details>

---

+ **Flood Fill 알고리즘**의 대표적인 문제
+ Flood Fill 알고리즘이란?
  + 주어진 시작점으로부터 연결된 영역들을 찾는 알고리즘
  + 다차원 배열의 어떤 칸과 연결된 영역을 찾는 알고리즘
  + 보통 DFS 알고리즘을 이용하여 재귀 함수를 통해 구현하거나, BFS 알고리즘을 이용하여 Queue로 구현한다.

### (1) input을 넣는 과정
```python
T = int(input())
B = [] # 배추

def process():
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1

for _ in range(T):
    process()
```
+ BFS와 DFS를 사용할 때 상하좌우를 살펴봐야 하므로, 배열의 인덱스를 넘지 않도록 가상의 0을 채워준다.
+ 이때 0은 배추가 없으므로 BFS와 DFS 탐색 조건에 어긋나게 되어 알아서 제외된다.
+ 실수로 'B\[X+1]\[Y+1] = 1' 라고 입력하지 않도록 주의하자.

### (2) 체크 배열과 정답 변수
```python
T = int(input())
B, ck = [], []

def process():
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    ck = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)
    

for _ in range(T):
    process()
```
+ Flood Fill의 핵심은 배열의 어떤 부분이 채워져 있는지 알 수 없기 때문에 전체 탐색을 진행하고, 탐색한 부분을 다시 탐색하지 않는 것이다.
+ 탐색한 부분은 탐색했다고 표시해주기 위해 ck를 만들어 주었다.
+ ck\[i]\[j]가 1로 채워져 있다면 즉, 이미 방문했다면 continue로 넘어가주고, 아닌 경우에만 dfs(i, j)로 그 지점에서 순회를 돌아준다.
+ 순회를 시작한다는 것은 아직 체크가 되지 않은 배열의 순회를 시작하겠다는 의미이다. 이 말은 새로운 그룹을 하나 찾았다는 의미가 된다.
+ 우리의 출력 정보 즉, 정답인 ans 변수를 이중 for문 상단과 하단에 작성해주고, for문이 끝났을 때 ans가 출력되게 한다.
+ 이제 dfs 함수를 작성하면 된다.

### (3) dfs 함수
```python
T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global B, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i] # 다음으로 순회를 돌 점
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)

def process():
    global B, ck
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    ck = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)
    

for _ in range(T):
    process()
```
+ 처음 지점에 'ck\[x]\[y] = 1'로 체크를 해주고, for문으로 네 방향을 확인한다.
+ 이때 다음에 갈 방향이 0이거나, 이미 갔던 곳이라면 가지 않는다.
+ global B, ck를 덧붙여 전역변수를 사용한다고 선언한다.

### (4) 런타임 에러 수정
```python
import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global B, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)

def process():
    global B, ck
    M, N, K = map(int, input().split())
    B = [[0 for i in range(50+2)] for _ in range(50+2)]
    ck = [[0 for i in range(50+2)] for _ in range(50+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)

for _ in range(T):
    process()
```
+ (3)까지 작성 후 제출을 해보면 런타임 에러가 발생하는 것을 확인할 수 있다.
+ DFS를 사용할 때는 가끔 재귀함수 깊이가 너무 깊어질 경우 런타임 에러가 발생할 수 있는데, 재귀함수의 깊이를 제한하는 함수를 작성해주면 이 문제를 해결할 수 있다.
+ 'sys.setrecursionlimit(10000)'를 통해 재귀함수 깊이를 제한해주자.

## 16768번 - Mooyo Mooyo
<details>
<summary>문제 및 입출력 펼쳐보기</summary>

### 문제
With plenty of free time on their hands (or rather, hooves), the cows on Farmer John's farm often pass the time by playing video games. One of their favorites is based on a popular human video game called Puyo Puyo; the cow version is of course called Mooyo Mooyo.

The game of Mooyo Mooyo is played on a tall narrow grid N cells tall (1 ≤ N ≤ 100) and 10 cells wide. Here is an example with N = 6:
```python
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223
```
Each cell is either empty (indicated by a 0), or a haybale in one of nine different colors (indicated by characters 1..9). Gravity causes haybales to fall downward, so there is never a 0 cell below a haybale.

Two cells belong to the same connected region if they are directly adjacent either horizontally or vertically, and they have the same nonzero color. Any time a connected region exists with at least K cells, its haybales all disappear, turning into zeros. If multiple such connected regions exist at the same time, they all disappear simultaneously. Afterwards, gravity might cause haybales to fall downward to fill some of the resulting cells that became zeros. In the resulting configuration, there may again be connected regions of size at least K cells. If so, they also disappear (simultaneously, if there are multiple such regions), then gravity pulls the remaining cells downward, and the process repeats until no connected regions of size at least K exist.

Given the state of a Mooyo Mooyo board, please output a final picture of the board after these operations have occurred.

---

### 입력
The first line of input contains N and K (1 ≤ K ≤ 10N). The remaining N lines specify the initial state of the board.

### 출력
Please output N lines, describing a picture of the final board state.

### 예제 입력1
```python
6 3
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223
```

### 예제 출력1
```python
0000000000
0000000000
0000000000
0000000000
1054000000
2254500000
```
</details>

---

+ 문제를 간략히 설명하자면 최대 100*100 크기의 map이 존재하고, 이 map에서 어떠한 특정 같은 수는 한 그룹이다. 이 그룹에 속한 수가 K개를 넘어가면 삭제되고 나머지가 아래로 내려온다. 이 과정을 반복했을 때 마지막에 남는 상태가 어떠한지 출력으로 나타내면 된다.
+ 이 문제는 **Flood Fill 알고리즘**을 기초지식으로 요구하고 있고, **Flood Fill 알고리즘으로 처리한 것을 이후에 어떻게 다시 처리할 것인지**도 이야기하고 있다. 마지막으로 **2차원 배열에서 배열 내부에 있는 요소들을 어떻게 잘 이동시킬 수 있는가**에 대한 것도 묻고 있다.
+ 따라서 BFS 혹은 DFS로 그룹의 개수를 찾고 이를 반환하는 함수, 그 그룹에 속한 수가 K개가 넘었을 때 그룹을 삭제하는 함수, 요소를 내려오게 하는 함수를 반복문으로 변화가 발생하지 않을 때까지 돌려주면 될 것이다.

### (1) input을 넣는 과정
```python
# import sys
# sys.setrecursionlimit(10000)

N, K = map(int, input().split())
M = [list(input()) for _ in range(N)] # [['0', '0', ..., '0'], ['0', '0', ... '0'], ...]

while True:
    exist = True
    
    if exist: # 바뀌는 게 없을 때 반복문을 빠져 나온다.
        break

for i in M:
    print(''.join(i))
```
+ 바뀌는 것이 있을 때까지 반복하기 위해 while문을 작성한다.
+ 이제 우리가 해야할 것은 단 두 가지이다. dfs를 돌리고, dfs가 맞으면 다시 dfs를 돌려서 없애는 것이다.

### (2) 체크 배열과 결과 변수
```python
# import sys
# sys.setrecursionlimit(10000)

def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)

def dfs(x, y):
  pass
  
def dfs2(x, y):
  pass
  
def down():
  pass

while True:
    exist = False
    ck = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j) # 개수 세기
            if res >= K:
                dfs2(i, j) # 지우기
                exist = True
    if not exist:
        break
    down() # 내리기

for i in M:
    print(''.join(i))
```
+ 반복문 내부를 작성한 결과 dfs, dfs2, down 총 3개의 함수를 짜야한다는 것을 알 수 있다.

### (3) dfs, dfs2, down 함수
```python
# import sys
# sys.setrecursionlimit(10000)

def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)
ck2 = new_array(N)


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret


def dfs2(x, y, val):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx, yy, val)


def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != '0':
                tmp.append(M[j][i])
        for j in range(N-len(tmp)):
            M[j][i] = '0'
        for j in range(N-len(tmp), N):
            M[j][i] = tmp[j - (N-len(tmp))]


while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j) # 개수 세기
            if res >= K:
                dfs2(i, j, M[i][j]) # 지우기
                exist = True
    if not exist:
        break
    down() # 내리기

for i in M:
    print(''.join(i))
```

---

## 12100번 - 2048
<details>
<summary>문제 및 입출력 펼쳐보기</summary>

### 문제
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

(그림을 통한 예시는 [링크](https://www.acmicpc.net/problem/12100)를 통해 확인)

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

---

### 입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

### 출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

### 예제 입력1
```python
3
2 2 2
4 4 4
8 8 8
```

### 예제 출력1
```python
16
```
</details>

---

+ 삼성 A형, 삼성 공채 문제와 유사하다.
+ 이러한 문제는 BFS, DFS, 구현을 이용해 푸는 것이 대다수이다.
+ 상하좌우 4방향을 총 5번 움직일 수 있으므로, 모든 경우가 다르다면 4의 5승인 1024가지가 나온다. 따라서 1024가지의 경우의 수에서 max값을 구하는 문제이다.
+ 꼭 5번 움직일 필요는 없다는 것에 주의하자.
+ 한시간에서 두시간 정도의 풀이 시간이 소요되며, 테스트 케이스를 돌리는 시간까지 고려하면 30분에서 45분 정도의 시간을 풀이에 할애한다고 생각하면 된다.

### (1) input을 넣는 과정
```python
N = int(input())
B = [list(map(int, input().split())) for i in range(N)]  #[[2, 2, 2], [4, 4, 4], [8, 8, 8]]
```
+ 1024가지의 경우를 어떤식으로 탐색할 것인가?
+ 상하좌우로 움직이는 것 그리고 합치는 것은 주어진 시간 내에 문제를 풀기에 적합하지 않다.
+ 최근 코딩테스트 유형은 상하좌우로 움직이는 경우 따로 움직여도 되지만, map을 돌리는 것이 더 효율적인 경향이 있다.
+ 방향을 하나로 미리 설정해 두고, map만 조금씩 회전시키는 것이다.
+ 우리는 결과적으로 map을 출력하는 것이 아닌 최대값을 출력하는 것이기 때문에 회전 방향에 대해서는 고려할 필요가 없다.

### (2) dfs 함수
```python
N = int(input())
B = [list(map(int, input().split())) for i in range(N)]

def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)
    return ret


print(dfs(N, B, 5))
```
+ 'print(dfs(N, B, 5))'에서 5는 이동할 수 있는 최대 횟수이다.
+ 따라서 dfs 함수의 'if count == 0: return ret'은 이동 횟수가 0인 경우 Board의 최댓값을 반환하라는 의미이다. (이동횟수 제한)
+ 한 번 dfs를 돌릴 때에는 상하좌우 총 4가지의 브랜치를 만들 수 있다.
+ 반복문을 총 4번 돌리면서 배열을 원하는 방향으로 연산해 주고, 그것이 기존 값과 다르다면 계속해서 dfs를 돌려주면서 리턴값 ret을 갱신해준다.
+ 그리고 보드를 의미하는 B를 반복문을 한 번 반복할 때마다 90도로 돌려준다.

### (3) rotate90, convert 함수
```python
from copy import deepcopy

N = int(input())
B = [list(map(int, input().split())) for i in range(N)]  #[[2, 2, 2], [4, 4, 4], [8, 8, 8]]


def convert(lst, N):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))


def rotate90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = B[i][j]
    return NB


def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)
    return ret


print(dfs(N, B, 5))
```
+ rotate90 함수의 경우에는 외우는 것이 좋다.
+ convert 함수에서 우선 'new_list = [i for i in lst if i]'를 통해 0이 아닌 숫자들 즉, 양수만 남긴다.
+ 그 다음 for문을 통해 1부터 돌리며 지금 값과 그 전 값이 같으면, 지금 값은 0으로 만들고 전 값은 2배를 해준다. (2 2 2 2 배열 -> 4 0 4 0 배열)
+ 'new_list = [i for i in new_list if i]'을 통해 다시 0이 아닌 숫자들 즉, 양수만 남긴다.
+ 'return new_list + [0] * (N-len(new_list))'으로 남은 칸을 0으로 채운 배열을 리턴한다.

---

## 17406번 - 배열 돌리기4
<details>
<summary>문제 및 입출력 펼쳐보기</summary>

### 문제
크기가 N×M 크기인 배열 A가 있을때, 배열 A의 값은 각 행에 있는 모든 수의 합 중 최솟값을 의미한다. 배열 A가 아래와 같은 경우 1행의 합은 6, 2행의 합은 4, 3행의 합은 15이다. 따라서, 배열 A의 값은 4이다.
```python
1 2 3
2 1 1
4 5 6
```
배열은 회전 연산을 수행할 수 있다. 회전 연산은 세 정수 (r, c, s)로 이루어져 있고, 가장 왼쪽 윗 칸이 (r-s, c-s), 가장 오른쪽 아랫 칸이 (r+s, c+s)인 정사각형을 시계 방향으로 한 칸씩 돌린다는 의미이다. 배열의 칸 (r, c)는 r행 c열을 의미한다.

예를 들어, 배열 A의 크기가 6×6이고, 회전 연산이 (3, 4, 2)인 경우에는 아래 그림과 같이 회전하게 된다.
```python
A[1][1]   A[1][2] → A[1][3] → A[1][4] → A[1][5] → A[1][6]
             ↑                                       ↓
A[2][1]   A[2][2]   A[2][3] → A[2][4] → A[2][5]   A[2][6]
             ↑         ↑                   ↓         ↓
A[3][1]   A[3][2]   A[3][3]   A[3][4]   A[3][5]   A[3][6]
             ↑         ↑                   ↓         ↓
A[4][1]   A[4][2]   A[4][3] ← A[4][4] ← A[4][5]   A[4][6]
             ↑                                       ↓
A[5][1]   A[5][2] ← A[5][3] ← A[5][4] ← A[5][5] ← A[5][6]

A[6][1]   A[6][2]   A[6][3]   A[6][4]   A[6][5]   A[6][6]
```
회전 연산이 두 개 이상이면, 연산을 수행한 순서에 따라 최종 배열이 다르다.

다음은 배열 A의 크기가 5×6이고, 회전 연산이 (3, 4, 2), (4, 2, 1)인 경우의 예시이다.
```python
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
```
배열 A에 (3, 4, 2), (4, 2, 1) 순서로 연산을 수행하면 배열 A의 값은 12, (4, 2, 1), (3, 4, 2) 순서로 연산을 수행하면 15 이다.

배열 A와 사용 가능한 회전 연산이 주어졌을 때, 배열 A의 값의 최솟값을 구해보자. 회전 연산은 모두 한 번씩 사용해야 하며, 순서는 임의로 정해도 된다.

---

### 입력
첫째 줄에 배열 A의 크기 N, M, 회전 연산의 개수 K가 주어진다.

둘째 줄부터 N개의 줄에 배열 A에 들어있는 수 A[i][j]가 주어지고, 다음 K개의 줄에 회전 연산의 정보 r, c, s가 주어진다.

### 출력
배열 A의 값의 최솟값을 출력한다.

### 예제 입력1
```python
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
```

### 예제 출력1
```python
12
```
</details>

---

+ 
+ 
