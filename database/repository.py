"""
==================================================
Smart Travel Planning System
Trip Repository
Version : 3.0
Author  : Nikki
==================================================
"""

import sqlite3
from pathlib import Path


class TripRepository:

    def __init__(self):

        self.db_path = Path("travel.db")
        self._create_table()

    # =====================================================
    # DATABASE CONNECTION
    # =====================================================

    def _connect(self):

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    # =====================================================
    # CREATE TABLE
    # =====================================================

    def _create_table(self):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS trips(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            source TEXT NOT NULL,

            destination TEXT NOT NULL,

            route TEXT NOT NULL,

            total_distance REAL,

            preference TEXT,

            transport_mode TEXT,

            status TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        conn.commit()
        conn.close()

    # =====================================================
    # SAVE TRIP
    # =====================================================

    def save_trip(self, trip):

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO trips(

            source,

            destination,

            route,

            total_distance,

            preference,

            transport_mode,

            status

        )

        VALUES(?,?,?,?,?,?,?)

        """, (

            trip["source"],

            trip["destination"],

            " -> ".join(trip["route"]),

            trip["total_distance"],

            trip["preference"],

            trip["transport_mode"],

            trip["status"]

        ))

        conn.commit()
        conn.close()

    # =====================================================
    # GET HISTORY
    # =====================================================

    def get_all_trips(self):

        conn = self._connect()

        rows = conn.execute("""

        SELECT *

        FROM trips

        ORDER BY id DESC

        """).fetchall()

        conn.close()

        trips = []

        for row in rows:

            trips.append({

                "id": row["id"],

                "source": row["source"],

                "destination": row["destination"],

                "route": row["route"].split(" -> "),

                "distance": row["total_distance"],

                "preference": row["preference"],

                "transport_mode": row["transport_mode"],

                "status": row["status"],

                "created_at": row["created_at"]

            })

        return trips

    # =====================================================
    # ANALYTICS
    # =====================================================

    def total_trips(self):

        conn = self._connect()

        count = conn.execute(

            "SELECT COUNT(*) FROM trips"

        ).fetchone()[0]

        conn.close()

        return count

    def average_distance(self):

        conn = self._connect()

        avg = conn.execute(

            "SELECT AVG(total_distance) FROM trips"

        ).fetchone()[0]

        conn.close()

        return round(avg or 0, 2)

    def successful_trips(self):

        conn = self._connect()

        count = conn.execute("""

        SELECT COUNT(*)

        FROM trips

        WHERE status='SUCCESS'

        """).fetchone()[0]

        conn.close()

        return count

    def budget_exceeded(self):

        conn = self._connect()

        count = conn.execute("""

        SELECT COUNT(*)

        FROM trips

        WHERE status='BUDGET_EXCEEDED'

        """).fetchone()[0]

        conn.close()

        return count

    # =====================================================
    # DELETE HISTORY
    # =====================================================

    def clear_history(self):

        conn = self._connect()

        conn.execute("DELETE FROM trips")

        conn.commit()

        conn.close()