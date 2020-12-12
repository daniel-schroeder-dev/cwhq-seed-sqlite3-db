from make_api_request import get_random_users

if __name__ == "__main__":
    users = get_random_users()

    if users:
        print(users[0])
    else:
        print("Something went wrong!")
