from flask import Flask
from occupancy import counter

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/smoke-detector/alert", methods=["POST", "GET"])
def smoke_detector_alert():
    # notify to police text message
    return "Alert!"


@app.route("/occupancy/count", methods=["POST", "GET"])
def occupancy_count():

    # increment count
    counter["bedroom"] += 1

    return "%s" % counter["bedroom"]

if __name__ == "__main__":
    app.run(debug=True)
