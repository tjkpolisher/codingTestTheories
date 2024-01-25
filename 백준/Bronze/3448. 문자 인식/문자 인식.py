import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    sentence = ''
    
    while True:
        line = input()
        if line == '\n':
            break
        sentence += line.rstrip('\n')
    
    A = len(sentence)
    R = A - sentence.count("#")
    p = round(R / A * 100, 1)
    
    if str(p).split('.')[1] == '0':
        answer = f"Efficiency ratio is {int(p):d}%."
    else:
        answer = f"Efficiency ratio is {p:.1f}%."
    
    print(answer)