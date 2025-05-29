import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
pointers = {}
ref_count = {}

for i in range(1, M + 1):
    obj = int(input())
    pointers[i] = obj
    if obj > 0:
        ref_count[obj] = ref_count.get(obj, 0) + 1

for _ in range(Q):
    operation = input().rstrip()
    if operation.startswith("reset"):
        _, x = operation.split()
        x = int(x)

        old_obj = pointers[x]
        if old_obj > 0:
            ref_count[old_obj] -= 1
        pointers[x] = 0
    else:
        op, x, y = operation.split()
        x, y = int(x), int(y)
        if op == "assign":
            old_obj = pointers[x]
            new_obj = pointers[y]
            if old_obj > 0:
                ref_count[old_obj] -= 1
            if new_obj > 0:
                ref_count[new_obj] = ref_count.get(new_obj, 0) + 1
            pointers[x] = new_obj
        else:
            pointers[x], pointers[y] = pointers[y], pointers[x]

alive_objects = sorted([obj for obj, count in ref_count.items() if count > 0])
print(len(alive_objects))
if alive_objects:
    for obj in alive_objects:
        print(obj)