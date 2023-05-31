"""
Prosimy przygotować skrypt Python, który:
1. do pliku data.csv dodaje kolumny year i month zwrócone z kolumny date;
2. utworzy bazę SqlLite oraz tabeli data, która zawiera kolumny jak w pliku wyjściowym z poprzedniego zadania,
oraz dict z kolumnami jak we wejściowych pliku dict.csv oraz kluczem audiocode;
3. wgra dane z plików do bazy danych;
4. stworzy widok, który łącze dane z data i dict;
5. wgra dane z widoku do pliku xlsx.
"""

import csv
import sqlite3
from sqlite3 import Error
import pandas as pd


def edit_csv_file(file_path: str, modified_col: str, new_col_1: str, new_col_2: str) -> None:
    data = []

    try:
        with open(file_path, "r+", newline="") as data_csv:
            data_csv_reader = csv.DictReader(data_csv)
            fieldnames = [n.replace('"', '') for n in data_csv_reader.fieldnames[0].split(',')]

            for row in data_csv:
                row = [n.replace('"', '') for n in row.strip().split(',')]
                row_data = {fieldnames[index]: n for index, n in enumerate(row)}

                year, month, _ = row_data[modified_col].split('-')
                row_data[new_col_1] = year
                row_data[new_col_2] = month
                data.append(row_data)

            modified_fieldnames = data[0].keys()

            data_csv.seek(0)
            data_csv.truncate()

            data_csv_writer = csv.DictWriter(data_csv, fieldnames=modified_fieldnames)
            data_csv_writer.writeheader()
            data_csv_writer.writerows(data)

        print('edit_csv_file - succeed')

    except:
        print(f"edit_csv_file - failed")


def create_database(file_path_1: str, file_path_2: str, file_2_key: str, database_path: str, table_1_name: str,
                    table_2_name: str) -> None:

    with open(file_path_1, "r", newline="") as file_1:
        fieldnames_1 = csv.DictReader(file_1).fieldnames

    with open(file_path_2, "r", newline="") as file_2:
        fieldnames_2 = csv.DictReader(file_2).fieldnames
        fieldnames_2.remove(file_2_key)

    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()

        c.execute(f"CREATE TABLE IF NOT EXISTS {table_1_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                  f"{', '.join(f'{field} TEXT' for field in fieldnames_1)})")

        c.execute(f"CREATE TABLE IF NOT EXISTS {table_2_name} ({file_2_key} INTEGER PRIMARY KEY, "
                  f"{', '.join(f'{field} TEXT' for field in fieldnames_2)})")

        conn.close()
        print("create_database - succeed")

    except Error as error:
        print(f"create_database - failed, {error}")


def insert_data_into_database(file_path_1: str, file_path_2: str, database_path: str, table_1_name: str,
                              table_2_name: str) -> None:

    data_list = [[file_path_1, table_1_name], [file_path_2, table_2_name]]

    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()

        for data in data_list:

            with open(data[0], "r", newline="") as file:
                data_csv_reader = csv.DictReader(file)

                for row in data_csv_reader:
                    data_values = ', '.join(row.keys())
                    columns = ', '.join('?' * len(row))
                    c.execute(f"INSERT INTO {data[1]} ({data_values}) VALUES ({columns})", list(row.values()))

        conn.commit()
        conn.close()

        print("insert_data_into_database - succeed")

    except Error as error:
        print(f"insert_data_into_database - failed, {error}")


def create_view(database_path: str, view_name: str, table_1_name: str, table_2_name: str) -> None:

    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()

        c.execute(f"CREATE VIEW {view_name} AS "
                  f"SELECT {table_1_name}.*, {table_2_name}.advertiser, {table_2_name}.brand "
                  f"FROM {table_1_name} LEFT JOIN {table_2_name} ON {table_1_name}.audiocode = {table_2_name}.audiocode")

        conn.commit()
        conn.close()

        print("create_view  - succeed")

    except Error as error:
        print(f"create_view - failed, {error}")


def export_view_into_xlsx(database_path: str, view_name: str, xlsx_path: str) -> None:

    try:
        conn = sqlite3.connect(database_path)
        df = pd.read_sql_query(f"SELECT * FROM {view_name}", conn)
        writer = pd.ExcelWriter(xlsx_path, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name=view_name)

        for i, column in enumerate(df.columns):
            column_width = max(df[column].astype(str).map(len).max(), len(column)) + 1
            writer.sheets[view_name].set_column(i, i, column_width)

        writer.save()
        conn.close()

        print("export_view_into_xls - succeed")

    except Error as error:
        print(f"export_view_into_xlsx - failed, {error}")
