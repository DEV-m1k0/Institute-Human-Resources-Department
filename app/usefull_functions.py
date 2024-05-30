from create_DB import get_cursor, sq

cursor: sq.Cursor = get_cursor()

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

def get_notes_for_department() -> list[str]:
    cursor = get_cursor()

    cursor.execute("""
                    SELECT * FROM department;
                    """)
    
    departmens = []

    for row in cursor.fetchall():
        departmens.append(row[1])

    return departmens

def get_notes_for_job_title() -> list[str]:
    cursor = get_cursor()

    cursor.execute("""
                    SELECT * FROM job_title;
                    """)
    
    departmens = []

    for row in cursor.fetchall():
        departmens.append(row[1])

    return departmens


CHOICES_FOR_STATUS = ['да', 'нет']
CHOICES_FOR_ROLE = ['Администрация', 'Преподаватель', 'Технический персонал']
DEPARTMENTS: list[str] = get_notes_for_department()
JOB_TITLE = get_notes_for_job_title()