from backend.agents.meal_planner import meal_planner
from backend.agents.grocery_agent import grocery_agent
from backend.agents.workout_planner import workout_planner
from backend.observability.tracing import start_trace

def run_full_pipeline(user_profile: dict):
    """
    Orchestrates the full pipeline:
    - Meal planner
    - Grocery list
    - Workout planner
    Adds tracing for observability.
    """
    trace = start_trace("full_pipeline")

    try:
        # Run all agents
        meal_plan = meal_planner(user_profile)
        grocery_list = grocery_agent(user_profile)
        workout_plan = workout_planner(user_profile)

        # Final result structure
        result = {
            "calories": meal_plan.get("calories"),
            "meal_plan": meal_plan,
            "grocery_list": grocery_list,
            "workout_plan": workout_plan,
        }

        # Record in tracing
        if trace:
            trace.update(output=result)

        return result

    except Exception as e:
        error_result = {"error": str(e)}

        # Log error in tracing
        if trace:
            trace.update(output=error_result)

        return error_result
