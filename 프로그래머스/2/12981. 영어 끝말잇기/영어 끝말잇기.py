def solution(n, words):
    previous_words = set() # 현재까지 사람들이 말한 단어들
    for i, word in enumerate(words):
        if i == 0:
            last_char = word[-1]
            previous_words.add(word)
            continue
        
        first_char = word[0]
        if last_char != first_char:  # 앞 단어의 마지막 문자와 현 단어의 첫 문자가 일치하지 않을 경우
            return [i % n + 1 , i // n + 1]
        if word in previous_words:  # 이미 나온 단어를 말했을 경우
            return [i % n + 1 , i // n + 1]
        
        last_char = word[-1]
        previous_words.add(word)
    
    return [0, 0]  # 탈락자가 생기지 않으면 [0, 0]을 리턴