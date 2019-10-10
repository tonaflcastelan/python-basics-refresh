# Functions
def hello():
    print("Hello!")

hello()


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 *24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")

print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")


# -- Remember function body only runs when the function is called --


def add_friend():
    friends.append("Rolf")


friends = []
add_friend()

print(friends)  # [Rolf]