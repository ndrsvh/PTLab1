# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
from lxml import etree  # импортируем библиотеку lxml


class XML_DataReader(DataReader):
    def read(self, path: str) -> DataType:
        data = {}
        tree = etree.parse(path)
        students = tree.findall("student")
        for student in students:
            name = student.get("name")
            grades = []
            for subject in student:
                subject_name = subject.tag
                subject_grade = int(subject.text)
                grades.append((subject_name, subject_grade))
            data[name] = grades
        return data
