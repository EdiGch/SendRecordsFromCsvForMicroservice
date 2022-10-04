from typing import List, Final, Dict
import json

import settings
from model import FileCsv, Response, Request
import requests


class SendRequest:
    _records_from_file_csv: List[FileCsv]
    response_list_after_send: List[Response] = []
    records_sent: int = 0
    _endpoint_address: str = settings.ENDPOINT_ADDRESS
    _requests_timeout: int = int(settings.REQUESTS_TIMEOUT)
    HEADERS: Final[Dict] = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    def __init__(self, records_from_file_csv: List[FileCsv], number_records_to_sent: int):
        self._records_from_file_csv = records_from_file_csv
        self.number_records_to_sent = number_records_to_sent

    def send(self):
        print(f"{settings.OKGREEN}Proces wysyłki rozpoczęty{settings.OKGREEN}")
        for record_file_csv in self._records_from_file_csv:
            print(f"Liczba rekordów do wysłania {self.number_records_to_sent}")
            self.response_list_after_send.append(self._send_request(record_file_csv))

        print("\n")
        print(f"{settings.OKGREEN}Liczba rekordów do wysyłki "
              f"{self.number_records_to_sent}, wysłano {self.records_sent}{settings.OKGREEN}")

    def _send_request(self, record_file_csv: FileCsv):
        request_obj: Request = self._convert_to_request(record_file_csv)
        request_json: str = self._convert_to_json(request_obj)

        requests_reason = requests.post(
            self._endpoint_address,
            json=request_json,
            headers=self.HEADERS,
            timeout=self._requests_timeout
        )
        self.records_sent = self.records_sent + 1
        self.number_records_to_sent = self.number_records_to_sent - 1
        return Response(
            name=request_obj.name,
            email=request_obj.email,
            phone=request_obj.phone,
            country_iso=request_obj.country_iso,
            postcode=request_obj.postcode,
            province_code=request_obj.province_code,
            address=request_obj.address,
            full_address=request_obj.full_address,
            city=request_obj.city,
            status="sukces" if requests_reason.status_code == 201 else "błąd",
            status_code=requests_reason.status_code,
            reason=requests_reason.reason,
            text=requests_reason.text
        )

    @staticmethod
    def _convert_to_request(record_file_csv: FileCsv) -> Request:
        return Request(
            name=record_file_csv.name,
            email=record_file_csv.email,
            phone=record_file_csv.phone,
            country_iso=record_file_csv.country_iso,
            postcode=record_file_csv.postcode,
            province_code=record_file_csv.province_code,
            address=record_file_csv.address,
            full_address=record_file_csv.full_address,
            city=None
        )

    @staticmethod
    def _convert_to_json(request: Request) -> str:
        request_dict: dict = request.__dict__
        return json.dumps(request_dict)
