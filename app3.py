# inherits & extend, override
class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        print(f"{self.name} is a hard worker, derserve a promotion!")


class JobType(Employee):
    pass


class Developer(Employee):
    pass


job = JobType("Joe Deo", "jeo4@gmail.com", 2500)
developer = Developer("Jazz", "jazz@example.com", 3500)

print(job.name, job.email, job.salary)
job.work()
print("From developer class")
print(developer.name, developer.email, developer.salary)
developer.work()
