from math import ceil
while True:
    number = input()
    
    if number == "0":
        break
    
    if len(number) % 2 == 1: # 자릿수가 홀수일 때
        front = number[:int(len(number)/2)]
        rear = number[ceil(len(number)/2):][::-1]
    else: # 자릿수가 짝수일 때
        front = number[:int(len(number)/2)]
        rear = number[int(len(number)/2):][::-1]
    
    if front == rear:
        print('yes')
    else:
        print('no')