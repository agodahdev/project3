# HealthMetrics class to track weight, body fat, and daily calorie intake
class HealthMetrics:
    def __init__(self):
        # Initialize health metrics with default values to avoid KeyErrors
        self.data = {
            "weight": 0.0,           # Default weight
            "body_fat": 0.0,         # Default body fat percentage
            "calories_intake": 0      # Default daily calorie intake
        }

    def update_metrics(self, weight, body_fat, calories_intake):
        # Update metrics with new values provided by the user
        self.data["weight"] = weight
        self.data["body_fat"] = body_fat
        self.data["calories_intake"] = calories_intake

    def __str__(self):
        # Return a string representation of the health metrics
        return f"Weight: {self.data['weight']} kg, Body Fat: {self.data['body_fat']}%, Daily Calorie Intake: {self.data['calories_intake']} kcal"