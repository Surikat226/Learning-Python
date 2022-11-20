import sqlite3

# Создаём/подключаемся к БД. Для этого используем "with", чтобы при выбрасывании каких-либо исключений подключение к
# БД прекращалось и не возникало утечек памяти
with sqlite3.connect('db1.db') as db:
    cursor = db.cursor()

    # Создаём таблицу "instruments" в нашей БД
    query1 = """ CREATE TABLE IF NOT EXISTS instruments(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name TEXT NOT NULL UNIQUE,
    quantity INTEGER,
    price INTEGER
    ) """
    cursor.execute(query1)

    # Создаём таблицу "tool_shops" в нашей БД
    query2 = """ CREATE TABLE IF NOT EXISTS tool_shops(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name TEXT NOT NULL UNIQUE
    ) """
    cursor.execute(query2)

    ### Здесь заюзал INSERT OR IGNORE, чтобы при повторном выполнении скрипта не дублировались строки. Для этого
    ### также при создании таблиц колонки "name" пометил как UNIQUE
    # Добавляем строки со значениями в таблицу "instruments"
    query3 = """ INSERT OR IGNORE INTO instruments(name, quantity, price) VALUES
    ("Молоток", 4, 600),
    ("Дрель", 10, 3500),
    ("Отвёртка крестовая", 50, 250),
    ("Набор бит", 120, 350),
    ("Набор гаечных ключей", 35, 670),
    ("Набор шестигранников", 68, 150),
    ("Рулетка лазерная", 10, 4000);
    """
    cursor.execute(query3)

    # Добавляем строки со значениями в таблицу "tool_shops"
    query4 = """ INSERT OR IGNORE INTO tool_shops(name) VALUES
    ("ДолгоСТРОЙ маркет"),
    ("Super крепёж"),
    ("PRIMA");
    """
    cursor.execute(query4)

    # Делаем выборку
    query5 = """ SELECT * FROM instruments """
    cursor.execute(query5)

    data = cursor.fetchall()  # Записываем все полученные результаты в "data", а затем выводим их построчно
    for row in data:
        print(f"id: {row[0]}")
        print(f"name: {row[1]}")
        print(f"quantity: {row[2]}")
        print(f"price: {row[3]}")
        print("\n")