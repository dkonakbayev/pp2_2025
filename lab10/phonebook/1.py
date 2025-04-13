import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="12345",   
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Создание таблицы (если ещё не создана)
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
""")
conn.commit()

# Добавление вручную
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Контакт добавлен.\n")

# Загрузка из CSV
def insert_from_csv():
    filename = input("Введите путь к CSV-файлу: ")
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # пропустить заголовок
            for row in reader:
                if len(row) >= 2:
                    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("Данные из CSV добавлены.\n")
    except FileNotFoundError:
        print("Файл не найден.\n")

# Обновление данных
def update_contact():
    name = input("Введите имя контакта для обновления: ")
    new_name = input("Новое имя (оставь пустым, если не менять): ")
    new_phone = input("Новый телефон (оставь пустым, если не менять): ")

    if new_name:
        cur.execute("UPDATE contacts SET name = %s WHERE name = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE contacts SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Контакт обновлён.\n")

# Поиск
def search_contacts():
    keyword = input("Введите имя или телефон для поиска: ")
    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s OR phone ILIKE %s", (f'%{keyword}%', f'%{keyword}%'))
    results = cur.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Контакт не найден.")
    print()

# Удаление
def delete_contact():
    value = input("Введите имя или телефон для удаления: ")
    cur.execute("DELETE FROM contacts WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    print("Контакт удалён (если существовал).\n")

# Показать все
def show_all():
    cur.execute("SELECT * FROM contacts")
    results = cur.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Телефонная книга пуста.")
    print()

# Главное меню
def menu():
    while True:
        print("📞 PhoneBook Меню:")
        print("1. Добавить контакт вручную")
        print("2. Загрузить контакты из CSV")
        print("3. Обновить контакт")
        print("4. Найти контакт")
        print("5. Удалить контакт")
        print("6. Показать все контакты")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            show_all()
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуй ещё раз.\n")

    # Закрываем соединение
    cur.close()
    conn.close()
    print("До свидания!")

# Запуск
if __name__ == "__main__":
    menu()
