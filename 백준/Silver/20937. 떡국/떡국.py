from collections import Counter

N = int(input())
plates = list(map(int, input().split()))
counter_plates = Counter(plates)
print(max(counter_plates.values()))