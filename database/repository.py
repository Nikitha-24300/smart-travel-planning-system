import sqlite3
from pathlib import Path


class TripRepository:

    def __init__(self):

        self.db_path = Path("travel.db")
        self._create_table()

    def _connect(self):

        return sqlite3.connect(self.db_path)

    def _create_table(self):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                destination TEXT,
                route TEXT,
                total_distance REAL,
                preference TEXT,
                status TEXT
            )
        """)

        conn.commit()
        conn.close()

    def save_trip(self, trip_data: dict):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO trips (
                source,
                destination,
                route,
                total_distance,
                preference,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            trip_data["source"],
            trip_data["destination"],
            " -> ".join(trip_data["route"]),
            trip_data["total_distance"],
            trip_data["preference"],
            trip_data["status"]
        ))

        conn.commit()
        conn.close()

    def get_all_trips(self):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT source, destination, route, total_distance, preference, status
            FROM trips
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()
        return rows