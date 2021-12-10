import requests
import json

r = requests.get("http://api:8000/api")
j = json.loads(r.text)
print("O nome do filme é", j["movie"])
