import json
from math import sqrt

# Chemin vers le fichier JSON
json_file_path = 'Genuine/extp_attackrate_0.100000_807.json'

def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def prepare_data():
    with open(json_file_path) as file:
        data = json.load(file)['EP']

    frontend_data = []
    for entry in data:
        ego_position = (entry.get('Xegosumoposition'), entry.get('Yegopsumoposition'))
        objects_data = []

        for obj in entry.get('Extended_Perceived_Objects', []):
            obj_position = (obj.get('Xcoordinate'), obj.get('Ycoordinate'))
            distance = calculate_distance(*ego_position, *obj_position) if None not in obj_position else None
            objects_data.append({
                'PerceivedObjectID': obj.get('PerceivedObjectID'),
                'Xcoordinate': obj.get('Xcoordinate'),
                'Ycoordinate': obj.get('Ycoordinate'),
                'Distance': distance,
                'Velocity': obj.get('Velocity')
            })

        frontend_data.append({
            'timestamp': entry.get('timestamp'),
            'myStationId': entry.get('myStationId'),
            'objects': objects_data
        })

    return frontend_data

if __name__ == "__main__":
    data = prepare_data()
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
