import json
from math import sqrt

# Chemin vers votre fichier JSON
json_file_path = '/Users/oumaimahaimar/Downloads/mini_projet_1_2/ExtendedPerception/Genuine/extp_attackrate_0.100000_807.json'


# Fonction pour calculer la distance euclidienne
def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Lire le fichier JSON
with open(json_file_path, 'r') as file:
    data = json.load(file)["EP"]

# Préparer une liste pour stocker les informations extraites
extracted_data = []

for entry in data:  # Correction: suppression de la boucle interne redondante
    ego_x = entry.get("Xegosumoposition")
    ego_y = entry.get("Yegopsumoposition")

    if ego_x is None or ego_y is None:
        continue  # Ignore cette entrée si les positions X ou Y ne sont pas disponibles

    if "Extended_Perceived_Objects" in entry:
        for obj in entry["Extended_Perceived_Objects"]:
            distance = calculate_distance(ego_x, ego_y, obj["Xcoordinate"], obj["Ycoordinate"])
            extracted_data.append({
                "timestamp": entry["timestamp"],
                "PerceivedObjectID": obj["PerceivedObjectID"],
                "DistanceToEgo": distance,
                "Xcoordinate": obj["Xcoordinate"],
                "Ycoordinate": obj["Ycoordinate"]
            })

# À ce stade, extracted_data contient les informations nécessaires pour chaque objet perçu
