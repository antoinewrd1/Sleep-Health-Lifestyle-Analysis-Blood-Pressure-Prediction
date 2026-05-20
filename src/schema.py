REQUIRED_COLUMNS = [
    "Person ID",
    "Gender",
    "Age",
    "Occupation",
    "Sleep Duration",
    "Quality of Sleep",
    "Physical Activity Level",
    "Stress Level",
    "BMI Category",
    "Blood Pressure",
    "Heart Rate",
    "Daily Steps",
    "Sleep Disorder",
]


NUMERIC_RANGE_RULES = {
    "Age": (18, 100),
    "Sleep Duration": (0, 24),
    "Quality of Sleep": (1, 10),
    "Physical Activity Level": (0, 100),
    "Stress Level": (1, 10),
    "Heart Rate": (30, 220),
    "Daily Steps": (0, 100000),
}