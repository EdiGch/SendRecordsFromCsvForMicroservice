import os
from typing import Final

from dotenv import dotenv_values


config = {
    **dotenv_values(".env"),  # load shared development variables
    **dotenv_values(".env.local"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

FILE_TYPE: Final[str] = os.environ.get("FILE_TYPE", ".csv")
FILE_PATH: Final[str] = os.environ.get("FILE_PATH", "volumes/")
FILE_NAME: Final[str] = os.environ.get("FILE_NAME", "orders_2022-05-24")
MAXIMUM_FILE_SIZE: Final[int] = os.environ.get("MAXIMUM_FILE_SIZE", 1048576)
SEPARATOR: Final[str] = os.environ.get("SEPARATOR", ";")
ACCEPTABLE_COLUMNS: set = {"name",
                           "email",
                           "phone",
                           "country_iso",
                           "postcode",
                           "address",
                           "province_code",
                           "full_address"}


ENDPOINT_ADDRESS: Final[str] = config.get("ENDPOINT_ADDRESS", "")
REQUESTS_TIMEOUT: Final[int] = os.environ.get("REQUESTS_TIMEOUT", 60)
FILE_PATH_FOR_REPORT: Final[str] = os.environ.get("FILE_PATH_FOR_REPORT", "")
BASIC_NAME_OF_THE_REPORT: Final[str] = os.environ.get("BASIC_NAME_OF_THE_REPORT", "")
FILE_TYPE_FOR_REPORT: Final[str] = os.environ.get("FILE_TYPE_FOR_REPORT", "")

HEADER: Final[str] ='\033[95m'
OKBLUE: Final[str] ='\033[94m'
OKCYAN: Final[str] ='\033[96m'
OKGREEN: Final[str] ='\033[92m'
WARNING: Final[str] ='\033[93m'
FAIL: Final[str] ='\033[91m'
ENDC: Final[str] ='\033[0m'
BOLD: Final[str] ='\033[1m'
UNDERLINE: Final[str] ='\033[4m'
