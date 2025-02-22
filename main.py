# Corporate Wellness App (Basic Version)
# Features: User onboarding, workout plan generator, user and admin dashboards

# Required Libraries
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Mock Database ---
users = {}  # Stores user data
workouts = {  # Sample workout plans
    "beginner": ["10-min walk", "5 push-ups", "Stretch for 5 min"],
    "intermediate": ["20-min jog", "10 push-ups", "Plank for 30 seconds"],
    "advanced": ["30-min run", "20 push-ups", "Plank for 1 minute"],
}

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")  # Landing page

@app.route("/onboard", methods=["GET", "POST"])
def onboard():
    if request.method == "POST":
        # Capture user preferences
        user_data = {
            "name": request.form["name"],
            "age": request.form["age"],
            "fitness_level": request.form["fitness_level"],
            "goal": request.form["goal"],
        }
        users[user_data["name"]] = user_data
        return jsonify({"message": "User onboarded successfully!", "user_data": user_data})
    return render_template("onboard.html")  # Onboarding form

@app.route("/workout/<username>", methods=["GET"])
def workout(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Generate workout plan based on fitness level
    fitness_level = user.get("fitness_level", "beginner").lower()
    plan = workouts.get(fitness_level, workouts["beginner"])
    return jsonify({"username": username, "workout_plan": plan})

@app.route("/admin", methods=["GET"])
def admin():
    # Admin dashboard showing user engagement stats
    user_count = len(users)
    return jsonify({"total_users": user_count, "user_data": users})

# --- Run the App ---
if __name__ == "__main__":
    app.run(debug=True)
