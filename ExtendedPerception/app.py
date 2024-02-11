from flask import Flask, jsonify, render_template

from test import extracted_data

app = Flask(__name__)

# Utilisez `extracted_data` de l'étape précédente ou assurez-vous de charger/analyser les données JSON ici
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    # Supposons que `extracted_data` est disponible et contient les données à afficher
    return jsonify(extracted_data)

if __name__ == "__main__":
    app.run(debug=True)
