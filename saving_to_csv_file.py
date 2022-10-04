from typing import List
from model import Response
from datetime import datetime
import pandas as pd
import settings


class SavingToCsvFile:
    _file_path_for_report: str = settings.FILE_PATH_FOR_REPORT
    _basic_name_of_the_report: str = settings.BASIC_NAME_OF_THE_REPORT
    _file_type_for_report: str = settings.FILE_TYPE_FOR_REPORT
    _separator: str = settings.SEPARATOR
    records_for_writing: List[Response] = []
    _records_for_writing_csv: list = []

    def __init__(self, records_for_writing: List[Response]):
        self.records_for_writing = records_for_writing
        self.time = datetime.now().strftime("%Y%m%d-%H%M%S")

    def write_csv(self):
        print(f"{settings.OKGREEN}Proces zapisu raportu rozpoczęty{settings.OKGREEN}")
        for content in self.records_for_writing:
            self._records_for_writing_csv.append(content.__dict__)

        csv_write = pd.DataFrame(self._records_for_writing_csv)
        csv_write.to_csv(self._generating_save_paths_and_names(), sep=self._separator, index=False)
        print(f"{settings.OKGREEN}Raport zapisano prawidłowo{settings.OKGREEN}")
        print(f"{settings.OKGREEN}Sprawdź raport zawierający szczegóły wysyłki danych."
              f"{self._generating_save_paths_and_names()}{settings.OKGREEN}")

    def _generating_save_paths_and_names(self) -> str:
        return self._file_path_for_report + self._basic_name_of_the_report + \
               self.time + self._file_type_for_report
