# inherits & extend, override
class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        print(f"{self.name} is a hard worker, derserve a promotion!")

# extends the function employee


class JobType(Employee):
    def __init__(self, name, email, salary, tester, designer, backend, frontend):
        super().__init__(name, email, salary)
        self.tester = tester
        self.designer = designer
        self.backend = backend
        self.frontend = frontend


class Developer(Employee):
    pass


job = JobType("Joe Deo", "jeo4@gmail.com", 2500,
              "Tester", "Designer", "Back-End", "Front-End")
developer = Developer("Jazz", "jazz@example.com", 3500)

print(job.name, job.email, job.salary)
job.work()
print(job.tester, job.designer, job.backend, job.frontend)


print("From developer class...")
print(developer.name, developer.email, developer.salary)
developer.work()
