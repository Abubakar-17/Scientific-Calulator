import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
HISTORY_FILE = os.path.join(DATA_DIR, "history.csv")

class HistoryManager:
    def save(self, expression, result):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(HISTORY_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expression, result])

    def load(self):
        if not os.path.exists(HISTORY_FILE):
            return []

        with open(HISTORY_FILE, "r") as file:
            reader = csv.reader(file)
            return list(reader)
