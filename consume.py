import requests

url = "http://127.0.01:8000/register/"


headers = {'Content-Type': 'application/json'}
data = {'key': 'value'}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
