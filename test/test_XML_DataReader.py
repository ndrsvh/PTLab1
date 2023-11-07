# -*- coding: utf-8 -*-
import pytest
from XML_DataReader import XML_DataReader
from Types import DataType

xml_reader = XML_DataReader()

expected_data = {
    "Иванов Иван Иванович": [
        ("математика", 67),
        ("литература", 100),
        ("программирование", 91),
    ],
    "Петров Петр Петрович": [
        ("математика", 78),
        ("литература", 89),
        ("программирование", 86),
    ],
    "Смирнов Алексей Алексеевич": [
        ("математика", 85),
        ("литература", 73),
        ("программирование", 92),
    ],
    "Кузнецова Мария Ивановна": [
        ("математика", 88),
        ("литература", 79),
        ("программирование", 95),
    ],
    "Попов Дмитрий Сергеевич": [
        ("математика", 94),
        ("литература", 81),
        ("программирование", 89),
    ],
}


class TestXML_DataReader:
    @pytest.fixture(scope="class")
    def test_xml_file(self) -> str:
        filename = "C:\\Users\\sivukha.a\\Desktop\\TP_Lab1\\test\\data.xml"
        yield filename

    def test_read(self, test_xml_file: str) -> None:
        actual_data = xml_reader.read(test_xml_file)
        assert actual_data == expected_data
