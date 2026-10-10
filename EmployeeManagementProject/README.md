# Employee Management System (Python)

A beginner-to-intermediate, interview-focused Python project. It runs using the Python standard library; no pip installations are required.

## Files

- `main.py` — menu-driven app and program entry point
- `models.py` — abstract Employee class plus Developer, Manager, and Tester
- `utils.py` — lambda, map, filter, reduce, comprehensions, generator, decorator, `*args` and `**kwargs`
- `exceptions.py` — custom exceptions
- `employees.json` — data saved by the app

## Run in VS Code

1. Download and unzip `EmployeeManagementProject.zip`.
2. In VS Code, select **File → Open Folder...** and choose the extracted `EmployeeManagementProject` folder.
3. Open **Terminal → New Terminal**.
4. Run:

   ```bash
   python3 main.py
   ```

   If `python3` is not available, try `python main.py`.

5. Choose an option from the menu. Added/updated/deleted employees are saved to `employees.json`.

No virtual environment or external package is required. If you already have a `.venv`, you can use it; activate it first if needed.

## Concepts demonstrated

- **Abstraction:** `Employee(ABC)` and `@abstractmethod`
- **Inheritance:** `Developer`, `Manager`, and `Tester` inherit from `Employee`
- **Encapsulation:** `salary` property and setter validate values before saving them to `_salary`
- **Polymorphism:** each child class overrides `calculate_bonus()`
- **Class/instance/static methods:** `get_company_name`, employee attributes, `is_valid_employee_id`
- **Constructor and `super()`**
- **Lambda:** salary sorting and filtering
- **Comprehensions:** list, dictionary, and set
- **Functional tools:** `map`, `filter`, `reduce`
- **Generator:** `yield`
- **Decorator:** `@log_execution`
- **Variable arguments:** `*args`, `**kwargs`
- **Exception handling:** `try`, `except`, `finally`, custom exceptions
- **Files and JSON:** persistent employee data
- **Other basics:** type hints, f-strings, `enumerate`, `zip`, modules/imports, `if __name__ == "__main__"`

## Suggested demo

1. Add a Developer with ID `EMP101`, name `Rahul`, salary `80000`, language `Python`.
2. Add a Manager with ID `EMP102`, name `Priya`, salary `120000`, team size `5`.
3. Add a Tester with ID `EMP103`, name `Amit`, salary `90000`, tool `Selenium`.
4. View employees, search `EMP102`, update a salary, then open Reports.
5. Exit and reopen the app to confirm that data remains in `employees.json`.

## Notes

- Employee IDs must look like `EMP101`, `EMP102`, etc.
- Salary must be greater than zero.
- This is a learning/demo application, not a production HR system.
