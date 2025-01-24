import sys
input = sys.stdin.readline


def transform_word(word):
    symbols = ['*', '?', '/', '+', '!']
    seen = set()  # 이미 등장한 문자(소문자 변환 기준)
    repeated_symbols = {}  # 중복이 처음 확인된 소문자 -> 할당된 기호
    symbol_index = 0  # 몇 번째로 중복이 발생한 문자인가(0~4)

    result = []

    for char in word:
        lower_char = char.lower()

        if lower_char not in seen:
            # 아직 등장하지 않은 문자
            seen.add(lower_char)
            result.append(char)
        else:
            # 이미 등장한(중복) 문자
            if lower_char not in repeated_symbols:
                # 이 중복 문자가 처음 등장한 경우
                # 아직 할당되지 않았다면 symbols[symbol_index]를 할당
                repeated_symbols[lower_char] = symbols[symbol_index]
                symbol_index += 1
            # 이미 할당된 기호로 대체
            result.append(repeated_symbols[lower_char])

    return ''.join(result)


while True:
    word = input().rstrip()
    if word == '#':
        break

    print(transform_word(word))