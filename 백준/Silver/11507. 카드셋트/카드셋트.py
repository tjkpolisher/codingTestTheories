S = input()
card_table = {"P": set(), "K": set(), "H": set(), "T": set()}
for i in range(len(S) // 3):
    card = S[i * 3:i * 3 + 3]
    category = card[0]
    if card in card_table[category]:
        print("GRESKA")
        exit()
    card_table[category].add(card)
for category in card_table.keys():
    print(13 - len(card_table[category]), end=' ')