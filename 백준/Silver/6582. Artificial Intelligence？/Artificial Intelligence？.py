import sys
input = sys.stdin.readline


def extract_value(unit):
    prefix_table = {'m': 1e-3, 'k': 1e3, 'M': 1e6}
    if unit[-1] in (',', '.'):
        unit = unit[:-1]
    if unit[-2] in ('m', 'k', 'M'):
        value = float(unit[:-2]) * prefix_table[unit[-2]]
    else:
        value = float(unit[:-1])
    return value


T = int(input())
for i in range(T):
    test_case = list(input().rstrip().split())
    field1, field2 = None, None
    for word in test_case:
        if not field1 and "=" in word:
            field1 = word
        if field1 and '=' in word:
            field2 = word

    concept1, unit1 = field1.split('=')
    concept2, unit2 = field2.split('=')
    value1 = extract_value(unit1)
    value2 = extract_value(unit2)

    power, voltage, current = None, None, None

    for concept, value in zip((concept1, concept2), (value1, value2)):
        if concept == 'P':
            power = value
        elif concept == 'U':
            voltage = value
        else:
            current = value

    if not power:
        ans1 = 'P'
        ans2 = voltage * current
        ans3 = 'W'
    elif not voltage:
        ans1 = 'U'
        ans2 = power / current
        ans3 = 'V'
    else:
        ans1 = 'I'
        ans2 = power / voltage
        ans3 = 'A'

    print(f"Problem #{i + 1}")
    print(f"{ans1}={ans2:.2f}{ans3}")
    if i != T - 1:
        print()