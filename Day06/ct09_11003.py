# 백준 - 11003 - 최솟값찾기1
from collections import deque
# from pythonds.basic.deque import Deque
mydeque = deque()
N, L = map(int, input().split()) #12 3

now = list(map(int, input().split()))
 
 # 새값이 들어올 때마다 정렬 대신 현재수보다 큰 값을 덱에서 제거
 # 시간복잡도를 줄여준다
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 인덱스가 현재 값보다 크면 빼기
        mydeque.pop()
    mydeque.append((now[i], i))

    if mydeque[0][1] <= i - L: # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end = ' ') # 이 값은 무조건 최솟값이다.(min())
