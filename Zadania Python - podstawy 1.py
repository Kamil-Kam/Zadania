"""
Napisz skrypt, który obliczy i wypisze na ekran sumę wszystkich elementów listy: [10, 5, 4, 62, 4, 13, 7, 8, 21]
"""

elements_list = [10, 5, 4, 62, 4, 13, 7, 8, 21]


def get_sum(elements_list: list) -> None:
    list_sum = sum(elements_list)
    print(list_sum)

    input()


get_sum(elements_list)
