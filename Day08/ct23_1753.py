# 백준 1753 - 최단경로
import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input()) # 시작노드
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 갈 때, 가중치 w
    myList[u].append((v,w))

q.put((0, K)) # q에 시작점을 집어넣는다, queue에 넣을 때는 가중치, 노드순으로 넣었다.
distance[K] = 0

while q.qsize() > 0:
    current = q.get() # current에 q의 값을 가져온다
    c_v = current[1]
    if visited[c_v]:
        continue

    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next)) # 가중치로 오름차순

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print('INF')
