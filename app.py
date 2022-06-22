emp1 = ["Tester", "geo@example.com", "Joe Doe", 25, 8200, "jobTitle"]
emp2 = ["Front-end", "jeffery@example.com", "Jeffery", 25, 98200, "jobTitle"]
emp3 = ["Web Developer", "jay@example.com", "Jay", 35, 3200, "jobTitle"]


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
      emp2.payment, emp2.jobTitle, emp2.payment)
