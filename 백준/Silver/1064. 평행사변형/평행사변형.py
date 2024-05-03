def incline_and_bias(x1, y1, x2, y2):
    # 두 점을 지나는 직선의 기울기를 구하는 함수
    if x1 == x2:
        incline = 0
    elif y1 == y2:
        incline = float('inf')
    else:
        incline = (y2 - y1) / (x2 - x1)
    return incline


def total_length(l1, l2):
    return 2 * (l1 + l2)


x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
i_ab = incline_and_bias(x_a, y_a, x_b, y_b)
i_bc = incline_and_bias(x_b, y_b, x_c, y_c)
i_ca = incline_and_bias(x_c, y_c, x_a, y_a)
if i_ab == i_bc == i_ca:
    print(-1.0)
else:
    l_ab = ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** 0.5
    l_bc = ((x_c - x_b) ** 2 + (y_c - y_b) ** 2) ** 0.5
    l_ca = ((x_a - x_c) ** 2 + (y_a - y_c) ** 2) ** 0.5

    lengths = [total_length(l_ab, l_bc),
               total_length(l_bc, l_ca),
               total_length(l_ca, l_ab)]
    print(max(lengths) - min(lengths))