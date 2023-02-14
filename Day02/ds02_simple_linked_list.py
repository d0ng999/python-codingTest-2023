# 단순 연결리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return
    
    print(current.data, end = ' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end = ' -> ')

# 노드추가
def insertNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData: # 첫노드 앞
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head # 제일 앞으로
    while current.link != None: # 중간노드 추가방식
        pre = current # pre는 현재노드로
        current = current.link # 현재노드를 다시 다음노드를 향한 link로

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # current.link == None 이라면
    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드삭제
def deleteNode(deleteData):
    global memory, pre, current, head

    if head.data == deleteData:
        current = head
        head = head.link # 두번째 노드로 변경
        del(current)
        return
    
    current = head
    while current.link != None: # 첫번째 이외의 노드 삭제
        pre = current # pre, current, head를 모두 첫번째 노드로 맞춤
        current = current.link # 여전히 pre는 current이고, current는 current가 가리키는 노드가 됨
        if current.data == deleteData:
            pre.link = current.link # current가 가리키는 노드를 pre가 가리키는 노드와 동일하게 만들어줌
            del(current)
            return
        

def findNode(findData):
    global memory, pre, current, head
    
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node() # 빈 노드 반환

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두번째노드 이후부터 쭉~ 4번 반복
        pre = node
        node = Node()
        node.data = data # 1번부터이니 정연, 쯔위, 사나, 지효 순으로
        pre.link = node
        memory.append(node)
    
    printNodes(head) # 전체출력

    print('노드 추가')

    insertNode('다현','화사') # 다현이라는 인덱스 앞에 화사를 넣기
    printNodes(head)

    insertNode('사나', '솔라') # 사나 노드 앞에 솔라를 추가
    printNodes(head)

    insertNode('재남', '문별') # 없는 데이터를 넣게되면 제일 마지막에 생성된다.
    printNodes(head)

    print('노드 삭제')
    deleteNode('화사')
    printNodes(head)

    deleteNode('지효')
    printNodes(head)

    deleteNode('재남')
    printNodes(head)

    deleteNode('문별')
    printNodes(head)

    print('노드검색')
    result = findNode('정연')

    if result.data != None:
        print('데이터를 찾았습니다.')
    else:
        print('검색한 데이터가 없습니다')
    
    result = findNode('재남')
    if result.data !=None:
        print('데이터를 찾았습니다.')
    else:
    
        print('검색한 데이터가 없습니다')