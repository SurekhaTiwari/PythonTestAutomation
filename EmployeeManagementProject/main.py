import json
from pathlib import Path

from exceptions import EmployeeNotFoundError, InvalidSalaryError
from models import Developer, Employee, Manager, Tester, employee_from_dict
from utils import (
    bonus_list,
    employee_generator,
    employee_names,
    filter_high_salary,
    log_execution,
    print_arguments,
    salary_dictionary,
    sort_employees_by_salary,
    total_salary,
    unique_salaries,
)

DATA_FILE = Path(__file__).with_name("employees.json")


def load_employees() -> list[Employee]:
    """Load saved employees from the JSON file."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return [employee_from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not load employee data: {error}")
        return []


def save_employees(employees: list[Employee]) -> None:
    """Save employees to JSON."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump([employee.to_dict() for employee in employees], file, indent=4)
    print("Employee data saved.")


def find_employee(employees: list[Employee], employee_id: str) -> Employee:
    for employee in employees:
        if employee.employee_id.lower() == employee_id.lower():
            return employee
    raise EmployeeNotFoundError(f"No employee found with ID {employee_id}.")


def read_salary() -> float:
    try:
        salary = float(input("Enter salary: ₹"))
        if salary <= 0:
            raise InvalidSalaryError("Salary must be greater than zero.")
        return salary
    except ValueError as error:
        raise InvalidSalaryError("Please enter a valid numeric salary.") from error


def choose_role() -> Employee:
    print("Choose role: 1. Developer  2. Manager  3. Tester")
    role_choice = input("Enter choice: ").strip()
    employee_id = input("Employee ID (example EMP105): ").strip().upper()

    if not Employee.is_valid_employee_id(employee_id):
        raise ValueError("Employee ID must start with EMP followed by digits, e.g. EMP105.")

    name = input("Employee name: ").strip()
    if not name:
        raise ValueError("Employee name cannot be empty.")

    salary = read_salary()

    if role_choice == "1":
        language = input("Programming language [Python]: ").strip() or "Python"
        return Developer(employee_id, name, salary, language)
    if role_choice == "2":
        team_text = input("Team size [1]: ").strip() or "1"
        team_size = int(team_text)
        if team_size < 1:
            raise ValueError("Team size must be at least 1.")
        return Manager(employee_id, name, salary, team_size)
    if role_choice == "3":
        tool = input("Automation tool [Selenium]: ").strip() or "Selenium"
        return Tester(employee_id, name, salary, tool)

    raise ValueError("Please choose role 1, 2, or 3.")


def display_employees(employees: list[Employee]) -> None:
    if not employees:
        print("No employees found.")
        return
    print("\nEMPLOYEE LIST")
    print("-" * 80)
    for number, employee in enumerate(employees, start=1):
        print(f"{number}. {employee}")
        print(f"   Bonus: ₹{employee.calculate_bonus():,.2f}")
    print("-" * 80)


@log_execution
def show_reports(employees: list[Employee]) -> None:
    if not employees:
        print("Add at least one employee to view reports.")
        return

    print("\nEmployees sorted by salary (highest first):")
    for employee in sort_employees_by_salary(employees):
        print(f"{employee.name}: ₹{employee.salary:,.2f}")

    try:
        minimum = float(input("\nShow employees earning at least ₹: "))
        print("Matching employees:")
        for employee in filter_high_salary(employees, minimum):
            print(employee.display_details())
    except ValueError:
        print("Invalid amount; skipping salary filter.")

    print("\nNames (list comprehension):", employee_names(employees))
    print("Name-to-salary dictionary:", salary_dictionary(employees))
    print("Unique salaries (set comprehension):", unique_salaries(employees))
    print(f"Total salary (reduce): ₹{total_salary(employees):,.2f}")
    print("Bonuses (map):", [round(value, 2) for value in bonus_list(employees)])

    print("\nEmployees from generator:")
    for employee in employee_generator(employees):
        print("-", employee.name)

    print("\nBonus report (zip):")
    for employee, bonus in zip(employees, bonus_list(employees)):
        print(f"{employee.name}: ₹{bonus:,.2f}")


def main() -> None:
    employees = load_employees()

    while True:
        print(f"""
====== {Employee.get_company_name()} ======
1. Add employee
2. View all employees
3. Search employee by ID
4. Update employee salary
5. Delete employee
6. Reports (lambda, filter, comprehensions, map/reduce, generator)
7. Save data
0. Save and exit
""")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                new_employee = choose_role()
                if any(e.employee_id.lower() == new_employee.employee_id.lower()
                       for e in employees):
                    print("That employee ID already exists.")
                else:
                    employees.append(new_employee)
                    save_employees(employees)
                    print("Employee added successfully.")

            elif choice == "2":
                display_employees(employees)

            elif choice == "3":
                employee_id = input("Enter employee ID: ").strip()
                print(find_employee(employees, employee_id).display_details())

            elif choice == "4":
                employee_id = input("Enter employee ID: ").strip()
                employee = find_employee(employees, employee_id)
                employee.salary = read_salary()
                save_employees(employees)
                print("Salary updated successfully.")

            elif choice == "5":
                employee_id = input("Enter employee ID to delete: ").strip()
                employee = find_employee(employees, employee_id)
                employees.remove(employee)
                save_employees(employees)
                print("Employee deleted successfully.")

            elif choice == "6":
                show_reports(employees)

            elif choice == "7":
                save_employees(employees)

            elif choice == "0":
                save_employees(employees)
                print("Goodbye!")
                break

            else:
                print("Invalid option. Choose 0 to 7.")

        except (EmployeeNotFoundError, InvalidSalaryError, ValueError) as error:
            print(f"Error: {error}")
        except (OSError, json.JSONDecodeError) as error:
            print(f"Could not save or read data: {error}")
        finally:
            # finally runs after each menu operation
            pass


if __name__ == "__main__":
    main()
