import sys
input = sys.stdin.readline

N = int(input())
# opcode를 기계어 비트로 변환하는 딕셔너리
opcode_table = {'ADD': '0000', 'SUB': '0001', 'MOV': '0010', 'AND': '0011',
                'OR': '0100', 'NOT': '0101', 'MULT': '0110', 'LSFTL': '0111',
                'LSFTR': '1000', 'ASFTR': '1001', 'RL': '1010', 'RR': '1011'}

for _ in range(N):
    opcode, rD, r1, r2 = input().rstrip().split()
    rD = int(rD)
    rA = int(r1)
    if opcode[-1] == 'C':
        C = int(r2)
    else:
        rB = int(r2)

    ans = []
    # opcode 변환
    if opcode[-1] == 'C':
        ans.append(opcode_table[opcode[:-1]])
        ans.append('1')
    else:
        ans.append(opcode_table[opcode])
        ans.append('0')

    # 5번 비트는 항상 0
    ans.append('0')

    # rD 변환
    rD = bin(rD)[2:]
    if len(rD) < 3:
        rD = '0' * (3 - len(rD)) + rD
    ans.append(rD)
    # rA 변환
    if opcode[:3] == 'MOV' or opcode[:3] == 'NOT':
        rA = '000'
    else:
        rA = bin(rA)[2:]
        if len(rA) < 3:
            rA = '0' * (3 - len(rA)) + rA
    ans.append(rA)

    # rB, #C 변환
    if opcode[-1] == 'C':
        C = bin(C)[2:]
        if len(C) < 4:
            C = '0' * (4 - len(C)) + C
        ans.append(C)
    else:
        rB = bin(rB)[2:]
        if len(rB) < 3:
            rB = '0' * (3 - len(rB)) + rB
        ans.append(rB)
        ans.append('0')

    # 병합 후 출력
    print(''.join(ans))