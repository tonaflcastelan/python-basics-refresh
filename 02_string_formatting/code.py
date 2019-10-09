# String formatting

name = "Tona"
print(f"Hello, {name}")

name = "Bob"
print(f"Hello, {name}")


name = "Ceci"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format('Tona')
print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Ceci", "Sunday")
print(formatted)