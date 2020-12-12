import requests

def get_random_users():
    api_url = "https://randomuser.me/api/"

    response = requests.get(api_url)
    if response.status_code >= 200 and response.status_code < 300:
        json_data = response.json()
        users = json_data["results"]
        return users
    else:
        return None



if __name__ == "__main__":
    users = get_random_users()

    if users:
        print(users)
    else:
        print("Something went wrong!")
