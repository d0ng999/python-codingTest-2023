# 백준 - 2750 수 정렬하기
a = int(input())
A = [0] * a

for i in range(a):
    A[i] = int(input())

for i in range(a-1):
    for j in range(a-1-i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

for i in A:
    print(i)