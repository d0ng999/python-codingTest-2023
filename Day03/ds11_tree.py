# 이진 탐색 트리 구현
# 전역 변수 선언
# 이진 검색의 검색 시간은 빠른 편이다.
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# 값의 크기로 순서를 나누는데 
# 1. 블랙핑크의 ㅂ과 레드벨벳의 ㄹ을 비교함. ㅂ이 더 늦은 숫자이므로 블랙핑크가 부모노드
# 2. 마마무 역시 ㅂ보다 ㅁ이 더 낮은 숫자
# 3. 에이핑크의 ㅇ는 ㅂ보다 큼 => 그래서 오른쪽으로 이동
# 4. 트와이스는 이 그룹중 가장 큰 숫자, 그래서 가장 오른쪽이다.
# 5. 걸스데이는 ㄱ으로 가장 낮은 숫자이므로 제일 왼쪽
# 6. 마마무는 ㄹ보다 크지만 ㅂ보다 작음. 그래서 레드벨벳의 오른쪽으로 이동.
class TreeNode:
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None

if __name__ == '__main__':
    node = TreeNode()
    node.data = nameAry[0] # BlackPink
    root = node
    memory.append(node)

    for name in nameAry[1:]:
        node = TreeNode()
        node.data = name
        current = root

        while True:
            if name < current.data: # 부모노드의 왼쪽으로 이동
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right
                    
        memory.append(node)

    print('이진 탐색트리 구성 완료')
    
    print('       ',root.data)
    print('   ｜               ＼')
    print('  ',root.left.data, '       ',root.right.data)
    print('   ｜     ＼          ｜')
    print(root.left.left.data, root.left.right.data, '  ', root.right.right.data)

    search = input('찾을 걸그룹을 입력 : ')

    current = root
    while True:
        if search == current.data:
            print(search, '찾음')
            break
        elif search < current.data:
            if current.left == None: # 왼쪽 데이터와 비교
                print(search, '못 찾음 끝')
                break
            else:
                current = current.left
        else:
            if current.right == None: # 오른쪽 데이터와 비교
                print(search, '못 찾음 끝')
                break
            else:
                current = current.right