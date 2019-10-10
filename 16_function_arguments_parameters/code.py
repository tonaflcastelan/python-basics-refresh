# Function arguments parameters
def add(x, y):
    result = x + y
    print(result)

add(2, 3)

def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Bob")
# say_hello()  # Error, needs an argument

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=3)
divide(15, 0)
divide(15, divisor=0)  # That's OK
# divide(dividend=15, 0)  # Not OK, named arguments must go after positional arguments