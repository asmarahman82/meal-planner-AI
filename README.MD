# 🥗 AI Meal & Fitness Planner

An AI-powered **meal, grocery, and workout planner** built with **FastAPI**, **LangGraph**, and **Streamlit**.  
It generates personalized plans based on your **weight, height, age, activity level, goal, diet, and duration**.  

---

## 🚀 Features
- 🍴 **Meal Plan**  
- 🛒 **Grocery List**   
- 🏋️ **Workout Plan**   
- 🎯 **Personalization** → Calories estimated using your profile  
- 📊 **Observability** → Metrics, logging, and tracing (Langfuse)  
- 🖥️ **User-Friendly UI** → Powered by Streamlit  

---

## 📂 Project 
meal-planner-ai/
│── backend/
│ ├── api/
│ │ ├── routes.py
│ │ └── models.py
│ ├── agents/
│ │ ├── combined_pipeline.py
│ │ ├── meal_planner.py
│ │ ├── grocery_agent.py
│ │ └── workout_planner.py
│ ├── observability/
│ │ ├── logging_config.py
│ │ ├── metrics.py
│ │ └── tracing.py
│ └── main.py
│
│── ui/
│ └── app.py
│
│── requirements.txt
│── .env
│── README.md

