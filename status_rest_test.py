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
r = requests.get("http://192.241.182.68:5000/statuses")
print r.content


r = requests.post(
    url="http://192.241.182.68:5000/status/livingroom",
    headers={'Content-type': 'application/json'},
    data=utils.to_json({"occupancy": 1 })
)
print r.content


### upload image

r = requests.post('http://localhost:5000/upload', files={'file': open('etc/test.png', 'rb')})
print r.text
# works

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print "Doing stuff..."
    # do your stuff
    sc.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()

## run every 60s
INTERVAL = 10
import sched, time
s = sched.scheduler(time.time, time.sleep)
def update_photo(sc):
    print "Uploading photo..."
    r = requests.post('http://localhost:5000/upload', files={'file': open('etc/test.png', 'rb')})
    print r.text
    sc.enter(INTERVAL, 1, update_photo, (sc,))

s.enter(INTERVAL, 1, update_photo, (s,))
s.run()