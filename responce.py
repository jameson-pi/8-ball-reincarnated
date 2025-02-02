import requests

url = "https://ai.hackclub.com/chat/completions"
headers = {
    "Content-Type": "application/json"
}
def get_responce(prompt):

    response = requests.post(url, headers=headers, json=prompt)
    return response.json()