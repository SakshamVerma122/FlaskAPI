from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"

# Sending a get request to the BASE URL
response = requests.get(BASE+"helloworld")

print(response.json())