# Default parameter values

def add(x, y=3):
    print(x + y)


add(5)  # 8
add(5, 8)  # 13
add(y=3)  # Error, missing x