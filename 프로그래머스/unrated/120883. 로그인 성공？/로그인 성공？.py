def solution(id_pw, db):
    answer = ''
    id_input, pw_input = id_pw[0], id_pw[1]
    ids = [db_[0] for db_ in db]
    pws = [db_[1] for db_ in db]
    if id_pw in db:
        answer = "login"
    elif id_input not in ids:
        answer = "fail"
    else:
        answer = "wrong pw"
    return answer