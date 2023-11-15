def validate_input(input_str, input_type):
    """Валидация ввода пользователя с преобразованием типа."""
    try:
        return input_type(input_str)
    except ValueError:
        print(f"Ввод должен быть типа {input_type.__name__}. Попробуйте еще раз.")
        return None


def format_note_display(note):
    """Форматирование отображения заметки."""
    return f"ID: {note[0]}, Заголовок: {note[1]}, Содержание: {note[2]}"
