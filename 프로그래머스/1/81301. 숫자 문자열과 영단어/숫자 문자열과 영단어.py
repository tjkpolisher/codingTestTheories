def solution(s):
    table_keys = ['zero', 'one', 'two', 'three',
                  'four', 'five', 'six', 'seven',
                  'eight', 'nine']
    table_values = [str(i) for i in range(10)]
    table = {table_keys[i]:table_values[i] for i in range(10)}
    answer = ''
    word = ''
    for i, c in enumerate(s):
        if c.islower():
            word += c
            if word in table_keys:
                answer += table[word]
                word = ''
        else:
            answer += c         
            
    return int(answer)