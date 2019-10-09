# If statements with the in keyword
# movies_watched = {"Endgame", "TLoR", "Matrix"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too")
# else:
#     print(f"I haven't watched that yet")


number = 7
user_input = input("Enter 'y' of you would like to play: ").lower()

if user_input == 'y':
    user_number = int(input("Guess or number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1:
        print("You were of by one")
    else:
        print("sorry, it's wrong")