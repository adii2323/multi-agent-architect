def user_login(username, password):
    # Add validation check here
    if username == 'admin' and password == 'password':
        return True
    else:
        return False