import json

# Function to load data from JSON file
def load_data(filename="data/fitness_data.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            # Ensures health metrics are initialized with default values if they don't exist in the file
            health_metrics = data.get("health_metrics", {
                "weight": 0.0,       # Default weight
                "body_fat": 0.0,     # Default body fat percentage
                "calories_intake": 0  # Default daily calorie intake
            })
            # Return workouts, health_metrics, and goals from the file
            return data["workouts"], health_metrics, data["goals"]
    except FileNotFoundError:
        # If the file doesn't exist, return empty defaults
        return [], {"weight": 0.0, "body_fat": 0.0, "calories_intake": 0}, []

# Function to save data to JSON file
def save_data(workouts, health_metrics, goals, filename="data/fitness_data.json"):
    data = {
        "workouts": [workout.__dict__ for workout in workouts],
        "health_metrics": health_metrics,  # Save updated health metrics
        "goals": goals
    }
    with open(filename, 'w') as f:
        json.dump(data, f)