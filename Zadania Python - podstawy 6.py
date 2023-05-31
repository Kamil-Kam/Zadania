"""
Napisz skrypt, który wyświetli daty w formacie YYYY-MM-DD z przedziału <x, y> (wartości x i y podaje użytkownik)
"""
import datetime

text_inf = "Podaj datę w formacie YYYY-MM-DD"
text_x_input = "Podaj pierwszą datę: "
text_y_input = "Podaj drugą datę: "
text_incorrect_format = 'Format daty jest nieprawidłowy!'


def display_date(text_inf: str, text_x_input: str, text_y_input: str, text_incorrect_format: str) -> None:
    data_list = []
    print(text_inf)
    x = input(text_x_input)
    y = input(text_y_input)

    try:
        x_date = datetime.datetime.strptime(x, "%Y-%m-%d")
        y_date = datetime.datetime.strptime(y, "%Y-%m-%d")

        older_date = min(x_date, y_date)
        newer_date = max(x_date, y_date)

        while older_date <= newer_date:
            date = older_date.strftime("%Y-%m-%d")
            data_list.append(date)
            older_date += datetime.timedelta(days=1)

        for n in data_list:
            print(n)

    except:
        print(text_incorrect_format)
        display_date(text_inf, text_x_input, text_y_input, text_incorrect_format)

    input()


display_date(text_inf, text_x_input, text_y_input, text_incorrect_format)
