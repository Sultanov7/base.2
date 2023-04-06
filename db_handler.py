import sqlite3


def login(login, passw, signal):
    con = sqlite3.connect('handler/aaapopbd')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    
    statement = f"SELECT login from users WHERE login='{login}' AND pass = '{passw}';"
    cur.execute(statement)
    if not cur.fetchone():
        signal.emit('пошел нахуй')
    else:
        signal.emit("ты принят")
    
    cur.close()
    con.close()


def register(login, passw, signal):
    con = sqlite3.connect('handler/aaapopbd')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется!')

    elif value == []:
        cur.execute(f"INSERT INTO users (login, pass) VALUES ('{login}', '{passw}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    cur.close()
    con.close()
