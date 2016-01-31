import requests
import utils

BASE_DIR = "http://localhost:5000"

# get all

r = requests.get("http://localhost:5000/statuses")
print r.content

r = requests.get("http://localhost:5000/status/livingroom")
print r.content


# update

r = requests.post(
    url="http://localhost:5000/status/livingroom",
    headers={'Content-type': 'application/json'},
    data=utils.to_json({"status": "FIRE" })
)
print r.content
# send sms

r = requests.post(
    url="http://localhost:5000/status/livingroom",
    headers={'Content-type': 'application/json'},
    data=utils.to_json({"occupancy": 1 })
)
print r.content


r = requests.get("http://localhost:5000/statuses")
print r.content



###

r = requests.post(
    url="http://192.241.182.68:5000/status/livingroom",
    headers={'Content-type': 'application/json'},
    data=utils.to_json({"occupancy": 1 })
)
print r.content
