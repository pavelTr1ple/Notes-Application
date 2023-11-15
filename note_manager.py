from database_manager import DatabaseManager
from utils import format_note_display


class NoteManager:
    def __init__(self, db_path):
        self.db_manager = DatabaseManager(db_path)

    def create_note(self, title, content):
        """Создание новой заметки."""
        self.db_manager.add_note(title, content)
        print("Заметка успешно создана.")

    def display_notes(self):
        """Отображение списка всех заметок."""
        notes = self.db_manager.get_all_notes()
        if not notes:
            print("Заметки отсутствуют.")
            return
        for note in notes:
            print(format_note_display(note))

    def search_note(self, keyword):
        """Поиск заметок по ключевому слову."""
        notes = self.db_manager.search_notes(keyword)
        if not notes:
            print("Заметки не найдены.")
            return
        for note in notes:
            print(f"ID: {note[0]}, Заголовок: {note[1]}, Содержание: {note[2]}")

    def remove_note(self, note_id):
        """Удаление заметки по идентификатору."""
        self.db_manager.delete_note(note_id)
        print("Заметка удалена.")
