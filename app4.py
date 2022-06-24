# emcap


class Employee:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._password = None
        self._secret_number = 0

   # getter function
    def get_password(self):
        return self._password

  # setter function
    def set_password(self, value):
        # check value
        self._password = value


emp = Employee("Ney", "ney25@example.com")

print(emp.name, emp.email, emp._password)

emp.set_password(125896)
print(emp.get_password())
