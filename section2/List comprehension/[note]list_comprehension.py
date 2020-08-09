
username_mapping = {u.username: u for u in users}

# username_mapping: for each user in users
# u: things to do inside a for loop, in this case return u


def authenticate(username, password):
    user = username_mapping.get(username, None)
    return user
# username_mapping.get(username): get the value of username key in object username_mapping


# examples squares = [i * i for i in range(10)] #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]this needs only 1 output list
# example 2
