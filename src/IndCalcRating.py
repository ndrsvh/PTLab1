from Types import DataType
from statistics import quantiles


RatingType = dict[str, float]


class StudentsQuartile:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find_students_in_quartile(self) -> list[str]:
        ratings = []
        for key in self.data:
            total_rating = sum(subject[1] for subject in self.data[key])
            average_rating = total_rating / len(self.data[key])
            ratings.append(average_rating)

        # Рассчитываем первую квартиль
        q1 = quantiles(ratings, n=4)[0]

        # Находим студентов, чей рейтинг попадает в первую квартиль
        students_in_quartile = [
            student for student, rating in zip(self.data.keys(), ratings)
            if rating <= q1
        ]

        return students_in_quartile
