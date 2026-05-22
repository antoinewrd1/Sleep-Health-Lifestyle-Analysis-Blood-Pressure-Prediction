import argparse

from src.api.schemas import PredictionRequest
from src.services.prediction_service import PredictionService
from src.services.training_service import TrainingService
from src.services.monitoring_service import MonitoringService


def build_parser():
    parser = argparse.ArgumentParser(
        description="Sleep Health Blood Pressure ML Platform CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    predict_parser = subparsers.add_parser("predict")
    predict_parser.add_argument("--age", type=int, required=True)
    predict_parser.add_argument("--sleep-duration", type=float, required=True)
    predict_parser.add_argument("--quality-of-sleep", type=int, required=True)
    predict_parser.add_argument("--physical-activity-level", type=int, required=True)
    predict_parser.add_argument("--stress-level", type=int, required=True)
    predict_parser.add_argument("--heart-rate", type=int, required=True)
    predict_parser.add_argument("--daily-steps", type=int, required=True)

    subparsers.add_parser("train")
    subparsers.add_parser("test")

    schema_parser = subparsers.add_parser("schema-check")
    schema_parser.add_argument("--reference", nargs="+", required=True)
    schema_parser.add_argument("--current", nargs="+", required=True)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "predict":
        payload = PredictionRequest(
            age=args.age,
            sleep_duration=args.sleep_duration,
            quality_of_sleep=args.quality_of_sleep,
            physical_activity_level=args.physical_activity_level,
            stress_level=args.stress_level,
            heart_rate=args.heart_rate,
            daily_steps=args.daily_steps,
        )

        service = PredictionService()
        prediction = service.predict_systolic_bp(payload)

        print(
            {
                "predicted_systolic_bp": prediction,
                "model_name": service.model_name,
            }
        )

    elif args.command == "train":
        service = TrainingService()
        result = service.run_training_pipeline()
        print(result)

    elif args.command == "test":
        service = TrainingService()
        result = service.run_tests()
        print(result)

    elif args.command == "schema-check":
        service = MonitoringService()
        result = service.compare_schema(args.reference, args.current)
        print(result)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()