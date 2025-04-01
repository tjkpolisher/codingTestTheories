import sys
from collections import deque
input = sys.stdin.readline

key_string = input().rstrip()
cypher = input().rstrip()

key_list = list(key_string)
key_index_list = deque(list(enumerate(key_list)))
sorted_key_list = sorted(key_list)

n_row = len(cypher) // len(key_string)
cypher_table = [[0 for _ in range(len(key_string))] for i in range(n_row)]
idx = 0
for i in range(len(key_string)):
    for j in range(n_row):
        cypher_table[j][i] = cypher[idx]
        idx += 1

ans_table = [[0 for _ in range(len(key_string))] for i in range(n_row)]
for _ in range(len(key_string)):
    orig_key = key_index_list.popleft()
    orig_idx, orig_char = orig_key
    cypher_idx = sorted_key_list.index(orig_char)
    for j in range(n_row):
        ans_table[j][orig_idx] = cypher_table[j][cypher_idx]
    sorted_key_list[cypher_idx] = 0  # 중복 문자 처리

for i in range(n_row):
    print(''.join(ans_table[i]), end='')