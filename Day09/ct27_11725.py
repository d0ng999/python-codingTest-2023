# 백준 11725 - 트리의 부모찾기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
visited = [False] * (N+1)
tree = [[] for _ in range(N+1)]
answer = [0] * (N+1)

for _ in range(1, N):
    n1, n2 = map(int, input().split()) # 부모, 자식 노드인데, 순서는 상관없음
    tree[n1].append(n2)
    tree[n2].append(n1)

# DFS 탐색
def DFS(number):
    visited[number] = True # 방문
    for i in tree[number]:
        if not visited[i]:
            answer[i] = number # 부모노드를 정답 리스트에 저장
            DFS(i)

DFS(1) # 부모노드부터 DFS 시작

for i in range(2, N+1): # 1번은 루트노드라서
    print(answer[i])