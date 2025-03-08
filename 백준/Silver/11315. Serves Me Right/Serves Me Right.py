import sys
input = sys.stdin.readline

T = int(input())


def session_logout(t1, t2, TO):
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))

    return True if h1 * 60 + m1 + TO <= h2 * 60 + m2 else False


for _ in range(T):
    E, TO = map(int, input().split())
    user_table = {}
    max_users = 0
    unique_users = set()

    for i in range(E):
        log = input().rstrip()
        if log.endswith("RESTART"):
            user_table = {}
        else:
            TIME, _, USER, hUSER_ACTIONi = log.split()
            unique_users.add(USER)
            if user_table:
                names = list(user_table.keys())
                for name in names:
                    if session_logout(user_table[name], TIME, TO):
                        user_table.pop(name, None)

            if hUSER_ACTIONi == "LOG_IN":
                user_table[USER] = TIME
            elif hUSER_ACTIONi == "LOG_OUT":
                user_table.pop(USER, None)
            max_users = max(max_users, len(user_table))

    print(len(unique_users), max_users)