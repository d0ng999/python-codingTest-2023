# 백준 11657 - 타임머신
# 벨만 포드 - 가중치에 음수가 포함될 수 있고, 사이클이 형성된다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N+1)

for _ in range(M): # 엣지 리스트 저장
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0

for _ in range(N-1): # 노드개수 - 1까지 반복
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

# 음수 사이클 확인
mCycle = False
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True # 음수사이클이 존재!
        break # 음수사이클이 있다면 중단

if mCycle != True:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else: # 도시에 방문을 하지 않았을 때
            print(-1)
else:
    print(-1)