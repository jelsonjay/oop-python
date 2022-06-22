emp1 = ["Tester", "geo@example.com", "Joe Doe", 25, 8200]
emp2 = ["Front-end", "jeffery@example.com", "Jeffery", 25, 98200]
emp3 = ["Web Developer", "jay@example.com", "Jay", 35, 3200]
jobDescription = ["Mobile App", "IOS Developer", "Android Developer"]

# declare a class


class Employee:

    def __init__(self, name, email, age, payment, jobTitle):

     # instance attributes
        self.name = name
        self.email = email
        self.age = age
        self.payment = payment
        self.jobTitle = jobTitle

# instance method

    def write_code(self):
        print(f"{self.name} could be a good fit for our company...")


# instance
emp1 = Employee("George", "george25@example.com", 25, "Backend", 7855)
emp2 = Employee("Jeffery", "jeffery@example.com", 25, "Front-end", 8200)
emp3 = Employee("Jay", "jay@example.com", 35, "Developer", 3200)

# call method
emp3.write_code()
