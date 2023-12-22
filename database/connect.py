import json
import os


def path():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, 'db.json')

def get_all():
    with open(path(), 'r') as file:
        return json.load(file)


def get_one(id: int):
    with open(path(), 'r') as file:
        all = json.load(file)
        for a in all:
            if a['user_id'] == id:
                return a


def create(data):
    all_data = get_all()
    all_data.append(data)
    with open(path(), 'w') as file:
        json.dump(all_data, file, indent=2)


def update(id: int, new_data):
    all_data = get_all()
    for data in all_data:
        if data['user_id'] == id:
            data.update(new_data)
            with open(path(), 'w') as file:
                json.dump(all_data, file, indent=2)
            return True
    return False
