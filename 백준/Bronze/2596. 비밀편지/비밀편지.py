n = int(input())
message = input()
answer = ''
code_table = {'000000':'A', '001111':'B', '010011':'C', '011100':'D',
              '100110':'E', '101001':'F', '110101':'G', '111010':'H'}
for i in range(n):
    char = message[6 * i: 6 * (i + 1)]
    if char in code_table.keys():
        answer += code_table[char]
    else:
        for code in code_table.keys():
            counter = 0 # 틀린 글자의 개수 (2개 이상이면 루프 탈출 후 위치 출력)
            for j, c in enumerate(char):
                if code[j] != c:
                    counter += 1
            if counter == 1:
                answer += code_table[code]
                break
        if counter >= 2:
            answer = i + 1
            break
print(answer)