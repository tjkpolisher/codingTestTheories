class Node:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key


class BST:
    def __init__(self):
        # 루트 노드를 None으로 초기화. 즉, 아무 노드도 없는 상태
        self.root = None

    def insert(self, key):
        # 루트 노드가 없는 경우 새 노드를 루트로 추가
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while True:
                # 삽입할 값이 현재 노드의 값보다 작으면 왼쪽 자식 노드로 이동
                if key < curr.val:
                    if curr.left:
                        curr = curr.left
                    # 현재 노드의 왼쪽 자식 노드가 없는 경우 새 노드 추가
                    else:
                        curr.left = Node(key)
                        break
                else:
                    # 삽입하려는 값이 현재 노드의 값보다 클 경우 오른쪽 자식 노드로 이동
                    if curr.right:
                        curr = curr.right
                    else:
                        # 현재 노드의 오른쪽 자식 노드가 없는 경우 새 노드 추가
                        curr.right = Node(key)
                        break

    def search(self, key):
        # 루트 노드부터 시작해 이진 탐색 규칙에 따라 특정값이 있는지 확인
        curr = self.root
        while curr and curr.val != key:
            # 찾으려는 값이 현재 노드의 값보다 작으면 왼쪽 자식 노드로 이동
            if key < curr.val:
                curr = curr.left
            # 찾으려는 값이 현재 노드의 값보다 크면 오른쪽 자식 노드로 이동
            else:
                curr = curr.right
        return curr


def solution(lst, search_lst):
    answer = []
    bst = BST()
    # 리스트의 각 요소를 이용해 이진 탐색 트리 생성
    for key in lst:
        bst.insert(key)

    # 검색 리스트의 각 요소를 이진 탐색 트리에서 검색하고, 검색 결과를 리스트에 추가
    for search_val in search_lst:
        if bst.search(search_val):
            answer.append(True)
        else:
            answer.append(False)

    return answer


if __name__ == "__main__":
    ex1 = [[5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]]
    ex2 = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]

    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))
