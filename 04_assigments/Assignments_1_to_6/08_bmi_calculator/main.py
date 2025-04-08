import streamlit as st

# Set page config
st.set_page_config(page_title="BMI Calculator", page_icon="📏", layout="centered")

# Title and subheader
st.title("📏 BMI Calculator")
st.markdown("### Check your BMI and health status.")

# Sidebar - Inputs
st.sidebar.header("Enter Your Details")
height = st.sidebar.slider('Height (cm)', 100, 250, 170)
weight = st.sidebar.slider('Weight (kg)', 40, 200, 70)

# Add large space to push footer down
st.sidebar.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)

# Footer Divider
st.sidebar.markdown("---")

# Stylish Footer
st.sidebar.markdown("""
<div style='text-align: center; font-size: 16px; color: gray;'>
    👨‍💻 Developed by <br>
    <a href='https://www.linkedin.com/in/kabeer-iqbal' target='_blank' style='color: #4F8BF9; text-decoration: none;'>
        <b>Kabir Iqbal</b>
    </a>
</div>
""", unsafe_allow_html=True)

# BMI calculation
bmi = weight / ((height / 100) ** 2)

# Result Layout (Centered and Clean UI)
st.markdown("<br><br>", unsafe_allow_html=True)  # Adding spacing before result section
st.subheader("📊 Your Result")
st.markdown("<br>", unsafe_allow_html=True)  # Adding space before showing result

# Result Box with good design
st.markdown(f"""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; color: #2c3e50; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        💡 Your BMI is: <b>{bmi:.2f}</b>
    </div>
""", unsafe_allow_html=True)

# Determine BMI category
st.markdown("<br>", unsafe_allow_html=True)  # Spacing before category info
st.markdown("### 🧠 BMI Categories")
if bmi < 18.5:
    category = "🔹 Underweight"
elif 18.5 <= bmi < 25:
    category = "✅ Normal weight"
elif 25 <= bmi < 30:
    category = "⚠️ Overweight"
else:
    category = "❗ Obesity"

st.markdown(f"""
    <div style="background-color: #e7f9f7; padding: 15px; border-radius: 8px; font-size: 18px; color: #16a085; text-align: center;">
        🩺 Based on your BMI, you fall into the category: <b>{category}</b>
    </div>
""", unsafe_allow_html=True)

# BMI reference table
with st.expander("📚 Learn more about BMI categories"):
    st.markdown("""
    - **Underweight**: BMI less than 18.5  
    - **Normal weight**: BMI between 18.5 and 24.9  
    - **Overweight**: BMI between 25 and 29.9  
    - **Obesity**: BMI 30 or greater  
    """)
