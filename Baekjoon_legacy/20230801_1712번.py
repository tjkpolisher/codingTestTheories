# 입력 변수(단위는 만원)
## A: 노트북 판매 대수와 무관한 고정 비용 지출
## B: 한 대의 노트북을 생산하는 데 들어가는 가변 비용
## C: 노트북 가격

# 출력(단위는 판매 대수)
## BEP: 손익 분기점
try:
    A, B, C = map(int, input().split())
except NameError as e:
    print("Invalid input:", e)
    raise SystemExit

try:
    if C - B <= 0:
        BEP = -1
    else:
        BEP = A // (C - B) + 1
except ZeroDivisionError as z:
    BEP = -1

print(BEP)