print("Start api read application")

import requests

paginaresults = requests.get("https://catfact.ninja/facts")

feitjes = paginaresults.json()
print(feitjes['data'][0]['fact'])