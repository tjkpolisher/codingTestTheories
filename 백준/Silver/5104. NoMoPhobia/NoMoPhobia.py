import sys
input = sys.stdin.readline

demerit_dict = {'TT': 75, 'TX': 50, 'PR': 80,
                'RT': 30, 'AP': 25, 'PX': 60}
while True:
    W, N = map(int, input().split())
    if W == 0 and N == 0:
        break

    students_dict = {}
    for _ in range(N):
        student, demerit = input().rstrip().split()
        if student not in students_dict:
            students_dict[student] = demerit_dict[demerit]
        else:
            students_dict[student] += demerit_dict[demerit]

    name_list = list(students_dict.keys())
    for name in students_dict.keys():
        if students_dict[name] < 100:
            name_list.remove(name)

    if not name_list:
        print(f"Week {W} No phones confiscated")
    else:
        print(f"Week {W} {','.join(name_list)}")