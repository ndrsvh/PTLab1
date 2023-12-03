# -*- coding: utf-8 -*-
import argparse
import sys
from IndCalcRating import StudentsQuartile
from XML_DataReader import XML_DataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    # path = get_path_from_arguments(sys.argv[1:])
    # reader = XML_DataReader()
    students = {
        "Иванов Иван Иванович": [
            ("Математика", 80),
            ("Физика", 75),
            ("Химия", 85)],
        "Петров Петр Петрович": [
            ("Математика", 50),
            ("Физика", 50),
            ("Химия", 55)],
        "Сидоров Сидор Сидорович": [
            ("Математика", 90),
            ("Физика", 85),
            ("Химия", 92)],
        "Кузнецов Кузьма Кузьмич": [
            ("Математика", 50),
            ("Физика", 55),
            ("Химия", 50)],
    }
    print("Students: ", students)
    students_q1 = StudentsQuartile(students)
    rating = students_q1.find_students_in_quartile()
    print("Rating: ", rating)


if __name__ == "__main__":
    main()
