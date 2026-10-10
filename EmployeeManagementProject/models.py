from abc import ABC, abstractmethod
from exceptions import InvalidSalaryError


class Employee(ABC):
    """Abstract base class shared by all employee types."""

    company_name = "ABC Technologies"
    employee_count = 0

    def __init__(self, employee_id: str, name: str, salary: float):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @property
    def salary(self) -> float:
        """Getter for the encapsulated salary value."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Validate salary whenever it is assigned."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise InvalidSalaryError("Salary must be a number greater than zero.")
        self._salary = float(value)

    def display_details(self) -> str:
        return (
            f"ID: {self.employee_id} | Name: {self.name} | "
            f"Role: {self.__class__.__name__} | Salary: ₹{self.salary:,.2f}"
        )

    @abstractmethod
    def calculate_bonus(self) -> float:
        """Each employee type must implement its own bonus calculation."""
        raise NotImplementedError

    @classmethod
    def get_company_name(cls) -> str:
        return cls.company_name

    @staticmethod
    def is_valid_employee_id(employee_id: str) -> bool:
        return employee_id.startswith("EMP") and employee_id[3:].isdigit()

    def to_dict(self) -> dict:
        """Convert an employee object into JSON-friendly data."""
        data = {
            "employee_id": self.employee_id,
            "name": self.name,
            "salary": self.salary,
            "role": self.__class__.__name__,
        }
        if isinstance(self, Developer):
            data["programming_language"] = self.programming_language
        elif isinstance(self, Manager):
            data["team_size"] = self.team_size
        elif isinstance(self, Tester):
            data["automation_tool"] = self.automation_tool
        return data

    def __str__(self) -> str:
        return self.display_details()


class Developer(Employee):
    def __init__(self, employee_id: str, name: str, salary: float,
                 programming_language: str = "Python"):
        super().__init__(employee_id, name, salary)
        self.programming_language = programming_language

    def calculate_bonus(self) -> float:
        return self.salary * 0.10


class Manager(Employee):
    def __init__(self, employee_id: str, name: str, salary: float,
                 team_size: int = 1):
        super().__init__(employee_id, name, salary)
        self.team_size = team_size

    def calculate_bonus(self) -> float:
        return self.salary * 0.20


class Tester(Employee):
    def __init__(self, employee_id: str, name: str, salary: float,
                 automation_tool: str = "Selenium"):
        super().__init__(employee_id, name, salary)
        self.automation_tool = automation_tool

    def calculate_bonus(self) -> float:
        return self.salary * 0.15


def employee_from_dict(data: dict) -> Employee:
    """Re-create the correct subclass from a JSON dictionary."""
    role = data.get("role", "Employee")
    common = (data["employee_id"], data["name"], data["salary"])

    if role == "Developer":
        return Developer(*common, data.get("programming_language", "Python"))
    if role == "Manager":
        return Manager(*common, data.get("team_size", 1))
    if role == "Tester":
        return Tester(*common, data.get("automation_tool", "Selenium"))

    raise ValueError(f"Unknown employee role: {role}")
