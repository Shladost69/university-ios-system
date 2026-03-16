def get_user_input():
    """
    Функция для ввода данных об оценке от пользователя.
    Возвращает словарь с данными или None при ошибке.
    """
    try:
        student_name = input("Введите имя студента (строка): ").strip()
        if not student_name:
            raise ValueError("Имя студента не может быть пустым.")

        grade_str = input("Введите оценку (вещественное число, например 4.5): ").strip()
        grade = float(grade_str)
        if grade < 0 or grade > 5:
            raise ValueError("Оценка должна быть от 0 до 5.")

        course_id_str = input("Введите ID курса (целое число): ").strip()
        course_id = int(course_id_str)
        if course_id <= 0:
            raise ValueError("ID курса должно быть положительным.")

        comment = input("Введите комментарий (строка, опционально): ").strip()

        return {
            "student_name": student_name,
            "grade": grade,
            "course_id": course_id,
            "comment": comment
        }
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return None


def process_data(data):
    """
    Обработка данных: вывод и простая статистика.
    """
    if data:
        print(f"Студент: {data['student_name']}, Курс ID: {data['course_id']}")
        print(f"Оценка: {data['grade']:.1f}, Комментарий: {data['comment']}")
        # Пример: расчет "среднего" (для одной оценки)
        average = data['grade']
        print(f"Средняя оценка: {average:.1f}")
    else:
        print("Данные не введены.")


# Пример использования
if __name__ == "__main__":
    data = get_user_input()
    process_data(data)