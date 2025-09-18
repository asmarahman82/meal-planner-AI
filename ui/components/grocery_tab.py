import streamlit as st
import requests
import json
import pandas as pd

def grocery_tab():
    st.header("🛒 Grocery List Generator")

    st.info("Upload or generate your meal plan first, then get a real grocery list.")

    meal_plan_input = st.text_area("Paste meal plan JSON", height=200)

    if st.button("Generate Grocery List"):
        try:
            meal_plan = json.loads(meal_plan_input)  # ✅ safe JSON parsing
            resp = requests.post("http://localhost:8000/grocery-list", json=meal_plan)
            
            if resp.status_code == 200:
                data = resp.json()

                # --- Display Shopping List ---
                st.subheader("Shopping List")
                st.write(data["shopping_list"])

                # --- Display Product Matches ---
                st.subheader("Matched Products")
                st.json(data["grocery_products"])

                # --- Prepare CSV ---
                df = pd.DataFrame(data["grocery_products"])
                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="📥 Download Grocery List as CSV",
                    data=csv,
                    file_name="grocery_list.csv",
                    mime="text/csv",
                )

            else:
                st.error("Failed to fetch grocery list")
        except json.JSONDecodeError:
            st.error("Invalid JSON. Please paste a valid meal plan JSON.")
        except Exception as e:
            st.error(f"Unexpected error: {e}")
