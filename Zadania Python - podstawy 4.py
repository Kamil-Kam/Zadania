"""
Napisz skrypt, który sprawdzi czy klucz "produkt" występuje już w słowniku i jeśli nie występuje to dodaj
element "product" : "Ferrero Rosher" :
thisdict = {
    "audiocode": 236456,
    "media": "TV",
    "brand": "Nestle",
    "category": "Praliny"
}
"""

thisdict = {
    "audiocode": 236456,
    "media": "TV",
    "brand": "Nestle",
    "category": "Praliny"
}

element = ["product", "Ferrero Rosher"]


def check_dict(thisdict: dict, element: list) -> dict:
    if element[0] not in thisdict:
        thisdict.update({element[0]: element[1]})

    return thisdict


check_dict(thisdict, element)

