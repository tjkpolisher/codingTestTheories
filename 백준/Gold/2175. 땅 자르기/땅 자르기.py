def middle(dot1, dot2):
    # 두 꼭지점의 중점을 계산하는 함수
    return [(dot1[0] + dot2[0]) / 2, (dot1[1] + dot2[1]) / 2]


def t_area(dot1, dot2, dot3):
    # 분할된 삼각형의 각 넓이를 계산하는 함수
    return abs(((dot2[0] - dot1[0]) * (dot3[1] - dot1[1]) - (dot3[0] - dot1[0]) * (dot2[1] - dot1[1])) / 2)


arr = list(map(int, input().split()))
vertex = []
for i in range(4):
    vertex.append([arr[2 * i], arr[2 * i + 1]])

vertex_with_middle = [0] * 8
for i in range(8):
    if i % 2 == 0:
        vertex_with_middle[i] = vertex[i // 2]
    else:
        vertex_with_middle[i] = middle(vertex[i // 2], vertex[(i // 2 + 1) % 4])

left_half, right_half = 0, 10 ** 9
# 8개의 점에 대하여 반복
for i in range(8):
    target_dots = []
    if i % 2 == 0:  # 꼭짓점인 경우
        for j in range(2, 7):
            target_dots.append((i + j) % 8)
        triangles = []
        for k in range(4):
            triangles.append(t_area(vertex_with_middle[i],
                                    vertex_with_middle[target_dots[k]],
                                    vertex_with_middle[target_dots[k + 1]]))
        # 기존의 값보다 나눈 넓이의 차이가 작으면 기존 값과 교환
        for l in range(3):
            x = sum(triangles[:l + 1])
            y = sum(triangles[l + 1:])
            if abs(x - y) < abs(left_half - right_half):
                left_half, right_half = x, y
    else:  # 중점인 경우
        for j in range(1, 8):
            target_dots.append((i + j) % 8)
        triangles = []
        for k in range(6):
            triangles.append(t_area(vertex_with_middle[i],
                                    vertex_with_middle[target_dots[k]],
                                    vertex_with_middle[target_dots[k + 1]]))
        for l in range(5):
            x = sum(triangles[:l + 1])
            y = sum(triangles[l + 1:])
            if abs(x - y) < abs(left_half - right_half):
                left_half, right_half = x, y

left_half, right_half = round(left_half, 3), round(right_half, 3)

if left_half > right_half:
    left_half, right_half = right_half, left_half

print(left_half, right_half)