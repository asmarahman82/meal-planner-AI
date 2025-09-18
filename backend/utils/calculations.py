def calculate_calories(profile: dict) -> int:
    """
    Estimate daily calorie needs based on weight, height, age, activity, goal.
    Using Mifflin–St Jeor Equation (male as default).
    """
    weight = profile.get("weight", 70)   # kg
    height = profile.get("height", 170)  # cm
    age = profile.get("age", 25)         # years
    activity = profile.get("activity_level", "moderate")
    goal = profile.get("goal", "maintenance")

    # BMR calculation (Mifflin–St Jeor, male)
    bmr = 10 * weight + 6.25 * height - 5 * age + 5  

    # Activity factors
    activity_map = {
        "sedentary": 1.2,
        "moderate": 1.55,
        "active": 1.725
    }
    tdee = bmr * activity_map.get(activity, 1.55)

    # Adjust for goal
    if goal.lower() == "weight loss":
        tdee -= 500
    elif goal.lower() == "muscle gain":
        tdee += 300

    return int(tdee)
