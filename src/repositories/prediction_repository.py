import sqlite3
from pathlib import Path
from datetime import datetime, timezone


class PredictionRepository:
    def __init__(self, db_path="outputs/prediction_logs.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.initialize()

    def initialize(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS prediction_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at_utc TEXT NOT NULL,
                    model_name TEXT NOT NULL,
                    payload TEXT NOT NULL,
                    prediction REAL NOT NULL
                )
                """
            )

            connection.commit()

    def save_prediction(self, model_name, payload, prediction):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO prediction_logs (
                    created_at_utc,
                    model_name,
                    payload,
                    prediction
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    datetime.now(timezone.utc).isoformat(),
                    model_name,
                    str(payload),
                    float(prediction),
                ),
            )

            connection.commit()

        return True

    def get_recent_predictions(self, limit=10):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, created_at_utc, model_name, payload, prediction
                FROM prediction_logs
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            )

            rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "created_at_utc": row[1],
                "model_name": row[2],
                "payload": row[3],
                "prediction": row[4],
            }
            for row in rows
        ]