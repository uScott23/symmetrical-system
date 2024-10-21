from app import db

class GasData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(50), nullable=False)
    gas_type = db.Column(db.String(50), nullable=False)
    concentration = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<GasData {self.gas_type}, {self.concentration}>"
