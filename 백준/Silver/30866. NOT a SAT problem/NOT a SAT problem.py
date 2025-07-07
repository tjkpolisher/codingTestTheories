N, M = map(int, input().split())
clauses = []
for _ in range(M):
    line = list(map(int, input().split()))
    clauses.append(line[1:])

assignment = [0] * (N + 1)

for clause in clauses:
    used_vars = []
    can_make_false = True

    for literal in clause:
        var = abs(literal)
        needed_value = -1 if literal > 0 else 1

        if assignment[var] == 0:
            assignment[var] = needed_value
            used_vars.append(var)
        elif assignment[var] != needed_value:
            can_make_false = False
            break

    if can_make_false:
        for i in range(1, N + 1):
            if assignment[i] == 0:
                assignment[i] = 1

        print("YES")
        print(*[1 if assignment[i] == 1 else 0 for i in range(1, N + 1)])
        exit()

    for var in used_vars:
        assignment[var] = 0

print("NO")