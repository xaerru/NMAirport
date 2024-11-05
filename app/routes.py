from flask import Blueprint, jsonify, request, render_template
from .models import db, Aircraft, Airline, Passenger, Flight, IsOf, Boards, Owns

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home_root():
    return render_template('index.html')

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/')
def api_root():
    return jsonify({
        "message": "Welcome to the Airport Management API",
        "endpoints": {
            "aircraft": "/api/aircraft",
            "flights": "/api/flights",
            "airlines": "/api/airlines",
            "passengers": "/api/passengers"
        }
    })

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

@api_bp.route('/api/airlines', methods=['GET'])
def get_airlines():
    airlines = Airline.query.all()
    return jsonify([a.as_dict() for a in airlines])

@api_bp.route('/api/airlines', methods=['POST'])
def add_airline():
    data = request.get_json()
    new_airline = Airline(**data)
    db.session.add(new_airline)
    db.session.commit()
    return jsonify(new_airline.as_dict()), 201

@api_bp.route('/api/passengers', methods=['GET'])
def get_passengers():
    passengers = Passenger.query.all()
    return jsonify([p.as_dict() for p in passengers])

@api_bp.route('/api/passengers', methods=['POST'])
def add_passenger():
    data = request.get_json()
    new_passenger = Passenger(**data)
    db.session.add(new_passenger)
    db.session.commit()
    return jsonify(new_passenger.as_dict()), 201

@api_bp.route('/api/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([f.as_dict() for f in flights])

@api_bp.route('/api/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    new_flight = Flight(**data)
    db.session.add(new_flight)
    db.session.commit()
    return jsonify(new_flight.as_dict()), 201

@api_bp.route('/api/flights/search', methods=['GET'])
def search_flights():
    source = request.args.get('source')
    destination = request.args.get('destination')
    query = Flight.query
    if source:
        query = query.filter(Flight.Source == source)
    if destination:
        query = query.filter(Flight.Destination == destination)
    flights = query.all()
    return jsonify([f.as_dict() for f in flights])

@api_bp.route('/api/isof', methods=['POST'])
def add_isof():
    data = request.get_json()
    new_isof = IsOf(**data)
    db.session.add(new_isof)
    db.session.commit()
    return jsonify(new_isof.as_dict()), 201

@api_bp.route('/api/boards', methods=['POST'])
def add_boards():
    data = request.get_json()
    new_boards = Boards(**data)
    db.session.add(new_boards)
    db.session.commit()
    return jsonify(new_boards.as_dict()), 201

@api_bp.route('/api/flight/<flight_no>/passengers', methods=['GET'])
def get_flight_passengers(flight_no):
    passengers = Passenger.query.join(Boards, Passenger.SeatNo == Boards.SeatNo).filter(Boards.FlightNo == flight_no).all()
    return jsonify([p.as_dict() for p in passengers])

# `Owns` association table endpoints
@api_bp.route('/api/owns', methods=['POST'])
def add_owns():
    data = request.get_json()
    new_owns = Owns(**data)
    db.session.add(new_owns)
    db.session.commit()
    return jsonify(new_owns.as_dict()), 201

@api_bp.route('/api/airline/<airline_name>/aircraft', methods=['GET'])
def get_airline_aircraft(airline_name):
    aircrafts = Aircraft.query.join(Owns, Aircraft.AircraftNo == Owns.AircraftNo).filter(Owns.AName == airline_name).all()
    return jsonify([a.as_dict() for a in aircrafts])

@api_bp.route('/api/flight/<flight_no>', methods=['GET'])
def get_flight_details(flight_no):
    flight = Flight.query.get_or_404(flight_no)
    return jsonify(flight.as_dict())

@api_bp.route('/api/aircraft/<aircraft_no>', methods=['GET'])
def get_aircraft_details(aircraft_no):
    aircraft = Aircraft.query.get_or_404(aircraft_no)
    return jsonify(aircraft.as_dict())
def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Aircraft.as_dict = as_dict
Airline.as_dict = as_dict
Passenger.as_dict = as_dict
Flight.as_dict = as_dict
