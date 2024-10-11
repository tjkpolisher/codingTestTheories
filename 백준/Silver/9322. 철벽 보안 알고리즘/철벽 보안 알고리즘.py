T = int(input())
for _ in range(T):
    n = int(input())  # 한 문장의 단어 수
    first_key = list(input().split())  # 제1공개키
    second_key = list(input().split())  # 제2공개키
    code = list(input().split())  # 암호문

    mapping = [0] * n  # 제2공개키와 제1공개키의 인덱스 매핑
    for i in range(n):
        idx_orig = first_key.index(second_key[i])
        mapping[idx_orig] = code[i]
    print(' '.join(mapping))