p, w = map(int, input().split())
message = input()
keys = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
values = [1] + [2] * 3 + [3] * 3 + [4] * 3 + [5] * 3 + [6] * 3 + [7] * 4 + [8] * 3 + [9] * 4
buttons = {keys[i]:values[i] for i in range(len(keys))}

key_button = [list(keys[0]),keys[1:4], keys[4:7], keys[7:10],
              keys[10:13], keys[13:16], keys[16:20],
              keys[20:23], keys[23:27]]
keypad = {i + 1:key_button[i] for i in range(9)}

t = 0
for i, m in enumerate(message):
    button = buttons[m]
    if i > 0 and button == buttons[message[i-1]] and button != 1:
        t += w
    idx = keypad[button].index(m)
    t += p * (idx + 1)
print(t)