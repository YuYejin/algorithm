graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# DFS 알고리즘 구현 - need_visit 스택과 visited 큐 생성
def dfs(graph, start_node):
  visited, need_visit = list(), list()
  need_visit.append(start_node)

  while need_visit:
    node = need_visit.pop()
    if node not in visited:
      visited.append(node)
      need_visit.expend(graph[node])

  return visited

print(dfs(graph, 'A'))

# 일반적인 DFS 시간 복잡도
# 노드 수 : V
# 간선 수 : E
# 시간 복잡도 : O(V + E)