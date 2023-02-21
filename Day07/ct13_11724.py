# 백준 11724 - 연결 요소의 개수
import sys

# 재귀호출 파이썬 제한 - 1000번까지 가능
# 재귀호출의 제한을 풀어줌
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split()) # 6 5
A = [[] for _ in range(n+1)] # 7개의 2차원 리스트
visited = [False] * (n+1) # [0, 1, 2, 3, 4, 5, 6]

# DFS 함수
def DFS(v):
    visited[v] = True # 방문노드를 참으로 바꿔줌
    for i in A[v]:
        if not visited[i]: # 방문을 안했다면
            DFS(i)

for _ in range(m): # 엣지의 개수만큼 돌기
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)
        
print(count)