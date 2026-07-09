# 🚆 Smart Travel Planning System

An AI-powered travel planning application that computes optimized travel routes between cities using graph algorithms, real-time APIs, and intelligent optimization strategies.

The system helps users choose the best route based on multiple preferences such as **Fastest**, **Cheapest**, **Eco-Friendly**, and **Balanced** travel while also providing travel analytics, weather information, traffic conditions, estimated cost, budget analysis, and trip history.

---

# 📌 Features

* Graph-based route optimization
* Multiple optimization strategies

  * Fastest Route
  * Cheapest Route
  * Eco Route
  * Balanced Route
* Dijkstra's Algorithm for shortest path computation
* DFS for alternative route discovery
* Real-time road distance and duration
* Live weather information
* Traffic analysis
* Budget analysis
* Travel analytics dashboard
* Trip history management
* FastAPI REST API
* Streamlit interactive dashboard
* SQLite database for storing trip history

---

# 🛠 Tech Stack

### Programming Language

* Python 3.11+

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Database

* SQLite

### Data Processing

* Pandas

### Visualization

* Plotly

### APIs

* OpenWeatherMap API
* OpenRouteService API
* Nominatim Geocoding API

### Other Libraries

* Requests
* Python Dotenv
* Pydantic
* Geopy

---

# 🧠 Algorithms Used

## Dijkstra's Algorithm

Used to compute the shortest route between cities.

## Depth First Search (DFS)

Used to generate all possible routes between the source and destination.

## Route Scoring

Each route is evaluated based on:

* Distance
* Travel Duration
* Cost

Different optimization strategies apply different scoring rules.

---

# 📂 Project Structure

```text
smart_travel_planning_system/

├── api/
│   └── main.py
│
├── algorithms/
│   ├── dijkstra.py
│   ├── dfs.py
│   └── graph_builder.py
│
├── services/
│   ├── application_controller.py
│   ├── route_optimizer.py
│   ├── route_scorer.py
│   ├── travel_intelligence_service.py
│   ├── budget_planner.py
│   ├── optimization/
│   └── external/
│
├── models/
│
├── database/
│
├── validation/
│
├── ui/
│   ├── app.py
│   └── pages/
│
├── data/
│
├── config/
│
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Optimization Strategies

## Fastest

Prioritizes minimum travel duration.

## Cheapest

Prioritizes minimum travel cost.

## Eco

Balances travel distance and cost to reduce environmental impact.

## Balanced

Considers travel distance, duration, and cost together.

---

# 🌍 External APIs

## OpenWeatherMap

Provides:

* Current weather
* Temperature
* Humidity

---

## OpenRouteService

Provides:

* Road distance
* Estimated travel duration

---

## Traffic Service

Provides estimated traffic conditions for supported cities.

---

# 💰 Budget Analysis

Users can optionally enter a maximum budget.

The application automatically determines whether the trip is:

* Within Budget
* Budget Exceeded
* No Budget Provided

---

# 📊 Analytics Dashboard

The dashboard provides:

* Total Trips
* Average Distance
* Successful Trips
* Budget Statistics
* Route Distribution
* Distance Distribution

---

# 🗄 Database

SQLite is used to store:

* Source
* Destination
* Route
* Distance
* Preference
* Transport Mode
* Status
* Created Time

---

# ▶️ Running the Project

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart_travel_planning_system.git
```

```bash
cd smart_travel_planning_system
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

Example:

```text
WEATHER_API_KEY=your_openweathermap_api_key
ORS_API_KEY=your_openrouteservice_api_key
```

---

## Run FastAPI

```bash
uvicorn api.main:app --reload
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

```bash
streamlit run ui/app.py
```

---

# 📷 Application Modules

* Trip Planning
* Trip History
* Travel Analytics
* Budget Analysis
* Weather Information
* Traffic Analysis

---

# Future Improvements

* User Authentication
* Multi-modal Transportation
* AI Travel Recommendations
* Live Traffic API Integration
* Hotel Recommendation System
* Flight Booking Integration
* Interactive Maps
* Route Caching

---

## 🚀 Live Demo

### Frontend Application
🔗 Streamlit App:
https://smart-travel-planning-system-jav2hsn4ckcxjg4mvmkjgw.streamlit.app/

### Backend API
🔗 FastAPI Server:
https://smart-travel-planning-system.onrender.com/docs

---

# 👩‍💻 Author

**Nikitha Lingapnor**

Computer Science Engineering Student

---

# 📄 License

This project is developed for educational purposes and portfolio demonstration.
