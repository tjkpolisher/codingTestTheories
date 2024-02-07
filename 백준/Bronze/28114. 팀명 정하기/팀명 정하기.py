p1, y1, s1 = input().split()
p2, y2, s2 = input().split()
p3, y3, s3 = input().split()
p = list(map(int, list([p1, p2, p3])))
y = list(map(int, list([y1, y2, y3])))
s = [s1, s2, s3]

name1_list = sorted([str(y_ % 100) for y_ in y])
name1 = ''.join(name1_list)

name2_list = [[p[i], s[i][0]] for i in range(3)]
name2_list.sort(reverse=True, key = lambda x: x[0])
n2_list = [str(name2_list[i][1]) for i in range(3)]
name2 = ''.join(n2_list)
print(name1)
print(name2)