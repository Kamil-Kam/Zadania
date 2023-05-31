"""
Napisz skrypt, który sprawdzi i wypisze na ekran ile liczb jest większych niż 8: 10, 5, 4, 62, 4, 13, 7, 8, 21]
"""

elements_list = [10, 5, 4, 62, 4, 13, 7, 8, 21]
mark = 8


def get_numbers_bigger_than(elements_list: list, mark: int) -> None:
    amount = sum(1 for n in elements_list if n > mark)
    print(amount)

    input()


get_numbers_bigger_than(elements_list, mark)
