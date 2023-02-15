# 큐 구현
# 전역변수
SIZE = 0 # 변수명을 대문자로 다 쓰면 그 변수는 보통 상수로 취급함
queue = []
front, rear = -1, -1

# Queue Full 확인
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE - 1):
        return False
    elif (rear == SIZE -1) and (front == -1):
        return True
    else:
        # deQueue를 한 뒤 빈자리를 다시 앞으로 채우는 작업
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# Queue Empty 확인
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (rear == front):
        return True
    else:
        return False

# Queue 데이터 추가
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() == True:
        print('Queue is Full')
    else:
        rear += 1
        queue[rear] = data

# Queue 데이타 추출
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    else:
        front +=1
        data = queue[front]
        queue[front] = None
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return data

# Queue front+1 위치값 확인
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    else:
        return queue[front+1]
    
# 메인 엔트리
if __name__ =='__main__':
    SIZE = int(input('큐 사이즈 입력 : '))
    queue = [None for _ in range(SIZE)]

    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) >> ')
        if select.lower() == 'x':
            break
        elif select.lower() == 'i':
            data = input('입력데이터 >> ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'e':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'v':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')           
        else:
            continue

    print('큐 프로그램 종료')


