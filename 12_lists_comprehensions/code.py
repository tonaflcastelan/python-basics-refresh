# List comprehensions

numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ["Mariana", "Luis", "Oscar", "Dave", "Sam", "Saul", "Samantha"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(friends)
print(starts_s)
print("friends: ", id(friends), "starts_s: ", id(starts_s))