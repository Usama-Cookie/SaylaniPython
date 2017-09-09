''' Write a function to compute 5/0 and use try/except to catch the
exceptions.
Hints:
Use try/except to catch exceptions. '''


def division():
    return 5/0

try:
    division()
except ZeroDivisionError:
    print("Can't Divide by zero!")
