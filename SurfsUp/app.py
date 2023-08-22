# CELL CODE BLOCK 1
# Import the dependencies
from flask import Flask, jsonify
import datetime as dt

# CELL CODE BLOCK 2
#################################################
# Database Setup
#################################################
# Import necessary dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# CELL CODE BLOCK 3
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# CELL CODE BLOCK 4
# Reflect the existing database into a new model
Base = automap_base()

# CELL CODE BLOCK 5
# Reflect the tables
Base.prepare(engine, reflect=True)

# CELL CODE BLOCK 6
# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# CELL CODE BLOCK 7
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# CELL CODE BLOCK 8
#################################################
# Flask Routes
#################################################

# Homepage route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a new session for this request
    session = Session(engine)
    
    # Calculate the date one year ago from the most recent date in the database
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d') - dt.timedelta(days=365)
    
    # Query for precipitation data
    precipitation_results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    
    # Close the session
    session.close()
    
    # Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_results}
    
    return jsonify(precipitation_dict)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Create a new session for this request
    session = Session(engine)
    
    stations_query = session.query(Station.station).all()
    stations_list = [station[0] for station in stations_query]
    
    # Close the session
    session.close()
    
    return jsonify(stations_list)

# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    # Create a new session for this request
    session = Session(engine)
    
    # Calculate the date one year ago from the most recent date in the database
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d') - dt.timedelta(days=365)
    
    # Query for temperature data
    temperature_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == "USC00519281", Measurement.date >= one_year_ago).all()
    
    # Close the session
    session.close()
    
    temperature_list = [{"date": date, "tobs": tobs} for date, tobs in temperature_results]
    
    return jsonify(temperature_list)

# Start date route
@app.route("/api/v1.0/<start>")
def start_date_summary(start):
    # Create a new session for this request
    session = Session(engine)
    
    summary_results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    # Close the session
    session.close()
    
    summary_dict = {
        "TMIN": summary_results[0][0],
        "TMAX": summary_results[0][1],
        "TAVG": summary_results[0][2]
    }
    
    return jsonify(summary_dict)

# Start-end date route
@app.route("/api/v1.0/<start>/<end>")
def start_end_date_summary(start, end):
    # Create a new session for this request
    session = Session(engine)
    
    summary_results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start, Measurement.date <= end).all()
    
    # Close the session
    session.close()
    
    summary_dict = {
        "TMIN": summary_results[0][0],
        "TMAX": summary_results[0][1],
        "TAVG": summary_results[0][2]
    }
    
    return jsonify(summary_dict)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


