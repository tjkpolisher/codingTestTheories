N = int(input())  # 스위치 개수
switches = [0] + list(map(int, input().split()))  # 스위치 상태, 인덱스 맞추기 위해 앞에 0 추가
m = int(input())  # 학생 수


def switch(n):
    return 0 if n == 1 else 1  # 스위치 상태를 반전시키는 함수


for _ in range(m):
    sex, number = map(int, input().split())
    if sex == 1:  # 남자
        # 남자는 받은 숫자의 배수에 해당하는 스위치들을 모두 반전시킨다.
        for i in range(number, N + 1, number):
            switches[i] = switch(switches[i])
    else:  # 여자
        # 여자는 자신이 받은 번호의 스위치를 먼저 반전시킨다.
        switches[number] = switch(switches[number])
        # 좌우 대칭을 검사하며 스위치를 반전시킨다.
        c1, c2 = number - 1, number + 1
        while c1 >= 1 and c2 <= N:
            if switches[c1] != switches[c2]:  # 대칭이 아니면 중단
                break
            switches[c1] = switch(switches[c1])
            switches[c2] = switch(switches[c2])
            c1 -= 1  # 왼쪽으로 한 칸 이동
            c2 += 1  # 오른쪽으로 한 칸 이동

# 스위치 상태를 20개씩 출력하기 위한 코드
switches = switches[1:]  # 인덱스 0을 제거하여 원래 스위치 리스트로 복구
for i in range(0, N, 20):
    print(*switches[i:i + 20])