from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models from models.py
from models import GasData

# Gas concentration thresholds (in ppm or % based on gas type)
GAS_THRESHOLDS = {
    "Methane": 5.0,         # Example: 5% in air
    "Carbon Monoxide": 50.0, # Example: 50 ppm
    "Hydrogen Sulfide": 10.0 # Example: 10 ppm
}

# Home route to test API
@app.route('/')
def index():
    return "Toxic Gas Detection API"

# Route to receive gas sensor data and check for threshold breaches
@app.route('/api/sensor', methods=['POST'])
def receive_sensor_data():
    try:
        data = request.get_json()
        gas_type = data['gas_type']
        concentration = data['concentration']
        sensor_id = data['sensor_id']
        
        # Check if the gas type has a defined threshold
        if gas_type in GAS_THRESHOLDS:
            threshold = GAS_THRESHOLDS[gas_type]
            if concentration > threshold:
                alert_message = f"ALERT: {gas_type} level of {concentration} exceeds safe threshold of {threshold}!"
                # Here we can trigger real-time notifications, send SMS, etc.
                # For now, just log the alert to the response.
                return jsonify({
                    "message": "Data received successfully",
                    "alert": alert_message
                }), 201

        # Save data to the database
        new_entry = GasData(sensor_id=sensor_id, gas_type=gas_type, concentration=concentration)
        db.session.add(new_entry)
        db.session.commit()
        
        return jsonify({"message": "Data received successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
