import sqlite3

from src.database.db import initialize_database, log_prediction


def test_initialize_database_creates_file(tmp_path):
    db_path = tmp_path / "predictions.db"

    result = initialize_database(db_path)

    assert result.exists()


def test_log_prediction_inserts_record(tmp_path):
    db_path = tmp_path / "predictions.db"

    log_prediction(
        model_name="test_model",
        input_payload={"age": 40},
        prediction=120.5,
        db_path=db_path,
    )

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM prediction_logs")
        count = cursor.fetchone()[0]

    assert count == 1