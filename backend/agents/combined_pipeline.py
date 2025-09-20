from backend.agents.meal_planner import generate_meal_plan
from backend.agents.grocery_agent import generate_grocery_list
from backend.agents.workout_agent import generate_workout_plan
from backend.observability.tracing import start_trace, log_event, end_trace

def run_full_pipeline(user_input: dict):
    """
    Run the full pipeline: meal plan → grocery list → workout plan.
    Returns a dict with keys ready for Streamlit tables.
    """
    trace_id = start_trace("full_pipeline")

    try:
        # --- Meal Plan ---
        log_event(trace_id, "Generating meal plan...")
        meal_plan = generate_meal_plan(user_input)

        # Ensure tabular format
        meal_plan_table = [
            {
                "Meal": m.get("name", ""),
                "Calories": m.get("calories", ""),
                "Protein (g)": m.get("protein", ""),
                "Carbs (g)": m.get("carbs", ""),
                "Fat (g)": m.get("fat", "")
            }
            for m in meal_plan
        ]

        # --- Grocery List ---
        log_event(trace_id, "Generating grocery list...")
        grocery_list = generate_grocery_list(user_input)

        grocery_table = [
            {
                "Item": g.get("item", ""),
                "Quantity": g.get("quantity", ""),
                "Unit": g.get("unit", "")
            }
            for g in grocery_list
        ]

        # --- Workout Plan ---
        log_event(trace_id, "Generating workout plan...")
        workout_plan = generate_workout_plan(user_input)

        workout_table = [
            {
                "Day": w.get("day", ""),
                "Exercise": w.get("exercise", ""),
                "Sets": w.get("sets", ""),
                "Reps": w.get("reps", "")
            }
            for w in workout_plan
        ]

        log_event(trace_id, "Pipeline completed successfully")

        return {
            "meal_plan": meal_plan_table,
            "grocery_list": grocery_table,
            "workout_plan": workout_table,
        }

    except Exception as e:
        log_event(trace_id, f"Pipeline failed: {e}")
        return {"error": str(e)}

    finally:
        end_trace(trace_id)

