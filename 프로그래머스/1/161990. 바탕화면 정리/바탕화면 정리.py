def solution(wallpaper):
    x = []
    y = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(j)
                y.append(i)
    
    lux = min(x)
    rdx = max(x)
    luy = min(y)
    rdy = max(y)
    return [luy, lux, rdy + 1, rdx + 1]