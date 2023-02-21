# # 백준 1541 - 잃어버린 괄호
# import sys
# import math
# input = sys.stdin.readline
# arr = [True for _ in range(246913)]

# c = math.ceil(math.sqrt(246913))
# for i in range(2, c+1):
#     j = 2
#     while i*j <= 246913:
#         if i*j >= 2:
#             arr[i*j] = False
#         j+=1

# while True:
#     n = int(input())
#     if n == 0:
#         break
    

#     count = 0
#     for i in range(n+1, 2*n+1):
#         if i == 1:
#             arr[1] == False

#         elif arr[i] == True:
#             count += 1
#     print(count)

# 기초수학2 - 골드바흐의 추측
import sys
import math
input = sys.stdin.readline
arr = [True for _ in range(10001)]

c = math.ceil(math.sqrt(10001))
for i in range(2, c+1):
    j = 2
    while i*j <= 10001:
        if i*j >= 2:
            arr[i*j] = False
        j+=1