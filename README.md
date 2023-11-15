# Менеджер Заметок

**Менеджер Заметок** - это консольное приложение на Python, предназначенное для создания, хранения, поиска и удаления заметок. Приложение использует SQLite для хранения данных и состоит из нескольких модулей, обеспечивающих различные функции в рамках приложения.

## Модули

1. **database_manager.py**
   - Отвечает за взаимодействие с базой данных SQLite.
   - Функции:
     - `initialize_database()`: инициализация и создание таблицы заметок.
     - `add_note()`: добавление новой заметки в базу данных.
     - `get_all_notes()`: извлечение всех заметок из базы данных.
     - `search_notes()`: поиск заметок по ключевому слову.
     - `delete_note()`: удаление заметки из базы данных.

2. **note_manager.py**
   - Управляет основной бизнес-логикой приложения.
   - Функции:
     - `create_note()`: логика создания новой заметки.
     - `display_notes()`: отображение списка всех заметок.
     - `search_note()`: логика поиска заметок.
     - `remove_note()`: логика удаления заметки.

3. **ui_manager.py**
   - Управляет пользовательским интерфейсом приложения.
   - Функции:
     - `main_menu()`: отображение главного меню приложения.
     - `create_note_ui()`: интерфейс для создания новой заметки.
     - `search_note_ui()`: интерфейс для поиска заметок.
     - `remove_note_ui()`: интерфейс для удаления заметки.

4. **utils.py**
   - Содержит вспомогательные функции.
   - Функции:
     - `validate_input()`: валидация ввода пользователя.
     - `format_note_display()`: форматирование отображения заметки.

5. **config.py**
   - Содержит конфигурационные параметры приложения, например, путь к файлу базы данных.

## Инструкции по установке

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.x).
2. Запустите приложение, выполнив команду: `python ui_manager.py` в командной строке.

## Использование

1. После запуска приложения выберите одну из опций из меню, введя соответствующую цифру.
2. Следуйте инструкциям на экране для выполнения выбранной операции.

## Примеры кода

```python
# Инициализация менеджера заметок
note_manager = NoteManager("path/to/database.db")

# Пример использования функции добавления заметки
note_manager.create_note("Заголовок заметки", "Содержание заметки")

# Пример использования функции поиска заметок
notes = note_manager.search_note("ключевое слово")

# Пример использования функции удаления заметки
note_manager.remove_note(note_id)
