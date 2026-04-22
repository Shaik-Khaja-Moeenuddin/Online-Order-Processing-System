import uuid
from datetime import datetime

class Tracking:
    def __init__(self):
        self.tracking_id = str(uuid.uuid4())[:8]
        self.history = []

    def add_update(self, location):
        time = datetime.now().strftime("%d-%b %H:%M")
        entry = f"[{time}] {location}"
        self.history.append(entry)

    def show_tracking(self):
        print(f"\nTracking ID: {self.tracking_id}")
        print("Tracking History:")
        for h in self.history:
            print("-", h)