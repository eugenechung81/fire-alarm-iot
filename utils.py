import json
from datetime import datetime

def to_json(obj, pretty=True):
    class DefaultEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__

    # return json.dumps(cls=DefaultEncoder, obj=obj, indent=2 if pretty else None, sort_keys=True)
    return json.dumps(cls=DefaultEncoder, obj=obj, indent=2 if pretty else None)


def from_json(str):
    return json.loads(str)

def get_currrent_time_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')