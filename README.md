# Описание программы

## Цель 
* Программа предназначена для нахождения минимальных характеристик, которые уникально определяют каждую запись в наборе данных

## Принцип работы алгоритма

* Алгоритм принимает на вход путь к JSON-файлу с данными,читает содержимое файла и преобразует его в pandas DataFrame для удобной работы с табличными данными.

* Функция is_duplicates проверяет, есть ли дубликаты строк в DataFrame на основе указанных столбцов.Если дубликаты присутствуют, возвращает True, иначе False.

* Для поиска минимального набора признаков используется функция find_minimal_unique_set, которая генерирует все возможные комбинации столбцов, начиная с комбинаций минимального размера.

* Алгоритм проверяет комбинации столбцов на уникальность записей, начиная с одного столбца и постепенно увеличивая их число, пока не найдёт минимальный уникальный набор. Как только такая комбинация найдена, алгоритм возвращает её как результат.

* Основная функция main объединяет все шаги: чтение данных, преобразование в DataFrame, поиск минимального уникального набора признаков и возврат этого набора.Результат выводится на экран или может быть использован в дальнейших вычислениях.

## Особенности

* Алгоритм перебирает все возможные комбинации столбцов начиная с самых маленьких, что гарантирует нахождение минимального набора признаков

* Вместо полного перебора всех возможных комбинаций значений, алгоритм перебирает только комбинации столбцов 

* Для работы с большими объемами данных была использована библиотека pandas 

## Для работы с программой 

1. Склонируйте репозиторий
```
git clone https://github.com/aleksandrzaruba1/minimal-identifiers.git
```
2. Установите библеотеку pandas
```
pip install pandas
```
3. В папке app.py укажите путь к вашему json файлу

## Структура программы
![](https://github.com/user-attachments/assets/bf9fbf09-7a9e-4528-8e71-2eb9894a2089)



