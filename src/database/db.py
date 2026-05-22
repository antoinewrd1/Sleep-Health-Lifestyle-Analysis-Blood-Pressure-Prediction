import sqlite3
from pathlib import Path
from datetime import datetime, timezone


def initialize_database(db_path="outputs/predictions.db"):
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS prediction_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at_utc TEXT NOT NULL,
                model_name TEXT NOT NULL,
                input_payload TEXT NOT NULL,
                prediction REAL NOT NULL
            )
            """
        )

        connection.commit()

    return db_path


def log_prediction(
    model_name,
    input_payload,
    prediction,
    db_path="outputs/predictions.db",
):
    db_path = initialize_database(db_path)

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO prediction_logs (
                created_at_utc,
                model_name,
                input_payload,
                prediction
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                datetime.now(timezone.utc).isoformat(),
                model_name,
                str(input_payload),
                float(prediction),
            ),
        )

        connection.commit()

    return True