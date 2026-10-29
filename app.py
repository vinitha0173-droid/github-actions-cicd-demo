"""Simple Python application for the CI/CD pipeline."""


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(f"2 + 3 = {add_numbers(2, 3)}")
