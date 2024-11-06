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
    model = TABLE_MODELS.get(table_name.lower())
    if not model:
        return jsonify({"error": "Table not found"}), 404

    data = request.get_json()
    try:
        new_record = model(**data)
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.as_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "IntegrityError - possible duplicate primary key or constraint violation"}), 400
    except Exception as e:
        db.session.rollback()
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

def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

for model in TABLE_MODELS.values():
    model.as_dict = as_dict
