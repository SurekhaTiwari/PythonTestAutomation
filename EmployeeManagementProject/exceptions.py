class InvalidSalaryError(ValueError):
    """Raised when a salary is missing, invalid, or not positive."""


class EmployeeNotFoundError(LookupError):
    """Raised when an employee ID cannot be found."""
