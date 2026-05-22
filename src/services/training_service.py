import subprocess
import sys


class TrainingService:
    def run_training_pipeline(self):
        result = subprocess.run(
            [sys.executable, "train.py"],
            capture_output=True,
            text=True,
            check=False,
        )

        return {
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0,
        }

    def run_tests(self):
        result = subprocess.run(
            [sys.executable, "-m", "pytest"],
            capture_output=True,
            text=True,
            check=False,
        )

        return {
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0,
        }