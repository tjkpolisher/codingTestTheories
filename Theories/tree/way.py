# 문제 출처: 2019 KAKAO BLIND RECRUITMENT - 길 찾기 게임
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42892


# Node 클래스 정의
class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right
        self.num = num

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


# 이진 트리 생성 함수
def make_BT(nodeinfo):
    # 노드 번호 리스트 생성
    nodes = [i for i in range(1, len(nodeinfo) + 1)]
    nodes.sort(key=lambda x: (nodeinfo[x - 1][1], -nodeinfo[x - 1][0]),
               reverse=True)
    root = None
    for i in range(len(nodes)):
        if not root:
            root = Node(nodeinfo[nodes[0] - 1], nodes[0])
        else:
            parent = root
            node = Node(nodeinfo[nodes[i] - 1], nodes[i])

            while True:
                # 부모 노드의 x좌표가 더 크면 왼쪽으로
                if node.info[0] < parent.info[0]:
                    if parent.has_left():
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                # 부모 노드의 x좌표가 더 작거나 같으면 오른쪽으로
                else:
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = node
                    break
    return root


# 전위 순회 함수
def pre_order(root, answer):
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        answer[0].append(node.num)
        stack.append(node.right)
        stack.append(node.left)


# 후위 순회 함수
def post_order(root, answer):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            answer[1].append(node.num)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))


# 주어진 좌표 정보를 이용해 이진 트리를 만들고, 전위 순회와 후위 순회한 결과 반환
def solution(nodeinfo):
    answer = [[], []]  # 결과를 저장할 리스트
    root = make_BT(nodeinfo)  # 이진 트리 생성
    pre_order(root, answer)  # 전위 순회
    post_order(root, answer)  # 후위 순회
    return answer


if __name__ == "__main__":
    ex1 = [[5, 3], [11, 5], [13, 3], [3, 5],
           [6, 1], [1, 3], [8, 6], [7, 2],
           [2, 2]]
    print(solution(ex1))
