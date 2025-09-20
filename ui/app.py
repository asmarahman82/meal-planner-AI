import os
import streamlit as st
import requests

# Load backend URL from secrets
BACKEND_URL = os.getenv("BACKEND_URL") or st.secrets["BACKEND_URL"]

st.title("🥗 AI Meal & Fitness Planner")

with st.form("user_input_form"):
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    height = st.number_input("Height (cm)", min_value=120, max_value=220, value=170)
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
    activity_level = st.selectbox("Activity Level", ["low", "moderate", "high"])
    goal = st.selectbox("Goal", ["weight loss", "muscle gain", "maintenance"])
    diet = st.selectbox("Diet Preference", ["balanced", "vegetarian", "vegan", "keto"])
    duration = st.number_input("Duration (days)", min_value=1, max_value=30, value=7)

    submitted = st.form_submit_button("Generate Plan")

if submitted:
    payload = {
        "weight": weight,
        "height": height,
        "age": age,
        "activity_level": activity_level,
        "goal": goal,
        "diet": diet,
        "duration": duration,
    }

    try:
        response = requests.post(f"{BACKEND_URL}/plan", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success("✅ Plan generated!")
            st.write("### Meal Plan")
            st.table(result["meal_plan"])
            st.write("### Grocery List")
            st.table(result["grocery_list"])
            st.write("### Workout Plan")
            st.table(result["workout_plan"])
        else:
            st.error(f"🚨 API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"🚨 Backend connection failed: {e}")
