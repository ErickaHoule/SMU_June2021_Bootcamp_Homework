import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, jsonify
import json

#################################################
# Database Setup
#################################################
db = create_engine("sqlite:///Resources/hawaii.sqlite")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Welcome to Surf's Up - Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f'/api/v1.0/tobs<br/>'
        f"/api/v1.0/DATE(date format yyyy-mm-dd)<br/>"
        f"/api/v1.0/START/END(date format yyyy-mm-dd)"
    )

@app.route("/api/v1.0/stations")
def station():

    query = f"""
            SELECT
                *
            FROM
                station;
            """

    conn = db.connect()
    df = pd.read_sql(query, conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/precipitation")
def precipitation():

    query = f"""
            SELECT
                date,
                avg(prcp) 
            FROM
                measurement
            GROUP BY
                    date
            ORDER BY
                    date asc;
            """

    conn = db.connect()
    df = pd.read_sql(query, conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/tobs")
def temperature():

    query = f"""
                SELECT
                    station,
                    date,
                    tobs
                FROM
                    measurement
                WHERE
                    station = 'USC00519281'
                    and date >= '2016-08-23'
                ORDER BY
                    date asc;
            """
    conn = db.connect()
    df = pd.read_sql(query, conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/<start>")
def start(start):

    query = f"""
                SELECT
                    date,
                    min(tobs),
                    avg(tobs),
                    max(tobs)
                FROM
                    measurement
                WHERE
                    date = '{start}'
                GROUP BY
                    date
            """
    conn = db.connect()
    df = pd.read_sql(query, conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/<start>/<end>")
def startEnd(start, end):

    query = f"""
                SELECT
                    min(date),
                    max(date),
                    min(tobs),
                    avg(tobs),
                    max(tobs)
                FROM
                    measurement
                WHERE
                    date = '{start}'
                    and date = '{end}'
                GROUP BY
                    date
            """
    conn = db.connect()
    df = pd.read_sql(query, conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})


# Run the web app
if __name__ == "__main__":
    app.run(debug=True)