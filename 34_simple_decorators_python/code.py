# Simple decorators

user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"

if user['access_level'] == 'admin':
    print(get_admin_password())


def secure_get_admin():
    if user['access_level'] == 'admin':
        print(get_admin_password())

secure_get_admin()
print(get_admin_password())



def secure_function(func):
    if user["access_level"] == "admin":
        return func


get_admin_password = secure_function(get_admin_password)
# print(get_admin_password())




def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissiomns for {user['username']}"

    return secure_function


get_admin_password = make_secure(
    get_admin_password
)

print(get_admin_password())