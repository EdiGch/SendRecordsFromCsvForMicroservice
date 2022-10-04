import collections
import os
from typing import List

import pandas as pd
from pandas import Series

import settings
from errors import MismatchedNumberOfColumns, TheFileIsEmpty, TheFileIsTooLarge
from model import FileCsv


class ReadCsvFile:
    file_type: str = settings.FILE_TYPE
    file_path: str = settings.FILE_PATH
    file_name: str = settings.FILE_NAME
    maximum_file_size: int = settings.MAXIMUM_FILE_SIZE
    separator: str = settings.SEPARATOR
    acceptable_columns: set = settings.ACCEPTABLE_COLUMNS
    records_from_file_csv: List[FileCsv] = []
    number_of_lines: int = 0

    def __init__(self,
                 file_type=settings.FILE_TYPE,
                 file_path=settings.FILE_PATH,
                 file_name=settings.FILE_NAME,
                 maximum_file_size=int(settings.MAXIMUM_FILE_SIZE),
                 separator=settings.SEPARATOR
                 ):
        self.file_type = file_type
        self.file_path = file_path
        self.file_name = file_name
        self.maximum_file_size = maximum_file_size
        self.separator = separator

        self._exact_file_path = self.file_path + self.file_name + file_type
        self._data_validation()

    def open_file(self):
        data = pd.read_csv(self._exact_file_path, on_bad_lines='skip', sep=self.separator)
        columns: list = data.head().columns.values
        self._check_the_existence_of_the_columns(columns)
        for index, row in data.iterrows():
            self.records_from_file_csv.append(self._convert_to_model(row))
            self.number_of_lines = self.number_of_lines + 1

    def _convert_to_model(self, row: Series) -> FileCsv:
        file_row: dict = {}
        for column in self.acceptable_columns:
            file_row[column] = None if pd.isnull(row[column]) else (row[column])

        return FileCsv(**file_row)

    def _data_validation(self):
        if not os.path.isfile(self._exact_file_path):
            raise FileNotFoundError("Nie znaleźono pliku")

        if os.stat(self._exact_file_path).st_size == 0:
            raise TheFileIsEmpty

        if os.stat(self._exact_file_path).st_size > self.maximum_file_size:
            raise TheFileIsTooLarge("Plik jest zbyt duży")

    def _check_the_existence_of_the_columns(self, columns: list):

        if collections.Counter(columns) != collections.Counter(self.acceptable_columns):
            raise MismatchedNumberOfColumns("W pliku nie istnieją wszystkie kolumny których wymaga program")



