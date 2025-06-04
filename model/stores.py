from dataclasses import dataclass

@dataclass
class Store:
    store_id: int
    store_name: str
    phone: str
    email: str
    street: str
    city: str
    state: str
    zip_code: str


    def __hash__(self):
        return hash((self._store_id, self._email))

    def __eq__(self, other):
        if not isinstance(other, Store):
            return NotImplemented
        return (self._store_id == other._store_id and
                self._email == other._email and
                self._store_name == other._store_name and
                self._phone == other._phone and
                self._street == other._street and
                self._city == other._city and
                self._state == other._state and
                self._zip_code == other._zip_code)

    def __str__(self):
        return (f"Store(ID: {self._store_id}, Name: {self._store_name}, Phone: {self._phone}, "
                f"Email: {self._email}, Address: {self._street}, {self._city}, {self._state} {self._zip_code})")
