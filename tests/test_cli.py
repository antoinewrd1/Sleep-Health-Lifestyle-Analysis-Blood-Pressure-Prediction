from src.cli.main import build_parser


def test_cli_parser_accepts_predict_command():
    parser = build_parser()

    args = parser.parse_args(
        [
            "predict",
            "--age",
            "40",
            "--sleep-duration",
            "7",
            "--quality-of-sleep",
            "7",
            "--physical-activity-level",
            "50",
            "--stress-level",
            "5",
            "--heart-rate",
            "75",
            "--daily-steps",
            "7000",
        ]
    )

    assert args.command == "predict"
    assert args.age == 40


def test_cli_parser_accepts_schema_check_command():
    parser = build_parser()

    args = parser.parse_args(
        [
            "schema-check",
            "--reference",
            "Age",
            "Stress",
            "--current",
            "Age",
        ]
    )

    assert args.command == "schema-check"
    assert args.reference == ["Age", "Stress"]