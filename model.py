from dataclasses import dataclass


@dataclass
class Model:
    name: str | None
    email: str | None
    phone: str | None
    country_iso: str | None
    postcode: str | None
    province_code: str | None
    address: str | None
    full_address: str | None


class FileCsv(Model):
    """Data that has been FileCsv"""


class Request(Model):
    def __init__(self, city, name, email, phone, country_iso, postcode, province_code, address,
                 full_address):
        self.city = city
        Model.__init__(self, name, email, phone, country_iso, postcode, province_code, address,
                       full_address)


class Response(Request):
    def __init__(self, status, status_code, reason, text, city, name, email, phone, country_iso,
                 postcode, province_code, address,
                 full_address):
        self.status = status
        self.status_code = status_code
        self.reason = reason
        self.text = text
        Request.__init__(self, city, name, email, phone, country_iso, postcode, province_code,
                         address,
                         full_address)


request = Request(
    name="Olek",
    email="",
    phone="",
    country_iso="",
    postcode="",
    province_code="",
    address="",
    full_address="",
    city="WW"
)

print(request.__dict__)

response = Response(
    name="OLEK",
    email="",
    phone="",
    country_iso="",
    postcode="",
    province_code="",
    address="",
    full_address="",
    city="",
    status="",
    status_code="201",
    reason="",
    text=""
)

print(response.__dict__)
