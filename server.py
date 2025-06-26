from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from the browser

@app.route("/api/cell-click", methods=["POST"])
def cell_click():
    data = request.get_json()
    cell = data.get("cell")
    print(f"Received click on cell: {cell}")
    return jsonify({"status": "success", "received": cell})

if __name__ == "__main__":
    app.run(debug=True)
