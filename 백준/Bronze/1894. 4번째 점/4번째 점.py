while True:
    try:
        locations = list(map(float, input().split()))
        temps = [list(locations[2 * i: 2 * (i + 1)]) for i in range(4)]
        for temp in temps:
            if temps.count(temp) != 1:
                adjacent = temp
                break
        
        dots = [temp for temp in temps if temp != adjacent]
        
        dot1, dot2 = dots[0], dots[1]
        delta_x, delta_y = dot2[0] - adjacent[0], dot2[1] - adjacent[1]
        incline = delta_y / delta_x
        x4, y4 = round(dot1[0] + delta_x, 3), round(dot1[1] + delta_y, 3)
        print(f"{x4:.3f} {y4:.3f}")
    except EOFError:
        break