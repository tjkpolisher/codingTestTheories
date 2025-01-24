from itertools import product

def solution(word):
    answer = 0
    alphabets = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        products = product(alphabets, repeat=i)
        for pro in products:
            words.append(''.join(list(pro)))
    
    words.sort()
    return words.index(word) + 1