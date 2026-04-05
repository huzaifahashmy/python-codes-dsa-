from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    id: int
    department: str
employee1 = Employee("John Doe", 123, "Engineering")
print(employee1)    


