# 2차원 구간합 - 11660번
import sys
input = sys.stdin.readline

n, m = tuple(map(int,input().split())) # 2차원행렬크기, 질의갯수
A = [[0] *(n+1)]
D = [[0] *(n+1) for _ in range(n+1)] # for문에서 _는 변수없이 반복문 실행

for i in range(n):
    rows = list(map(int, input().split()))
    A_row =[0]+ rows
    A.append(A_row)

# 2차원 합배열 D를 만든다.
for i in range(1, n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간합
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)