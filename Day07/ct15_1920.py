# 백준 1920 - 원하는 정수 찾기
N = int(input()) # 5
A = list(map(int, input().split()))
A.sort() # 파이썬에서 제공하는 기본 정렬

M = int(input()) # 4
targetlist = list(map(int, input().split()))

for i in range(M):
    find = False
    target = targetlist[i]
    # 이진 탐색
    start = 0
    end = N-1
    while start <= end:
        midle = (start + end) // 2 # 중앙 인덱스
        midVal = A[midle] # 중앙에 있는 값
        if midVal > target: # 오른쪽을 날림
            end = midle - 1
        elif midVal < target: # 왼쪽을 날림
            start = midle+1
        else: # 값을 찾음
            find = True
            break

    if find:
        print(1)
    else:
        print(0)