# 백준 10989 - 수 정렬하기3
# 기수정렬 정도는 외워두는게 좋다고 하심
import sys
input = sys.stdin.readline

N = int(input())
count = [0]*1000001

for i in range(N):
    count[int(input())] += 1

for i in range(1000000):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)