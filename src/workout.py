# Workout class to store workout information
class Workout:
    def __init__(self, exercise, duration, intensity, calories_burned, date):
        self.exercise = exercise
        self.duration = duration
        self.intensity = intensity
        self.calories_burned = calories_burned
        self.date = date

    # String representation of the workout for easy printing
    def __str__(self):
        return f"{self.date}: {self.exercise} for {self.duration} mins ({self.intensity} intensity) - {self.calories_burned} kcal"