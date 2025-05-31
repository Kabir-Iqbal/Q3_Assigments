import streamlit as st
import random
import time
import requests

# Custom CSS for Styling
st.markdown(
    """
    <style>
        /* Background and Font Styling */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
        }
        .stApp {
            background-color: #f8f9fa;
        }
        /* Title Styling */
        h1 {
            color: #007bff;
            text-align: center;
        }
        /* Buttons */
        .stButton>button {
            background: linear-gradient(45deg, #ff4b2b, #ff416c);
            color: white;
            padding: 10px 24px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
        /* Money Text Animation */
        .money-text {
            font-size: 32px;
            font-weight: bold;
            color: green;
            text-align: center;
            animation: fadeIn 1s ease-in-out;
        }
        /* Quote Box */
        .quote-box {
            background: #007bff;
            color: white;
            padding: 10px;
            border-radius: 8px;
            font-size: 18px;
            text-align: center;
            margin-top: 10px;
        }
        /* Fade-in Animation */
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💰 Money Making Machine")

def genrated_money():
    return random.randint(1, 1000)

st.subheader("💸 Instant Cash Generator")

if st.button("🎰 Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = genrated_money()
    st.markdown(f'<p class="money-text">You made ${amount} 🤑</p>', unsafe_allow_html=True)

# API: Getting Side Hustles
def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return "Freelancing"
    except:
        return "Something went wrong"

st.subheader("💼 Get a Side Hustle Idea")

if st.button("💡 Get Idea"):
    idea = fetch_side_hustles()
    st.success(idea)

# API: Getting Money Quotes
def fetch_Money_Qoutes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            Qoute = response.json()
            return Qoute["money_quotes"]
        else:
            return "Success is not about money; it's about impact."
    except:
        return "Wealth is the ability to fully experience life. - Henry David Thoreau"

st.subheader("📜 Get Money Quotes")

if st.button("📖 Get Money Quote"):
    ideas = fetch_Money_Qoutes()
    st.markdown(f'<div class="quote-box">"{ideas}"</div>', unsafe_allow_html=True)




# import streamlit as st
# import random
# import time
# import requests

# # Custom CSS for a Professional Look
# st.markdown(
#     """
#     <style>
#         /* Import Google Font */
#         @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

#         body {
#             font-family: 'Poppins', sans-serif;
#             background-color: #f9f9f9;
#         }
#         .stApp {
#             background-color: white;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
#         }
#         /* Title Styling */
#         h1 {
#             color: #2c3e50;
#             text-align: center;
#             font-weight: 600;
#         }
#         /* Buttons */
#         .stButton>button {
#             background: linear-gradient(90deg, #007bff, #00c6ff);
#             color: white;
#             padding: 12px 26px;
#             font-size: 16px;
#             font-weight: bold;
#             border-radius: 6px;
#             border: none;
#             transition: all 0.3s ease-in-out;
#             cursor: pointer;
#         }
#         .stButton>button:hover {
#             transform: scale(1.06);
#             box-shadow: 0px 6px 12px rgba(0, 123, 255, 0.3);
#         }
#         /* Money Display */
#         .money-box {
#             font-size: 28px;
#             font-weight: bold;
#             color: #27ae60;
#             text-align: center;
#             padding: 10px;
#             margin-top: 10px;
#             background: #ecf8f1;
#             border-radius: 8px;
#             border-left: 6px solid #2ecc71;
#             animation: fadeIn 0.8s ease-in-out;
#         }
#         /* Quote Box */
#         .quote-box {
#             background: #007bff;
#             color: white;
#             padding: 15px;
#             border-radius: 8px;
#             font-size: 18px;
#             text-align: center;
#             margin-top: 10px;
#             font-style: italic;
#             box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.2);
#         }
#         /* Fade-in Animation */
#         @keyframes fadeIn {
#             from {opacity: 0;}
#             to {opacity: 1;}
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Application Title
# st.title("💰 Money Making Machine")

# # Generate Money Function
# def generate_money():
#     return random.randint(50, 5000)  # Increased range for realism

# st.subheader("💸 Instant Cash Generator")

# if st.button("💵 Generate Money"):
#     st.write("💰 Counting your cash...")
#     time.sleep(1)
#     amount = generate_money()
#     st.markdown(f'<div class="money-box">You earned ${amount} 🎉</div>', unsafe_allow_html=True)

# # API: Fetch Side Hustles
# def fetch_side_hustles():
#     try:
#         response = requests.get("http://127.0.0.1:8000/side_hustles")
#         if response.status_code == 200:
#             hustles = response.json()
#             return hustles["side_hustles"]
#         else:
#             return "Freelancing"
#     except:
#         return "Something went wrong"

# st.subheader("💼 Get a Side Hustle Idea")

# if st.button("💡 Get Idea"):
#     idea = fetch_side_hustles()
#     st.success(f"💡 {idea}")

# # API: Fetch Money Quotes
# def fetch_money_quotes():
#     try:
#         response = requests.get("http://127.0.0.1:8000/money_quotes")
#         if response.status_code == 200:
#             quote = response.json()
#             return quote["money_quotes"]
#         else:
#             return "Success is not about money; it's about impact."
#     except:
#         return "Wealth is the ability to fully experience life. - Henry David Thoreau"

# st.subheader("📜 Get Money Quotes")

# if st.button("📖 Get Money Quote"):
#     quote = fetch_money_quotes()
#     st.markdown(f'<div class="quote-box">"{quote}"</div>', unsafe_allow_html=True)
