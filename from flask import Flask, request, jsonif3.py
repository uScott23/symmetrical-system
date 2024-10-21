from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuration settings (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models from models.py
from models import GasData

# Home route to test the API is working
@app.route('/')
def index():
    return "Toxic Gas Detection API"

# Route to receive gas sensor data
@app.route('/api/sensor', methods=['POST'])
def receive_sensor_data():
    try:
        data = request.get_json()
        gas_type = data['gas_type']
        concentration = data['concentration']
        sensor_id = data['sensor_id']
        
        # Save to database
        new_entry = GasData(sensor_id=sensor_id, gas_type=gas_type, concentration=concentration)
        db.session.add(new_entry)
        db.session.commit()
        
        return jsonify({"message": "Data received successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
