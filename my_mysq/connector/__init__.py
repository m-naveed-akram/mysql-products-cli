def connect(user, password, database, host="127.0.0.1"):

    return {
        "host": host,
        "user": user,
        "password": password,
        "database": database
    }