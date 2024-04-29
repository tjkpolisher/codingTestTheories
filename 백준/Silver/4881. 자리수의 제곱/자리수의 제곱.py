def num_square_sum(n):
    n_list = [n]
    while n_list.count(n_list[-1]) < 2:
        cal = n_list[-1]
        new_num = 0
        for i in str(cal):
            new_num += int(i) ** 2
        n_list.append(new_num)
    return n_list


def backtracking(list1, list2):
    minimum_num = 0
    for i in list1:
        if i in list2:
            minimum_num = list1.index(i) + list2.index(i) + 2
    for j in list2:
        if j in list1 and minimum_num > list1.index(j) + list2.index(j) + 2:
            minimum_num = list1.index(j) + list2.index(j) + 2

    return minimum_num


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        list1 = num_square_sum(A)
        list2 = num_square_sum(B)
        print(A, B, backtracking(list1, list2))