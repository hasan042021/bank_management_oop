def header(user, display):
    if display:
        print("------------------------------")
        print(f"Welcome {user.name}")
        print("------------------------------")
        return False


def decoration(display):
    if not display:
        print("------------------------------")
