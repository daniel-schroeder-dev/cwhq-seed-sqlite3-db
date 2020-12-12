from make_api_request import get_random_users
from seed_users_db import seed_users_db

if __name__ == "__main__":
    users = get_random_users()

    if users:
        seed_users_db(users)
    else:
        print("Something went wrong!")

