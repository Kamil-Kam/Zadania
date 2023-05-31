"""
Napisz skrypt, który obliczy i wypisze na ekran sumę elementów listy, które mają typ numeryczny:
[10, 5, „praca” , 62, 4, 13, 7, -8, 21]
"""

elements_list = [10, 5, "praca", 62, 4, 13, 7, -8, 21]


def get_sum(elements_list: list) -> None:
    list_sum = sum(n for n in elements_list if type(n) == int)
    print(list_sum)

    input()


get_sum(elements_list)
