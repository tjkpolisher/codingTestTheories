problem_table = {}
penalty = 0
correct = 0

while True:
    log = input()
    if log == "-1":
        break
    m, name, result = log.split()
    m = int(m)
    if name not in problem_table:
        problem_table[name] = [m]
    else:
        problem_table[name].append(m)
    
    if result == 'right':
        penalty += (m + 20 * len(problem_table[name][:-1]))
        correct += 1

print(correct, penalty)