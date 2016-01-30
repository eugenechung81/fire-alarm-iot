# Data Model

Status
{
    "status": "NORMAL",
    "room_id": "livingroom",
    "occupancy": 0,
    "carbon_detected": false
}

# APIs

## All Statuses

GET /statuses
[
  {
    "status": "NORMAL",
    "room_id": "livingroom",
    "occupancy": 0,
    "carbon_detected": false
  },
  {
    "status": "NORMAL",
    "room_id": "bedroom",
    "occupancy": 0,
    "carbon_detected": false
  }
]

## Get Status by Id

GET /status/livingroom
{
  "status": "NORMAL",
  "room_id": "livingroom",
  "occupancy": 0,
  "carbon_detected": false
}

## Update Status

POST /status/livingroom
{
    "status": "FIRE"
}

POST /status/livingroom
{
    "occupancy": 1
}

# Deployment

http://192.241.182.68:5000/
