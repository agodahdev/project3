import unittest
from workout import Workout

# Unit test for the Workout class
class TestWorkout(unittest.TestCase):
    def test_workout_initialization(self):
        # Create a workout instance
        workout = Workout("Running", 30, "medium", 300, "2024-10-15 14:00:00")
        # Check if the attributes are set correctly
        self.assertEqual(workout.exercise, "Running")
        self.assertEqual(workout.duration, 30)
        self.assertEqual(workout.intensity, "medium")
        self.assertEqual(workout.calories_burned, 300)
        self.assertEqual(workout.date, "2024-10-15 14:00:00")

if __name__ == '__main__':
    unittest.main()