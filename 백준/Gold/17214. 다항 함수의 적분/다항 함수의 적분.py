import sys
input = sys.stdin.readline

polynomial = input().rstrip()  # 다항식(최대 1차식)

if polynomial == "0":
    print("W")
    exit()

terms = []

if polynomial.startswith('-'):
    terms.append('-')
    polynomial = polynomial[1:]

for i in range(len(polynomial)):
    if polynomial[i] in ('+', '-'):
        terms.append(polynomial[:i])  # 연산자 이전까지의 항
        terms.append(polynomial[i])  # 연산자
        terms.append(polynomial[i+1:])  # 연산자 다음 항
        break
else:
    terms.append(polynomial)

ans = []
for term in terms:
    # 연산자일 때
    if term in ('+', '-'):
        ans.append(term)
    # 일차항일 때
    elif term.endswith('x'):
        coeff = int(term[:-1])  # 계수
        if coeff == 2:
            ans.append('xx')
        else:
            ans.append(f'{coeff // 2}xx')
    # 0일 때
    elif term == '0':
        continue
    # 상수항일 때
    else:
        if int(term) == 1:
            ans.append('x')
        else:
            ans.append(f"{term}x")

ans.append('+W')
print(''.join(ans))