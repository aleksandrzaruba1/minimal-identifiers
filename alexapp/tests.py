import unittest
import json
import pandas as pd
from app import is_duplicates, find_minimal_unique_set, main

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Подготовка данных для тестирования
        self.data = [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30},
            {"id": 3, "name": "Alice", "age": 25}
        ]
        with open('../data.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f)

    def test_is_duplicates(self):
        df = pd.DataFrame(self.data)
        self.assertTrue(is_duplicates(df, ['name']))  # Должны быть дубликаты по 'name'
        self.assertFalse(is_duplicates(df, ['id']))   # Не должно быть дубликатов по 'id'

    def test_find_minimal_unique_set(self):
        df = pd.DataFrame(self.data)
        result = find_minimal_unique_set(df)
        self.assertCountEqual(result, ['id'])  # Ожидаем ['id'] как минимальный уникальный набор

    def test_main(self):
        minimal_set = main('../data.json')
        self.assertCountEqual(minimal_set, ['id'])  # Ожидаем ['id'] из JSON-файла

if __name__ == '__main__':
    unittest.main()
