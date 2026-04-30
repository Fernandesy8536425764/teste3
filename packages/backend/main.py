from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to the Flask API connected to the monorepo!"
    })

# TODO: Add database connection setup using SQLAlchemy here.

if __name__ == "__main__":
    app.run(debug=True)
