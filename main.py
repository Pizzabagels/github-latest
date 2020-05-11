import sys
import json
import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    user = input("Please specify User ")
    try:
        response = requests.get(f"https://api.github.com/users/{user}/events")
        events = json.loads(response.content)
        output = (events[0]['created_at'])
        print(f'last commit from {user} at {output}')
    except IndexError:
        print("User not found")
    


