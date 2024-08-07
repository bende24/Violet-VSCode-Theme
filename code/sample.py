class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Hello, World!")

    x = 10
    y = 20
    sum = add(x, y)
    print(f"Sum: {sum}")

    numbers = [1, 2, 3]
    for number in numbers:
        print(f"Number: {number}")

    person = Person("Alice")
    person.greet()

    # Lambda functions and higher-order functions
    squared_numbers = list(map(lambda n: n ** 2, numbers))
    print(f"Squared numbers: {squared_numbers}")

    # List comprehensions
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"Even numbers: {even_numbers}")
