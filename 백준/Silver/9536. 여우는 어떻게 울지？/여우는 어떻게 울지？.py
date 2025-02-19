import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    recorded_sound = input().rstrip().split()
    unique_sounds = set()

    while True:
        line = input().rstrip()
        if line == "what does the fox say?":
            break
        _, _, sound = line.split()
        unique_sounds.add(sound)

    result = [sound for sound in recorded_sound if sound not in unique_sounds]
    print(' '.join(result))