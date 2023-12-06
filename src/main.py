# -*- coding: utf-8 -*-
import argparse
import sys
from IndCalcRating import StudentsQuartile
from XML_DataReader import XML_DataReader
from TextDataReader import TextDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    if path.endswith('.txt'):
        reader = TextDataReader()
    elif path.endswith('.xml'):
        reader = XML_DataReader()
    
    students = reader.read(path)
    
    print("Students: ", students)
    students_q1 = StudentsQuartile(students)
    rating = students_q1.find_students_in_quartile()
    print("Rating: ", rating)


if __name__ == "__main__":
    main()
