emp1 = ["Tester", "geo@example.com", "Joe Doe", 25, 8200]
emp2 = ["Front-end", "jeffery@example.com", "Jeffery", 25, 98200]
emp3 = ["Web Developer", "jay@example.com", "Jay", 35, 3200]


# class
class Employee:

    def __init__(self, name, email, age, payment, jobTitle):

     # instance attributes
        self.name = name
        self.email = email
        self.age = age
        self.payment = payment
        self.jobTitle = jobTitle


# instance
emp1 = Employee("George", "george25@example.com", 25, "Backend", 7855)
print(emp1.name, emp1.email, emp1.age, emp1.jobTitle, emp1.payment)
emp2 = Employee("Jeffery", "jeffery@example.com", 25, "Front-end", 8200)
print(emp2.name, emp2.email, emp2.jobTitle,
      emp2.age, emp2.jobTitle, emp2.payment)

emp3 = Employee("Web Developer", "jay@example.com",
                "Jay", 35, 3200)
print(emp3.name, emp3.jobTitle, emp3.age, emp3.email, emp3.payment)
