from note_manager import NoteManager
from utils import validate_input


class UIManager:
    def __init__(self, db_path):
        self.note_manager = NoteManager(db_path)

    def main_menu(self):
        """Главное меню приложения."""
        while True:
            print("\nМенеджер Заметок")
            print("1. Создать заметку")
            print("2. Показать все заметки")
            print("3. Найти заметку")
            print("4. Удалить заметку")
            print("5. Выйти")
            choice = input("Выберите опцию: ")

            if choice == "1":
                self.create_note_ui()
            elif choice == "2":
                self.note_manager.display_notes()
            elif choice == "3":
                self.search_note_ui()
            elif choice == "4":
                self.remove_note_ui()
            elif choice == "5":
                break
            else:
                print("Неверный ввод, попробуйте ещё раз.")

    def create_note_ui(self):
        """Интерфейс для создания новой заметки."""
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержание заметки: ")
        self.note_manager.create_note(title, content)

    def search_note_ui(self):
        """Интерфейс для поиска заметок."""
        keyword = input("Введите ключевое слово для поиска: ")
        self.note_manager.search_note(keyword)

    def remove_note_ui(self):
        """Интерфейс для удаления заметки."""
        note_id = input("Введите ID заметки для удаления: ")
        note_id = validate_input(note_id, int)
        if note_id is not None:
            self.note_manager.remove_note(note_id)


if __name__ == "__main__":
    ui_manager = UIManager("notes.db")
    ui_manager.main_menu()
