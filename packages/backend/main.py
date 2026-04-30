import os
from flask import Flask, jsonify, send_from_directory

# Caminho absoluto para a pasta dist do frontend React
DIST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'apps', 'react', 'dist'))

app = Flask(__name__, static_folder=DIST_DIR, static_url_path='')

@app.route("/api")
def api_home():
    return jsonify({
        "status": "success",
        "message": "Welcome to the Flask API connected to the monorepo!"
    })

# Servir a aplicação React (Frontend)
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    # Se o arquivo existir na pasta estática (dist), servimos ele.
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    # Caso contrário, servimos o index.html (para o React Router cuidar do roteamento)
    elif os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_from_directory(app.static_folder, 'index.html')
    else:
        return jsonify({"error": "Frontend build not found. Please run 'npm run frontend:build'"}), 404

# TODO: Add database connection setup using SQLAlchemy here.

if __name__ == "__main__":
    app.run(debug=True)
