def solution(string_list, query_list):
    p = 31
    m = 1000000007
    result = []
    string_hash = [hash_function(w, p, m) for w in string_list]
    for query in query_list:
        query_hash = hash_function(query, p, m)
        if query_hash in string_hash:
            result.append(True)
        else:
            result.append(False)
    
    return result


def hash_function(w, p, m):
    result = 0
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for i, c in enumerate(w):
        result += ((alphabet.index(c) + 1) % m) * (p ** i)
    result %= m
    return result


if __name__ == "__main__":
    ex1 = [["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]]
    print(solution(ex1[0], ex1[1]))
