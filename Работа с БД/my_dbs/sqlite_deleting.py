import sqlite3

# Создаём/подключаемся к БД. Для этого используем "with", чтобы при выбрасывании каких-либо исключений подключение к
# БД прекращалось и не возникало утечек памяти
with sqlite3.connect('my_dbs/db1.db') as db:
    cursor = db.cursor()

    query1 = """ DROP TABLE instruments """
    cursor.execute(query1)