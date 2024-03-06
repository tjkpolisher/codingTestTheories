def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] >= target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


if __name__ == "__main__":
    # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
    n, target = 10, 7
    # 전체 원소 입력받기
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # array = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19] # 원소가 존재하지 않는 예시

    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n - 1)
    if not result:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)
