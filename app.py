import itertools
import json
import pandas as pd


def is_duplicates(df, columns):
    """
    Проверяет, есть ли в наборе данных дубликаты строк на основе указанных столбцов.

    Параметр df: DataFrame с данными
    Параметр columns: список имен столбцов для проверки на дубликаты
    Возвращает: True, если найдены дубликаты, иначе False
    """
    return df.duplicated(subset=columns).any()


def find_minimal_unique_set(df):
    """
    Ищет минимальный набор признаков, уникально идентифицирующий каждую сущность.

    Параметр df: DataFrame с данными
    Возвращает: список с именами минимального набора признаков
    """
    columns = df.columns
    n = len(columns)

    # Перебираем все возможные комбинации столбцов
    for r in range(1, n + 1):
        for subset in itertools.combinations(columns, r):
            if not is_duplicates(df, subset):
                return list(subset)
    return []


def main(file_path):
    """
    Основная функция, принимающая путь к JSON-файлу и возвращающая минимальный набор признаков.

    Параметр file_path: путь к JSON-файлу с исходными данными
    Возвращает: список с именами минимального набора признаков
    """
    # Чтение JSON-файла
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Преобразование JSON-данных в DataFrame
    df = pd.DataFrame(data)

    # Поиск минимального набора признаков
    minimal_set = find_minimal_unique_set(df)

    return minimal_set


if __name__ == "__main__":
    # Путь к JSON-файлу для тестирования
    file_path = 'data.json'  # Замените на путь к вашему JSON-файлу
    print(main(file_path))