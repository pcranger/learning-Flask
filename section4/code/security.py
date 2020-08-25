from user import User
users = [User(1, 'bob', '1234')]

# u for u in users: List comprehension
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

userid_mapping = {1: {
    'id': 1,
    'username': 'bob',
    'password': '1234'
}
}
# map username with their coresponding id


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

# payload: content of JWT token, identify that this user with id logged in


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)


    
