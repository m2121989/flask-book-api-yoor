from flask import Flask, request, jsonify
from db import insert_data, fetch_all_data, update_data, delete_data

app = Flask(__name__)

# Endpoint to insert data into Datastore
@app.route('/insert', methods=['POST'])
def insert_health_activities():
    health_activities = request.json
    insert_data(health_activities)
    return jsonify({"message": "Data inserted successfully!"})

# Endpoint to fetch all data from Datastore
@app.route('/fetch', methods=['GET'])
def fetch_health_activities():
    activities = fetch_all_data()
    return jsonify(activities)

# Endpoint to update a health activity by ID
@app.route('/update/<int:id>', methods=['PUT'])
def update_health_activity(id):
    data = request.json
    success = update_data(id, data)
    if success:
        return jsonify({"message": "Data updated successfully!"})
    else:
        return jsonify({"message": "Data not found!"}), 404

# Endpoint to delete a health activity by ID
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_health_activity(id):
    success = delete_data(id)
    if success:
        return jsonify({"message": "Data deleted successfully!"})
    else:
        return jsonify({"message": "Data not found!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
