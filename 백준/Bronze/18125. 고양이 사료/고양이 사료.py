import sys
input = sys.stdin.readline

string1 = '''|>___/|     /}
| O O |    / }
( =0= )""""  \\
| ^  ____    |
|_|_/    ||__|
'''
string2 = '''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|
'''

R, C = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(C)]
students = [list(map(int, input().split())) for _ in range(R)]

picture_T = list(map(list, zip(*picture)))
for i in range(R):
    picture_T[i].reverse()

for i in range(R):
    for j in range(C):
        if picture_T[i][j] and not students[i][j]:
            print(string1, end='')
            exit()
else:
    print(string2, end='')