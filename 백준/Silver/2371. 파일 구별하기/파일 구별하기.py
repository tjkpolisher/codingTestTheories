N = int(input())
files = []
K = 1
for _ in range(N):
    files.append(list(map(int, input().split()[:-1])))


def check_distinguishable(K):
    seen = set()
    for file in files:
        truncated_file = tuple(file[:K])
        if truncated_file in seen:
            return False
        seen.add(truncated_file)
    return True


while not check_distinguishable(K):
    K += 1

print(K)