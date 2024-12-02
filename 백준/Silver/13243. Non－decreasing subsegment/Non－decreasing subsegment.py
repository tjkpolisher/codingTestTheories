n = int(input())
integers = list(map(int, input().split()))

segment_len = 0  # 부분 수열의 크기
segment_sum = 0  # 부분 수열의 합
temp_len = 1
temp_sum = integers[0]

for i in range(1, n):
    if integers[i - 1] <= integers[i]:
        temp_len += 1
        temp_sum += integers[i]
    else:
        if segment_len < temp_len:
            segment_len = temp_len
            segment_sum = temp_sum
        temp_sum = integers[i]
        temp_len = 1

if temp_len > segment_len:
    segment_len = temp_len
    segment_sum = temp_sum

print(segment_len, segment_sum)