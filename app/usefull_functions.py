from create_DB import CreateDataBase, sq

db = CreateDataBase()
cursor: sq.Cursor = db.get_cursor()

def get_all_users() -> list[tuple]:
    cursor.execute("""
        SELECT * FROM employees;
    """)

    notes = cursor.fetchall()
    return notes


def sorting_users_by_status_pre_retirment(sort_by: str, notes: list[tuple] = None) -> list[tuple]:
    accepted_users = []

    if notes is None:
        notes = get_all_users()

    for user in notes:

        note = {
            'Предпенсионный возраст': user[11],
            'Бездетные': user[12],
            'Многодетные': user[13],
            'Ветераны': user[14]
        }[sort_by]

        if note == 'да':
            accepted_users.append(user)

    return accepted_users