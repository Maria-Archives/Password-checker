def password_checker(check_pass):
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    digits = set('0123456789')
    symbols = set('*@!?')

    if len(check_pass) >= 8 and len(check_pass) <= 20 and \
            uppercase.intersection(check_pass) and \
            lowercase.intersection(check_pass) and \
            digits.intersection(check_pass) and \
            symbols.intersection(check_pass):
        return True
    else:
        return False


if __name__ == "__main__":
    tries_left = 3
    while tries_left > 0:
        password = input("Enter password: ")
        if password_checker(password):
            print("Valid password.")
            break
        else:
            tries_left -= 1
            if tries_left > 0:
                print(f"Invalid password. {tries_left} tries left.")
            else:
                print("Maximum number of tries reached.")
