import unittest
from health_metrics import HealthMetrics

class TestHealthMetrics(unittest.TestCase):
    def test_initial_health_metrics(self):
        health = HealthMetrics()
        self.assertEqual(health.data['weight'], 0.0)
        self.assertEqual(health.data['body_fat'], 0.0)
        self.assertEqual(health.data['calories_intake'], 0)

    def test_update_health_metrics(self):
        health = HealthMetrics()
        health.update_metrics(75, 18, 2200)
        self.assertEqual(health.data['weight'], 75)
        self.assertEqual(health.data['body_fat'], 18)
        self.assertEqual(health.data['calories_intake'], 2200)

if __name__ == '__main__':
    unittest.main()