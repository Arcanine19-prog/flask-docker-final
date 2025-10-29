from flask import Flask, render_template, request, redirect, url_for, jsonify
from redis import Redis
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)

# Redis connection
redis = Redis(host="redis", port=6379, decode_responses=True)

# PostgreSQL connection
db_conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "counterdb"),
    user=os.getenv("POSTGRES_USER", "admin"),
    password=os.getenv("POSTGRES_PASSWORD", "admin"),
    host="db",
    port="5432"
)
db_conn.autocommit = True
cur = db_conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS visits (
    id SERIAL PRIMARY KEY,
    ip VARCHAR(100),
    timestamp TIMESTAMP
)
""")

@app.route("/")
def index():
    count = redis.incr("hits")
    ip = request.remote_addr
    cur.execute("INSERT INTO visits (ip, timestamp) VALUES (%s, %s)", (ip, datetime.now()))
    return render_template("index.html", count=count)

@app.route("/reset")
def reset():
    redis.set("hits", 0)
    cur.execute("TRUNCATE visits")
    return redirect(url_for("index"))

@app.route("/stats")
def stats():
    cur.execute("SELECT ip, timestamp FROM visits ORDER BY timestamp DESC LIMIT 20")
    rows = cur.fetchall()
    return render_template("stats.html", visits=rows)

# API to get chart data
@app.route("/api/stats")
def api_stats():
    cur.execute("SELECT timestamp FROM visits ORDER BY timestamp")
    rows = cur.fetchall()
    data = [row[0].strftime("%Y-%m-%d %H:%M:%S") for row in rows]
    return jsonify(data)

@app.route("/api/counter")
def api_counter():
    return jsonify({"count": int(redis.get("hits") or 0)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
