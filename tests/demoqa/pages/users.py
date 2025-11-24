from dataclasses import dataclass


@dataclass
class User:
    fullname: str
    email: str
    current_address: str
    permanent_address: str


first_user = User(
    fullname="Alexandra",
    email="achernecova@inbox.ru",
    current_address="Москва",
    permanent_address="Москва",
)
