# First Class functions
# A first class function just means that functions can be passed as arguments to functions.
from operator import itemgetter

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "Cannot divide!"


def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 0, operator=divide)
print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend['name']

print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend['name']))
print(search(friends, "Rolf Smith", itemgetter('name')))