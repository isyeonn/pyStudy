print('아자아자화이팅')

#스택 (LIFO)
stack = []
#삽입
stack.append(5)
stack.append(7)
stack.append(3)
#삭제
stack.pop()

#최상단 원소부터 출력 : pop하는 순서대로
#리스트 순서 역순
print(stack[::-1])
#최하단 원소부터 출럭
print(stack)


#큐 (FIFO)
from collections import deque
#효율을 위해 리스트가 아닌 덱 사용

queue = deque()
#삽입
queue.append(2)
queue.append(3)
queue.append(7)
#삭제
queue.popleft()

#먼저 들어온 순서대로 출력
print(queue)
#나중에 들어온 원소부터 출력
queue.reverse()
print(queue)


#재귀함수
#팩토리얼
def factorial_recursive(n):
  if n < 2:
    return 1
  else:
    return n * factorial_recursive(n - 1)

result = 1
print('5! = ', factorial_recursive(5))

#최대공약수 - 유클리드 호제법
def gcd(a, b):
  if a % b == 0: #나누어 떨어질 때까지 재귀
    return b
  else:
    return gcd(b, a % b)

print(gcd(192, 162))

#DFS (깊이 우선 탐색)
#탐색 시작 노드를 스택에 삽입하고 방문 처리
#스택의 최상단 노드에 방문하지 않은 인접노드가 하나라도 있으면 스택에 넣고 방문처리
#방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
#2번을 수행할 수 없을 때까지 반복
print('깊이 우선 탐색')
#파이썬에서는 그래프를 2차원리스트로 표현
#각 노드가 연결된 정보를 표현
graph = [
  [], #노드의 번호가 1번부터 시작하는 경우가 많아서 0번은 비워둠
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#방문한 노드
visited = [False] * 9

def dfs(graph, v, visited):
  #현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')

  #현재 노드와 인접한 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

#호출
dfs(graph, 1, visited)


#BFS (너비 우선 탐색)
#탐색 시작 노드를 큐에 삽입하고 방문 처리
#큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 방문
#2번을 수행할 수 없을 때까지 반복
print('\n너비 우선 탐색')
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  #현재 노드 방문 처리
  visited[start] = True
  #큐가 빌 때까지 반복
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    #아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * 9 #방문 정보 초기화
bfs(graph, 1, visited)

#연결요소 찾기
#N X M 크기의 얼음틀
#0이면 구멍, 1이면 칸막이
#생성되는 총 얼음의 개수
def dfs_ice(x, y):
  #범위를 벗어나면 종료
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  #미방문 노드를 방문하기
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs_ice(x - 1, y) #상
    dfs_ice(x + 1, y) #하
    dfs_ice(x, y - 1) #좌
    dfs_ice(x, y + 1) #우
    return True
  return False

print('n, m 입력 (4 5)')
n, m = map(int, input().split())
graph = []
print('row 단위로 그래프 정보 입력')
for i in range(n):
  graph.append(list(map(int, input())))

result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs_ice(i, j) == True:
      result += 1

print(result, end='\n')

#미로 탈출
#N X M 크기의 미로
#(1, 1)에서 시작, (N, M)에서 종료
#괴물이 있으면 0, 없으면 1
#탈출하기 위해 움직여야 할 최소 칸의 개수. 시작, 마지막 칸 포함

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue: #큐가 빌 때까지 반복
    x, y = queue.popleft()
    #현재 위치에서 4가지 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #범위를 벗어나면 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      #벽인 경우 무시
      if graph[nx][ny]  == 0:
        continue

      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  #가장 오른쪽 아래 까지의 최단 거리 반환
  return graph[n - 1][m - 1]


from collections import deque

print('N, M 입력(5 6)')
n, m = map(int, input().split())
print('row 단위로 graph 입력')
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

#이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

print(bfs(0, 0))
