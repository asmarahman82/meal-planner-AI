# 🥗 AI Meal & Fitness Planner

An **AI-powered planner** that creates personalized **meal plans, grocery lists, and workouts** based on your profile (weight, height, age, activity level, goal, diet preference, duration).
Built with **FastAPI**, **LangGraph**, **Streamlit**, and **Langfuse** for observability.

---

## 🚀 Features

- 🥘 **Meal Planning**: Personalized daily meals based on your diet and goals.
- 🛒 **Grocery List (Structured)**: Automatically generated shopping list, **grouped by categories** (e.g., Dairy, Protein, Vegetables, Fruits, Grains).
- 💪 **Workout Plan**: Tailored exercise suggestions to match your fitness goal.
- 📊 **Observability**: Metrics, logging, and tracing with **Langfuse**.
- 🎨 **Streamlit Frontend**: Simple UI with interactive input form and clean data tables.

---
## 📂 Project Structure

meal-planner-ai/
│── backend/
│ ├── agents/
│ │ ├── meal_planner.py
│ │ ├── grocery_agent.py # ✅ now returns {item, category}
│ │ ├── workout_agent.py
│ │ └── combined_pipeline.py
│ ├── api/
│ │ └── routes.py
│ ├── observability/
│ │ ├── logging_config.py
│ │ ├── metrics.py
│ │ └── tracing.py
│ └── main.py
│
│── ui/
│ └── app.py # Streamlit frontend with grouped grocery display
│
│── .streamlit/
│ └── secrets.toml
│
│── requirements.txt
│── README.md



