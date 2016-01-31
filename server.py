import sys
import utils
from flask import Flask, request, send_from_directory
from store import statuses
from twilio_api import send_message
import emailer

app = Flask(__name__)


@app.route("/")
def hello():
    return "Fire Alert System"


# @app.route("/smoke-detector/alert", methods=["POST", "GET"])
# def smoke_detector_alert():
#     # notify to police text message
#     return utils.to_json({ "status": True,
#              "message": "Alert sent!" })
#
#
# @app.route("/occupancy/count", methods=["POST", "GET"])
# def occupancy_count():
#
#     # increment count
#     counter["bedroom"] += 1
#
#     return "%s" % counter["bedroom"]


# new API
@app.route("/statuses", methods=["GET"])
def get_statuses():
    return utils.to_json(statuses.values())


@app.route("/status/<room_id>", methods=["GET"])
def get_status(room_id):
    return utils.to_json(statuses[room_id])


@app.route("/status/<room_id>", methods=["POST"])
def post_status(room_id):
    # print request.get_json()
    update_status = request.get_json()
    # update statuses
    status = statuses.get(room_id)

    # update given fields
    if update_status.get("status"):
        status.status = update_status.get("status")
        status.timestamp = utils.get_currrent_time_str()
        if update_status.get("status") == "FIRE":
            print "fire alert!"
            emailer.send_email(
                "eugenech@gmail.com, David.maiman@gmail.com, Ezafat.Khan@gmail.com, asheik91h@gmail.com, george.balayan55@gmail.com",
                "FIRE Alert! [%s]" % room_id, "Status Details: \n" + utils.to_json(status))
            # send_message("9492664065", "There is FIRE at room [%s]!" % (room_id))
    if update_status.get("occupancy"):
        status.occupancy += update_status.get("occupancy")
    if update_status.get("carbon_detected"):
        status.carbon_detected = update_status.get("carbon_detected")

    return utils.to_json({"Update": True})


@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('images', path)

### upload file



if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        app.run(
            host="0.0.0.0",
            # port=int("5000"),
            debug=True
        )
    else:
        app.run(
            host="0.0.0.0",
            threaded=True
        )
