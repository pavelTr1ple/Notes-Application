import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.initialize_database()

    def initialize_database(self):
        """Инициализация базы данных и создание таблицы заметок, если она не существует."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при работе с SQLite: {e}")
        finally:
            if self.conn:
                self.conn.close()

    def add_note(self, title, content):
        """Добавление новой заметки в базу данных."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении заметки: {e}")
        finally:
            if self.conn:
                self.conn.close()

    def get_all_notes(self):
        """Получение списка всех заметок."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            cursor.execute('SELECT id, title, content FROM notes')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при получении списка заметок: {e}")
            return []
        finally:
            if self.conn:
                self.conn.close()

    def search_notes(self, keyword):
        """Поиск заметок по ключевому слову."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            query = f"SELECT id, title, content FROM notes WHERE title LIKE '%{keyword}%' OR content LIKE '%{keyword}%'"
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при поиске заметок: {e}")
            return []
        finally:
            if self.conn:
                self.conn.close()

    def delete_note(self, note_id):
        """Удаление заметки по идентификатору."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при удалении заметки: {e}")
        finally:
            if self.conn:
                self.conn.close()
