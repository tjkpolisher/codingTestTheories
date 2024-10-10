import sys
input = sys.stdin.readline

string = input().rstrip()
characters = []

flags = [False] * 4  # U, C, P, C가 입력되었는지를 나타내는 플래그
for i in range(len(string)):
    if string[i] == 'U' and not flags[0]:
        characters.append(string[i])
        flags[0] = True
    elif string[i] == 'C' and (flags[0] and not flags[1]):
        characters.append(string[i])
        flags[1] = True
    elif string[i] == 'P' and (flags[0] and flags[1] and not flags[2]):
        characters.append(string[i])
        flags[2] = True
    elif string[i] == 'C' and (flags[0] and flags[1] and flags[2] and not flags[3]):
        characters.append(string[i])
        flags[3] = True

ans = ''.join(characters)
if ans == 'UCPC':
    print("I love UCPC")
else:
    print("I hate UCPC")