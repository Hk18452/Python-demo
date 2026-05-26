def login(username,password):
    if username == "admin" and password == "1234":
        return True
    return False


def register(username):
    if len(username) < 3:
        return "successfull failed"
    return "successfull succeeded"