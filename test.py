import requests

r = requests.get("https://api.themoviedb.org/3")
print(r.status_code)