emp1 = ["Tester", "Joe Doe" "age", 8200]
emp2 = ["Front-end", "Smith Jeffery" "age", 8200]


# class
class Employee:

    def __init__(self, name, email, age, payment, jobTitle):

        # instance attributes

        self.name = name
        self.email = email
        self.age = age
        self.jobTitle = jobTitle
        self.payment = payment


# instance
emp1 = Employee("George", "georgr@example.com", 41, "Backend", 7855)
print(emp1.name, emp1.email)
