from app import create_app, db
from sqlalchemy import text

app = create_app()

def insert_sample_data():
    aircraft_inserts = [
        "INSERT INTO Aircraft (AircraftNo, Model, Capacity) VALUES ('A001', 'Boeing 747', 416);",
        "INSERT INTO Aircraft (AircraftNo, Model, Capacity) VALUES ('A002', 'Airbus A320', 180);",
        "INSERT INTO Aircraft (AircraftNo, Model, Capacity) VALUES ('A003', 'Boeing 737', 215);"
    ]
    
    airline_inserts = [
        "INSERT INTO Airline (AName, No_of_Planes) VALUES ('AirIndia', '2');",
        "INSERT INTO Airline (AName, No_of_Planes) VALUES ('Lufthansa', '3');"
    ]
    
    passenger_inserts = [
        "INSERT INTO Passenger (SeatNo, PName, Class) VALUES ('1A', 'John Doe', 'First');",
        "INSERT INTO Passenger (SeatNo, PName, Class) VALUES ('3B', 'Jane Smith', 'Business');",
        "INSERT INTO Passenger (SeatNo, PName, Class) VALUES ('15C', 'Alice Brown', 'Economy');"
    ]
    
    flight_inserts = [
        "INSERT INTO Flight (FlightNo, FlightName, Source, Destination, DeptTime, ArrTime, Duration) "
        "VALUES ('F1001', 'AI202', 'Mumbai', 'New York', '2024-11-05 10:00:00', '2024-11-05 18:30:00', 510);",
        "INSERT INTO Flight (FlightNo, FlightName, Source, Destination, DeptTime, ArrTime, Duration) "
        "VALUES ('F1002', 'LH405', 'Frankfurt', 'Delhi', '2024-11-05 12:00:00', '2024-11-05 23:30:00', 690);"
    ]
    
    isof_inserts = [
        "INSERT INTO IsOf (FlightNo, AName) VALUES ('F1001', 'AirIndia');",
        "INSERT INTO IsOf (FlightNo, AName) VALUES ('F1002', 'Lufthansa');"
    ]
    
    boards_inserts = [
        "INSERT INTO Boards (SeatNo, FlightNo) VALUES ('1A', 'F1001');",
        "INSERT INTO Boards (SeatNo, FlightNo) VALUES ('3B', 'F1002');",
        "INSERT INTO Boards (SeatNo, FlightNo) VALUES ('15C', 'F1001');"
    ]
    
    owns_inserts = [
        "INSERT INTO Owns (AircraftNo, AName) VALUES ('A001', 'AirIndia');",
        "INSERT INTO Owns (AircraftNo, AName) VALUES ('A002', 'Lufthansa');"
    ]
    
    for sql in (aircraft_inserts + airline_inserts + passenger_inserts +
                flight_inserts + isof_inserts + boards_inserts + owns_inserts):
        db.session.execute(text(sql))
    
    db.session.commit()

with app.app_context():
    db.drop_all()
    db.create_all()
    insert_sample_data()
    print("Database tables created.")
