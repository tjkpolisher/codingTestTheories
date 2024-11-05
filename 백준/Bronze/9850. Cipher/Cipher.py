ciphertext = input()

p = 1
while True:
    ans = []
    for c in ciphertext:
        num = ord(c)
        if 65 <= num < 92:
            num -= p
            if num < 65:
                num += 26
            new_c = chr(num)
            ans.append(new_c)
        else:
            ans.append(c)
    ans_string = ''.join(ans)
    if 'CHIPMUNKS' in ans_string and 'LIVE' in ans_string:
        break
    p += 1

print(ans_string)