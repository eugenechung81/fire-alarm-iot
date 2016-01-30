import requests

r = requests.get("http://192.241.182.68:5000/smoke-detector/alert")
print r.content