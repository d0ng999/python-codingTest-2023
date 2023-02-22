# # 공백
# n, m = map(int, input().split())
# A = [[0 for col in range(n)] for row in range(m)]

while True:
    a, b = map(int, input().split())
    if a > b:
        if a % b == 0:
            print('multiple')
        else:
            print('neither')
    elif b > a:
        if b % a == 0:
            print('factor')
        else:
            print('neither')
    else:
        if a == b == 0:
            break            
            
            