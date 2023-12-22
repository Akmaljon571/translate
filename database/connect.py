import json


def get_all():
    with open('database/db.json', 'r') as file:
        return json.load(file)


def get_one(id: str):
    with open('database/db.json', 'r') as file:
        all = json.load(file)
        for a in all:
            if a['user_id'] == id:
                return a


def create(data):
    all_data = get_all()
    all_data.append(data)
    with open('database/db.json', 'w') as file:
        json.dump(all_data, file, indent=2)


def update(id: str, new_data):
    all_data = get_all()
    for data in all_data:
        if data['user_id'] == id:
            data.update(new_data)
            with open('database/db.json', 'w') as file:
                json.dump(all_data, file, indent=2)
            return True
    return False
