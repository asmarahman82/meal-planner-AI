import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"  # FastAPI backend

st.set_page_config(page_title="AI Meal & Fitness Planner", layout="wide")
st.title("🥗 AI Meal & Fitness Planner")

# --- Sidebar: User Profile Input ---
st.sidebar.header("User Profile")

weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (cm)", min_value=120, max_value=220, value=170)
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)

activity_level = st.sidebar.selectbox("Activity Level", ["sedentary", "moderate", "active"])
goal = st.sidebar.selectbox("Goal", ["muscle gain", "weight loss", "maintenance"])
diet = st.sidebar.text_input("Diet Preference", "balanced")
duration = st.sidebar.number_input("Duration (days)", min_value=1, max_value=30, value=7)

# --- Button to Generate Plan ---
if st.sidebar.button("Generate Plan"):
    payload = {
        "weight": weight,
        "height": height,
        "age": age,
        "activity_level": activity_level,
        "goal": goal,
        "diet": diet,
        "duration": duration
    }

    with st.spinner("⚙️ Generating your full plan..."):
        try:
            response = requests.post(f"{API_URL}/plan", json=payload)
            response.raise_for_status()
            plan = response.json()
        except Exception as e:
            st.error(f"🚨 API call failed: {e}")
            plan = None

    # --- Render Results ---
    if plan:
        if "error" in plan:
            st.warning(f"⚠️ Pipeline returned an error: {plan['error']}")
        else:
            calories = plan.get("calories", "N/A")
            st.success(f"✅ Plan generated for **{goal.title()}** with estimated **{calories} calories/day**")

            # Tabs for results
            tabs = st.tabs(["🍴 Meal Plan", "🛒 Grocery List", "🏋️ Workout Plan"])

            # --- Meals ---
            with tabs[0]:
                st.subheader("Recommended Meals")
                meal_plan = plan.get("meal_plan", {})
                if "error" in meal_plan:
                    st.error(meal_plan["error"])
                else:
                    st.info(f"Meal query used: **{meal_plan.get('recommended_query', 'N/A')}**")
                    meals = meal_plan.get("meals", [])
                    if meals:
                        df_meals = pd.DataFrame(
                            [{"Meal": m.get("strMeal"), "Category": m.get("strCategory")} for m in meals]
                        )
                        st.dataframe(df_meals)
                    else:
                        st.write("No meals found.")

            # --- Groceries ---
            with tabs[1]:
                st.subheader("Shopping List")
                grocery_list = plan.get("grocery_list", [])
                if grocery_list and isinstance(grocery_list, list):
                    df_groceries = pd.DataFrame(grocery_list)
                    st.dataframe(df_groceries)
                else:
                    st.write("No grocery items found.")

                        # --- Workouts ---
            with tabs[2]:
                st.subheader("Workout Plan")
                workout_plan = plan.get("workout_plan", {})
                if "error" in workout_plan:
                    st.error(workout_plan["error"])
                else:
                    exercises = workout_plan.get("exercises", [])
                    if exercises:
                        df_workouts = pd.DataFrame(exercises)
                        st.dataframe(df_workouts)
                    else:
                        st.write("No workouts found.")

            