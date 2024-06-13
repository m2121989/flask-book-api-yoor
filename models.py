class HealthActivity:
    def __init__(self, id, type, duration, calories_burned, timestamp):
        self.id = id
        self.type = type
        self.duration = duration
        self.calories_burned = calories_burned
        self.timestamp = timestamp

    def __repr__(self):
        return f'<id {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'duration': self.duration,
            'calories_burned': self.calories_burned,
            'timestamp': self.timestamp
        }

