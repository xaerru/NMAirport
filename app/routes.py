from flask import Blueprint, jsonify, request
from .models import db, Aircraft, Airline, Passenger, Flight

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/aircraft', methods=['GET'])
def get_aircraft():
    aircrafts = Aircraft.query.all()
    return jsonify([a.as_dict() for a in aircrafts])

@api_bp.route('/api/aircraft', methods=['POST'])
def add_aircraft():
    data = request.get_json()
    new_aircraft = Aircraft(**data)
    db.session.add(new_aircraft)
    db.session.commit()
    return jsonify(new_aircraft.as_dict()), 201

def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Aircraft.as_dict = as_dict
Airline.as_dict = as_dict
Passenger.as_dict = as_dict
Flight.as_dict = as_dict
