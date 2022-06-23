# emcap

from typing_extensions import Self


class Employee:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._password = None
        self._secret_number = 0

    def get_password():
        return self._password

    def set_password(self, value):
        self._password = value


emp = Employee("Ney", "ney25@example.com")

print(emp.name, emp.email, emp._password)

emp.set_password(125896)
emp.get_password()
