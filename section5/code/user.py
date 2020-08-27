import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):  # self: interact with an object
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))  # always pass a tuple
        row = result.fetchone()  # get first row of sql
        if row:  # is not None
            # create user object with data from sql
            user = cls(*row)  # *row = row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):  # self: interact with an object
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))  # always pass a tuple
        row = result.fetchone()  # get first row of sql
        if row:  # is not None
            # create user object with data from sql
            user = cls(*row)  # *row = row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user
