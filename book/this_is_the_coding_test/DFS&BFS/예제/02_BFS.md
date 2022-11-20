## BFS
- BFS(Breadth-First Search)는 너비 우선 탐색이라고도 부르며, 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
- DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하는데, BFS는 그 반대이다.

## BFS 동작 과정
- BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다. 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

> 재귀함수로 DFS를 구현하면 컴퓨터 시스템의 동작 특성상 실제 프로그램의 수행 시간은 느려질 수 있다.<br>
> 따라서 스택 라이브러리를 이용해 시간 복잡도를 완화하는 테크닉이 필요할 때도 있다.<br>
> 코딩 테스트에서는 보통 DFS보다는 BFS 구현이 조금 더 빠르게 동작한다는 것을 기억하자.

![graph](https://user-images.githubusercontent.com/98029695/202890814-a6559d06-b7f8-4530-b409-7284ae25b2b1.png)
```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```
```python
1 2 3 8 7 4 5 6
```
