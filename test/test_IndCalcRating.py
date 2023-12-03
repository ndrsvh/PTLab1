from IndCalcRating import StudentsQuartile


# Тест для проверки find_students_in_quartile
def test_find_students_in_quartile():
    # Подготовка данных для теста с русскими именами
    data = {
        "Иванов Иван Иванович": [
            ("Математика", 80),
            ("Физика", 75),
            ("Химия", 85)],
        "Петров Петр Петрович": [
            ("Математика", 60),
            ("Физика", 55),
            ("Химия", 50)],
        "Сидоров Сидор Сидорович": [
            ("Математика", 90),
            ("Физика", 85),
            ("Химия", 92)],
        "Кузнецов Кузьма Кузьмич": [
            ("Математика", 60),
            ("Физика", 55),
            ("Химия", 50)],
    }

    # Создание объекта StudentsQuartile
    # и вызов метода find_students_in_quartile
    students_quartile = StudentsQuartile(data)
    result = students_quartile.find_students_in_quartile()

    # Проверка ожидаемого результата
    expected_result = ["Петров Петр Петрович", "Кузнецов Кузьма Кузьмич"]
    assert result == expected_result
