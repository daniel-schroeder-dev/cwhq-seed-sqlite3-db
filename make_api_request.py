import requests

def get_random_users():
    """
    I don't need all the user information.
    All I want is:
        first name
        last name
        gender
        age
    """
    api_url = "https://randomuser.me/api/"
    api_query = {
        "results": 100,
        "inc": "gender,name,dob"
    }

    response = requests.get(api_url, api_query)
    if response.status_code >= 200 and response.status_code < 300:
        json_data = response.json()
        users = json_data["results"]
        return users
    else:
        return None



