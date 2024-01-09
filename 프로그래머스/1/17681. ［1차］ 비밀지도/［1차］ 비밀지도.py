def solution(n, arr1, arr2):
    arr1_bin = [bin(n1)[2:] for n1 in arr1]
    arr2_bin = [bin(n2)[2:] for n2 in arr2]
    
    arr_bin = [combine(arr1_bin[i], arr2_bin[i], n) for i in range(n)]
    return arr_bin

def combine(s1, s2, n):
    result = ''
    s1 = '0' * (n - len(s1)) + s1
    s2 = '0' * (n - len(s2)) + s2
    for i in range(n):
        if s1[i] == '0' and s2[i] == '0':
            result += ' '
        else:
            result += '#'
    return result