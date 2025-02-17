import sys
input = sys.stdin.readline

N = int(input())
word = list(input().rstrip() for _ in range(N))
M = int(input())
S = input().rstrip()


def key_generator(word):
    key = word

    if len(word) > 2:
        key = "-".join([word[0], word[-1], "".join(sorted(word[1:-1]))])
    elif len(word) == 2:
        key = "-".join(list(word))

    return key


def word_matching_dict(word_list):
    matching_dict = {}
    for word in word_list:
        key = key_generator(word)
        matching_dict[key] = word
    return matching_dict


def word_superiority_effect(word_list, S):
    matching_dict = word_matching_dict(word_list)
    word_S_list = S.split()
    answer = []
    for word in word_S_list:
        key = key_generator(word)
        answer.append(matching_dict.get(key, word))
    return " ".join(answer)


print(word_superiority_effect(word, S))