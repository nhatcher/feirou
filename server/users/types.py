from typing import TypedDict


class CreateAccountData(TypedDict):
    username: str
    email: str
    password: str
    locale: str
    first_name: str
    last_name: str


class UpdateUserSettingsData(TypedDict):
    password: str
    new_password: str
    change_password: bool
    locale: str
    first_name: str
    last_name: str
