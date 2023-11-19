import bcrypt
import sqlite3
conn = sqlite3.connect('last.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS users(
#                     id INTEGER PRIMARY KEY,
#                     email TEXT,
#                     password TEXT
#
# )
#
#
# ''')
class DataBaseManager:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    def AddUser(self,email,password):
        hashedpas = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        conn.execute('''
        INSERT INTO users(email,password) VALUES(?, ?)
        
        ''',(email,hashedpas))
        cursor.execute('SELECT * FROM users')
        existus = cursor.fetchone()
        if existus:
            print("Пользователь уже есть")
            conn.close()
        else:
            row = cursor.fetchall()
            for rows in row:
                print(rows)
            conn.commit()
            conn.close()
    def DeliteUser(self,acceskey):
        conn = sqlite3.connect('last.db')
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM users WHERE id = ?
        
        ''',(acceskey,))
        conn.commit()
        conn.close()

    def ShowDan(self):
        cursor.execute('SELECT * FROM users')
        row = cursor.fetchall()
        for i in row:
            print(i)
    def Aut(self,email,password):
        conn = sqlite3.connect('last.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM users WHERE email = ?
        
        ''',(email,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            hashed_password = user_data[2]
            if bcrypt.checkpw(password.encode(),hashed_password):
                print("Пользователь аутифицирован")
                return True
            else:
                print('Нет аута')
                return False

        else:
            print('Пользователь не найден')
            return False
def Menu():
    print('Выберите действие 1 - Добавть 2 - удалить 3 - показать')
    var = int(input())
    dbm = DataBaseManager(0,0)
    if var == 1:
        email = input()
        password = input()
        dbm.AddUser(email,password)
    elif var == 2:
        print("Выберете айди")
        v = int(input())
        dbm.DeliteUser(v)
    elif var == 3:
        dbm.ShowDan()
    elif var == 4:
        email = input()
        password = input()
        if dbm.Aut(email,password):
            print("Все ок")
        else:
            print('Все плохо')


def Krh():
    dbm =DataBaseManager(0,0)
    print("Введите данные")
    v = input()
    r = input()
    if dbm.Aut(v,r):
        Menu()
    else:
        print("Неправильные данные")

Krh()