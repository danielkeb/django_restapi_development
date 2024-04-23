import requests

end_point="http://127.0.0.1:8000/website/register/"


parameters={
    "email":"daneield@gmail.com",
    "first_name":"daneield",
    "last_name":"kebede",
    "username":"danemaki",
    "password1":"@Altaye21~#%",
    "password2":"@Altaye21~#%"
}
response = requests.post(end_point,params=parameters)

print(response.text)

