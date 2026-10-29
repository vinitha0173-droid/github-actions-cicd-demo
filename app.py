"""Small example application for the GitHub Actions CI/CD demo."""


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    """Run a tiny demonstration."""
    print(f"2 + 3 = {add_numbers(2, 3)}")


if __name__ == "__main__":
    main()
