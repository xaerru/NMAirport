from . import db

class Aircraft(db.Model):
    __tablename__ = 'Aircraft'
    AircraftNo = db.Column(db.String(100), primary_key=True)
    Model = db.Column(db.String(100))
    Capacity = db.Column(db.Integer)

class Airline(db.Model):
    __tablename__ = 'Airline'
    AName = db.Column(db.String(100), primary_key=True)
    No_of_Planes = db.Column(db.String(100))

class Passenger(db.Model):
    __tablename__ = 'Passenger'
    SeatNo = db.Column(db.String(100), primary_key=True)
    PName = db.Column(db.String(100))
    Class = db.Column(db.Enum('First', 'Business', 'Economy'))

class Flight(db.Model):
    __tablename__ = 'Flight'
    FlightNo = db.Column(db.String(100), primary_key=True)
    FlightName = db.Column(db.String(100))
    Source = db.Column(db.String(100))
    Destination = db.Column(db.String(100))
    DeptTime = db.Column(db.DateTime)
    ArrTime = db.Column(db.DateTime)
    Duration = db.Column(db.Integer, default=0)  # Can be calculated later

class IsOf(db.Model):
    __tablename__ = 'IsOf'
    FlightNo = db.Column(db.String(100), db.ForeignKey('Flight.FlightNo'), primary_key=True)
    AName = db.Column(db.String(100), db.ForeignKey('Airline.AName'), primary_key=True)

class Boards(db.Model):
    __tablename__ = 'Boards'
    SeatNo = db.Column(db.String(100), db.ForeignKey('Passenger.SeatNo'), primary_key=True)
    FlightNo = db.Column(db.String(100), db.ForeignKey('Flight.FlightNo'))

class Owns(db.Model):
    __tablename__ = 'Owns'
    AircraftNo = db.Column(db.String(100), db.ForeignKey('Aircraft.AircraftNo'), primary_key=True)
    AName = db.Column(db.String(100), db.ForeignKey('Airline.AName'))
