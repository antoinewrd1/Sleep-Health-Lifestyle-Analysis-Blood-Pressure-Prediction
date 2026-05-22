class MonitoringService:
    def compare_schema(self, reference_columns, current_columns):
        reference_set = set(reference_columns)
        current_set = set(current_columns)

        return {
            "missing_columns": sorted(reference_set - current_set),
            "new_columns": sorted(current_set - reference_set),
            "schema_matches": reference_set == current_set,
        }

    def summarize_predictions(self, predictions):
        if not predictions:
            return {
                "count": 0,
                "mean": None,
                "min": None,
                "max": None,
            }

        return {
            "count": len(predictions),
            "mean": sum(predictions) / len(predictions),
            "min": min(predictions),
            "max": max(predictions),
        }