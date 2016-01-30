


class Status(object):
    def __init__(self, room_id):
        self.room_id = room_id  # e.g. "bedroom", "livingroom"
        self.occupancy = 0
        self.carbon_detected = False
        self.status = "NORMAL" # "FIRE", "NORMAL"