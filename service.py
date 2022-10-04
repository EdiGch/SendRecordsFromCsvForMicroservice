from errors import MismatchedNumberOfColumns, TheFileIsTooLarge
from read_csv_file import ReadCsvFile
from send_request import SendRequest
from saving_to_csv_file import SavingToCsvFile


class Service:
    _read_csv_file: ReadCsvFile

    def __init__(self):
        self._read_csv_file = ReadCsvFile()

    def send_csv_for_validation(self):
        try:
            read_csv_file = self._read_csv_file
            read_csv_file.open_file()
            send_request = SendRequest(read_csv_file.records_from_file_csv, read_csv_file.number_of_lines)
            send_request.send()
            saving_to_csv_file = SavingToCsvFile(send_request.response_list_after_send)
            saving_to_csv_file.write_csv()

        except TheFileIsTooLarge as e:
            print(e.message)
        except MismatchedNumberOfColumns as e:
            print(str(e))
        except BaseException as e:
            print(str(e))
