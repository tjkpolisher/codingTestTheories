S = input()


def flag_check(flag):
    return not flag


tag_flag = False
length = len(S)
word_list = []  # 태그가 아닌 단어의 문자를 담을 리스트
for i, ch in enumerate(S):
    if ch in ('<', '>'):
        # 태그가 시작되거나 끝나면 플래그를 변환하고 태그 문자 출력
        tag_flag = flag_check(tag_flag)
        while word_list:
            print(word_list.pop(), end='')
        print(ch, end='')
    elif tag_flag:
        # 태그 안의 문자는 모두 그대로 출력
        print(ch, end='')
    else:
        if ch == ' ':
            # 공백 문자가 나오면 현재 word_list에 있는 문자를 모두 pop해서 출력
            while word_list:
                print(word_list.pop(), end='')
            print(' ', end='')
        else:
            # 그 외의 문자는 일단 word_list에 저장
            word_list.append(ch)
    if i == length - 1:
        # 마지막 문자까지 순회하면 word_list에 있는 문자를 모두 pop해서 출력
        while word_list:
            print(word_list.pop(), end='')