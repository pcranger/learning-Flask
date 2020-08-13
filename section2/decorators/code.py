import functools

# decorator to secure dictionary
user = {"username": "jose", "access_level": "guest"}


@make_secure
def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"NO admin permissions for username {user['username']}"


user = {"username": "bob", "access_level": "admin"}

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
