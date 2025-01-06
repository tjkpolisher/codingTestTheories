import sys
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]


def rotate(window):
    return [''.join(row) for row in zip(*window[::-1])]


def all_rotate(window):
    forms = [window]
    for _ in range(3):
        forms.append(rotate(forms[-1]))
    return forms


def normalize_window(window):
    return min(all_rotate(window))


def extract_windows(grid, r, c):
    windows = []
    i = 1
    while i < r - 1:
        j = 1
        while j < c - 1:
            height = 0
            while i + height < r - 1 and grid[i + height][j] != '#':
                height += 1

            width = 0
            while j + width < c - 1 and grid[i][j + width] != '#':
                width += 1

            window = [grid[i + h][j:j + width] for h in range(height)]
            windows.append(window)
            j += (width + 1)
        i += (height + 1)
    return windows


windows = extract_windows(grid, r, c)
unique_windows = set()
for window in windows:
    normalized = normalize_window(window)
    window_str = '\n'.join(normalized)
    unique_windows.add(window_str)

print(len(unique_windows))