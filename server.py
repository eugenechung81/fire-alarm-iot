import sys
import utils
from flask import Flask
from occupancy import counter

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/smoke-detector/alert", methods=["POST", "GET"])
def smoke_detector_alert():
    # notify to police text message
    return utils.to_json({ "status": True,
             "message": "Alert sent!" })


@app.route("/occupancy/count", methods=["POST", "GET"])
def occupancy_count():

    # increment count
    counter["bedroom"] += 1

    return "%s" % counter["bedroom"]

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
