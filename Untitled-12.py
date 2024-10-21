@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    try:
        alerts = Alert.query.all()
        alert_list = []
        for alert in alerts:
            alert_data = {
                "id": alert.id,
                "sensor_id": alert.sensor_id,
                "gas_type": alert.gas_type,
                "concentration": alert.concentration,
                "timestamp": alert.timestamp,
                "message": alert.message
            }
            alert_list.append(alert_data)
        return jsonify({"alerts": alert_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
