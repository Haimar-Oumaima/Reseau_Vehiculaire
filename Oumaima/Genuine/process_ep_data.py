import json
from math import sqrt

# Chemin vers le fichier JSON
json_file_path = '/Users/oumaimahaimar/Downloads/mini_projet_1_2/ExtendedPerception/Genuine/extp_attackrate_0.100000_807.json'

# Charger le fichier JSON
with open(json_file_path) as file:
    data = json.load(file)['EP']


# Fonction pour calculer la distance euclidienne
def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Préparer les données pour le frontend
frontend_data = []

for entry in data:
    # Utiliser .get() pour éviter KeyError
    ego_position = (entry.get('Xegosumoposition'), entry.get('Yegopsumoposition'))

    # Continuer uniquement si ego_position ne contient pas de None
    if None not in ego_position:
        objects_data = []

        for obj in entry.get('Extended_Perceived_Objects', []):
            obj_position = (obj.get('Xcoordinate'), obj.get('Ycoordinate'))

            # Calculer la distance seulement si obj_position ne contient pas de None
            if None not in obj_position:
                distance = calculate_distance(*ego_position, *obj_position)
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
            'Xegosumoposition': entry.get('Xegosumoposition'),
            'Yegopsumoposition': entry.get('Yegopsumoposition'),
            'objects': objects_data
        })

# Générer le fichier HTML/JavaScript avec des colonnes pour les positions
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Perception Etendue</title>
    <style>
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }}
    </style>
</head>
<body>
    <h2>Perception Etendue</h2>
    <p id="timestamp"></p>
    <p id="stationId"></p>
    <table>
        <thead>
            <tr>
                <th>ID de l'objet</th>
                <th>Distance (m)</th>
                <th>Vitesse (m/s)</th>
                <th>Position X</th>
                <th>Position Y</th>
            </tr>
        </thead>
        <tbody id="objectsTableBody">
        </tbody>
    </table>
    <script>
        var data = {json.dumps(frontend_data)};

        function updateDisplay(index) {{
            var entry = data[index];
            document.getElementById('timestamp').innerText = 'Timestamp: ' + entry.timestamp;
            document.getElementById('stationId').innerText = 'Station ID: ' + entry.myStationId;

            var tableBody = document.getElementById('objectsTableBody');
            tableBody.innerHTML = ''; // Clear previous entries

            entry.objects.forEach(function(obj) {{
                var row = '<tr>' +
                          '<td>' + obj.PerceivedObjectID + '</td>' +
                          '<td>' + (obj.Distance ? obj.Distance.toFixed(2) : 'N/A') + '</td>' +
                          '<td>' + obj.Velocity + '</td>' +
                          '<td>' + obj.Xcoordinate + '</td>' +
                          '<td>' + obj.Ycoordinate + '</td>' +
                          '</tr>';
                tableBody.innerHTML += row;
            }});
        }}

        window.onload = function() {{
            updateDisplay(0); // Initial display
            var index = 0;
            setInterval(function() {{
                index = (index + 1) % data.length;
                updateDisplay(index);
            }}, 3000); // Update every 3 seconds
        }};
    </script>
</body>
</html>
"""

# Sauvegarder le contenu HTML dans un fichier
with open('perception_etendue.html', 'w') as html_file:
    html_file.write(html_content)