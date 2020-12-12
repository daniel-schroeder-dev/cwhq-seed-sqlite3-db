import requests

def get_random_users():
    api_url = "https://randomuser.me/api/"
    api_query = {
        "results": 100,
    }

    response = requests.get(api_url, api_query)
    if response.status_code >= 200 and response.status_code < 300:
        json_data = response.json()
        users = json_data["results"]
        return users
    else:
        return None



if __name__ == "__main__":
    users = get_random_users()

    if users:
        print(len(users))
    else:
        print("Something went wrong!")
