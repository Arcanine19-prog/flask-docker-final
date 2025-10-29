**Dockerized Flask Web Application
with Redis, PostgreSQL & Nginx**

 **Project Overview**

This project is a Dockerized full-stack web application built with Flask, Redis, PostgreSQL, and Nginx.
It implements a visitor counter system where every page visit is counted in Redis and logged in PostgreSQL, displayed through a responsive frontend with Bootstrap and Chart.js.

The project demonstrates real-world multi-container orchestration using Docker Compose, simulating a production-ready microservice setup.

 **Project Motive**

The main objective of this project is to:

Learn and demonstrate containerization using Docker.

Integrate multiple backend and frontend technologies.

Build a real-time visitor counter (Redis).

Maintain persistent visit logs (PostgreSQL).

Create a modern and professional UI using Bootstrap + Chart.js.

Deploy all services through Docker Compose for a production-like architecture.

** Technologies Used**
** Backend**

Flask – Python web framework for routes, APIs, and rendering templates.

Redis – In-memory data store for fast visitor count operations.

PostgreSQL – Relational database for storing persistent visit logs.

Nginx – Reverse proxy to route requests to the Flask app.

 **Frontend**

HTML + Jinja2 – Template rendering for dynamic pages.

Bootstrap – Responsive and clean design framework.

Chart.js – JavaScript library for visit analytics visualization.

**DevOps / Deployment**

Docker – Containerization of services.

Docker Compose – Orchestration of multiple containers.

** Folder Structure**
flask-docker-final/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── templates/
│   │   ├── index.html
│   │   └── stats.html
│   └── static/
│       └── style.css
│
├── nginx/
│   └── nginx.conf
│
├── docker-compose.yml
└── README.md

** Workflow**

User opens http://localhost
 in the browser.

Nginx (port 80) forwards the request to the Flask app (port 5000).

Flask increments the counter in Redis.

Flask logs the IP address and timestamp into PostgreSQL.

Flask renders the HTML frontend with Bootstrap + Chart.js.

Users can view visit logs and analytics chart on /stats.

 **How to Run the Project**
 Step 1 — Clone the Repository
git clone https://github.com/Arcanine19-prog/flask-docker-final.git
cd flask-docker-final

 Step 2 — Run with Docker Compose
docker compose up --build

 Step 3 — Access the Application

Main Page: http://localhost
 → View visitor counter.

Stats Page: http://localhost/stats
 → View logs & analytics.

 Step 4 — Stop the Containers
docker compose down

 **Database Access (Optional)**

To open PostgreSQL database inside container:

docker exec -it flask-docker-final-db-1 psql -U admin -d counterdb


Then run:

SELECT * FROM visits;

** Docker Architecture**

Flow:
Browser → Nginx → Flask → Redis + PostgreSQL

Containers:

Service	Role
web	Flask backend
redis	In-memory counter
db	PostgreSQL database
nginx	Reverse proxy


** Future Enhancements**

Deploy on AWS/GCP using Docker or Kubernetes

Add user authentication and login system

Extend analytics dashboard with more insights

** Author**
Prasenjit Choudhury
B.Tech | VIT Chennai
📍 Agartala, Tripura
