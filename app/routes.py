from flask import Blueprint, jsonify, request, render_template
from .models import db, Aircraft, Airline, Passenger, Flight, IsOf, Boards, Owns

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home_root():
    return render_template('index.html')

@home_bp.route('/view_tables')
def view_tables():
    return render_template('view_tables.html')

@home_bp.route('/insert')
def insert():
    return render_template('insert.html')

@home_bp.route('/search_flights')
def search_flights():
    return render_template('search.html')

@home_bp.route('/add_passenger')
def add_passenger():
    return render_template('add_passenger.html')

@home_bp.route('/passengers_with_flights')
def passenger_with_flight():
    return render_template('passenger_with_flight.html')

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

TABLE_MODELS = {
    'aircraft': Aircraft,
    'airline': Airline,
    'passenger': Passenger,
    'flight': Flight,
    'isof': IsOf,
    'boards': Boards,
    'owns': Owns
}

@api_bp.route('/api/all/<table_name>', methods=['GET'])
def get_all_records(table_name):
    model = TABLE_MODELS.get(table_name.lower())
    if not model:
        return jsonify({"error": "Table not found"}), 404

    records = model.query.all()
    return jsonify({
        "columns": [column.name for column in model.__table__.columns],
        "data": [record.as_dict() for record in records]
    })

@api_bp.route('/api/into/<table_name>', methods=['POST'])
def insert_into_table(table_name):
    data = request.get_json()

    table_class = globals().get(table_name)
    if table_class is None:
        return jsonify({"error": "Table not found"}), 404

    try:
        new_record = table_class(**data)
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.as_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api_bp.route('/api/flights/search', methods=['GET'])
def search_flights():
    source = request.args.get('source')
    destination = request.args.get('destination')
    
    if not source or not destination:
        return jsonify({"error": "Source and destination are required."}), 400

    flights = Flight.query.filter(
        Flight.Source.ilike(f"%{source}%"),
        Flight.Destination.ilike(f"%{destination}%")
    ).all()

    return jsonify([flight.as_dict() for flight in flights])

@api_bp.route('/api/passengers_with_flights', methods=['GET'])
def get_passengers_with_flights():
    passengers = db.session.query(Passenger, Flight).join(Boards, Passenger.SeatNo == Boards.SeatNo).join(Flight, Boards.FlightNo == Flight.FlightNo).all()

    result = []
    for passenger, flight in passengers:
        result.append({
            'SeatNo': passenger.SeatNo,
            'PName': passenger.PName,
            'Class': passenger.Class,
            'FlightNo': flight.FlightNo,
            'FlightName': flight.FlightName,
            'Source': flight.Source,
            'Destination': flight.Destination,
            'DeptTime': flight.DeptTime,
            'ArrTime': flight.ArrTime,
            'Duration': flight.Duration
        })

    return jsonify(result)

def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

for model in TABLE_MODELS.values():
    model.as_dict = as_dict
