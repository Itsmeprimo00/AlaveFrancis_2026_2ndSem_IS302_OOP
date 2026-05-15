try:
    number_JFGA = int(input("Enter a number: "))
    result_JFGA = 100 / number_JFGA
    print("Result:", result_JFGA)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")