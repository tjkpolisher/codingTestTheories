N = int(input())
grades = []
for _ in range(N):
    grades.append(int(input()))

grades.sort(reverse=True)

while len(grades) > 1:
    a = grades.pop()
    b = grades.pop()
    grades.append((a + b) / 2)

print(f"{grades[0]:.6f}")