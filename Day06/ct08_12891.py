# 백준 12891 - DNA 비밀번호
checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

# 함수
def myadd(c): # 새로 들어온 문자 처리
    global checkList, checkList, checkSecret
    
    if c == 'A':
        myList[0] +=1
        if myList[0] == checkList[0]:
            checkSecret +=1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c): # 제거되는 문자 처리
    global checkList, checkList, checkSecret
    
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -=1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P): # 부분 문자열 갯수만큼
    myadd(A[i])

if checkSecret == 4:
    Result += 1

for i in range(P, S): # 2 ~ 4
    j = i - P
    myadd(A[i]) # 이번 슬라이드에서 처리
    myremove(A[j]) # 이전 슬라이드에서 처리한 값을 제거
    if checkSecret == 4:
        Result += 1

print(Result)


# a, b = map(int, input().split())
# l = list(map(str, input()))
# c, d, e, f = map(int, input().split())
# count = 0
# if l.count('A')>=c and l.count('C')>=d and l.count('G')>=e and l.count('T')>=f:
#     for i in range(a-b+1):
#         l1 = l[i:i+b]
#         if l1.count('A')>=c and l1.count('C')>=d and l1.count('G')>=e and l1.count('T')>=f:
#             count+=1
#     print(count)
# else:
#     print(0)