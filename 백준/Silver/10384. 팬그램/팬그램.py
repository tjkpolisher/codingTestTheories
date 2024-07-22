import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    test_sentence = input().rstrip()

    is_pangram = False
    is_double = False
    is_triple = False

    test_sentence = test_sentence.lower()
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    alphabet_counter = {alphabets[i]: 0 for i in range(26)}

    for c in test_sentence:
        if c in alphabets:
            alphabet_counter[c] += 1

    counters = list(alphabet_counter.values())
    minimum_counter = min(counters)
    if minimum_counter == 3:
        is_triple = True
    elif minimum_counter == 2:
        is_double = True
    elif minimum_counter == 1:
        is_pangram = True

    if is_triple:
        print(f"Case {i}: Triple pangram!!!")
    elif is_double:
        print(f"Case {i}: Double pangram!!")
    elif is_pangram:
        print(f"Case {i}: Pangram!")
    else:
        print(f"Case {i}: Not a pangram")