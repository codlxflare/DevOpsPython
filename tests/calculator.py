def sum(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Calculator module")
