import requests

url = "http://127.0.01:8000/drinks/"


headers = {'Content-Type': 'application/json'}
data = {'key': 'value'}

response = requests.get(url, headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
