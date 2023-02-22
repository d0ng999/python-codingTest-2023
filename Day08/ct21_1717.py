# 백준 1717 - 집합의 표현 (Union and Find 문제)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())
parent = [0] *(N+1) # 얕은 복사

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀호출 -> 경로압축!!
        return parent[a]

def union(a, b): # 대표노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

def checkSame(a, b): # 두 원소가 같은 집합인지 확인
    a = find(a)
    b = find(b)

    if a == b:
        return True
    else:
        return False
    
for i in range(N+1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split()) # 
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b): # checkSame의 함수에서 True이면
            print('Yes')
        else: # False 이면
            print('No')

