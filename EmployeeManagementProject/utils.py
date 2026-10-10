from functools import reduce
from typing import Iterable
from models import Employee


def sort_employees_by_salary(employees: Iterable[Employee]) -> list[Employee]:
    # lambda: use salary as the sorting key
    return sorted(employees, key=lambda employee: employee.salary, reverse=True)


def filter_high_salary(employees: Iterable[Employee], minimum_salary: float) -> list[Employee]:
    # filter + lambda
    return list(filter(lambda employee: employee.salary >= minimum_salary, employees))


def employee_names(employees: Iterable[Employee]) -> list[str]:
    # List comprehension
    return [employee.name for employee in employees]


def salary_dictionary(employees: Iterable[Employee]) -> dict[str, float]:
    # Dictionary comprehension
    return {employee.name: employee.salary for employee in employees}


def unique_salaries(employees: Iterable[Employee]) -> set[float]:
    # Set comprehension
    return {employee.salary for employee in employees}


def total_salary(employees: Iterable[Employee]) -> float:
    # reduce + lambda; the start value makes an empty list safe
    return reduce(lambda total, employee: total + employee.salary, employees, 0.0)


def bonus_list(employees: Iterable[Employee]) -> list[float]:
    # map + lambda
    return list(map(lambda employee: employee.calculate_bonus(), employees))


def employee_generator(employees: Iterable[Employee]):
    # Generator: yields one employee at a time
    for employee in employees:
        yield employee


def log_execution(function):
    """Simple decorator that logs the start and end of a function."""
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Starting {function.__name__}")
        result = function(*args, **kwargs)
        print(f"[LOG] Finished {function.__name__}")
        return result
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper


def print_arguments(*args, **kwargs):
    """Demonstrates *args and **kwargs."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
