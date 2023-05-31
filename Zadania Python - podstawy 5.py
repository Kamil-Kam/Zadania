"""
Napisz skrypt, który utworzy plik tekstowy, które by zawierał dane z listy: [10, 5, „praca” , 62, 4, 13, 7, -8, 21]
"""

element_list = [10, 5, "praca", 62, 4, 13, 7, -8, 21]
txt_path = 'Zadania Python - podstawy 5.txt'


def create_txt(element_list: list, txt_path: str) -> None:
    with open(txt_path, 'w') as txt:
        txt.writelines(f"{n}\n" for n in element_list)


create_txt(element_list, txt_path)
