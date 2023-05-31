"""
Prosimy przygotować skrypt Python, który:
1. do pliku data.csv dodaje kolumny year i month zwrócone z kolumny date;
2. utworzy bazę SqlLite oraz tabeli data, która zawiera kolumny jak w pliku wyjściowym z poprzedniego zadania,
oraz dict z kolumnami jak we wejściowych pliku dict.csv oraz kluczem audiocode;
3. wgra dane z plików do bazy danych;
4. stworzy widok, który łącze dane z data i dict;
5. wgra dane z widoku do pliku xlsx.
"""
from Zadanie_Python_functions import *

data_path = "data.csv"
dict_path = "dict.csv"

table_data_name, _ = data_path.split('.')
table_dict_name, _ = dict_path.split('.')

modified_col = 'date'
new_col_1 = 'year'
new_col_2 = 'month'
dict_sql_key = 'audiocode'
database_path = 'database.sqlite3'
view_name = 'data_dict_view'
view_to_xlsx_path = f'{view_name}.xlsx'


def main() -> None:
    edit_csv_file(data_path, modified_col, new_col_1, new_col_2)
    create_database(data_path, dict_path, dict_sql_key, database_path, table_data_name, table_dict_name)
    insert_data_into_database(data_path, dict_path, database_path, table_data_name, table_dict_name)
    create_view(database_path, view_name, table_data_name, table_dict_name)
    export_view_into_xlsx(database_path, view_name, view_to_xlsx_path)

    input()


if __name__ == "__main__":
    main()
