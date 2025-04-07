import streamlit as st
import random
import string

# Function to calculate password entropy
def calculate_entropy(password):
    length = len(password)
    character_sets = 0

    if any(c.islower() for c in password):
        character_sets += 26  # Lowercase letters
    if any(c.isupper() for c in password):
        character_sets += 26  # Uppercase letters
    if any(c.isdigit() for c in password):
        character_sets += 10  # Digits
    if any(c in string.punctuation for c in password):
        character_sets += len(string.punctuation)  # Special characters

    return character_sets if character_sets else 0  # Handle empty password case

# Page Title & Styling
st.set_page_config(page_title="Password Strength Checker & Generator", page_icon="🔐", layout="centered")
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            color: #4CAF50;
        }
        .stButton > button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
        .generated-pass {
            font-size: 1.2em;
            font-weight: bold;
            color: #FF5722;
            text-align: center;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 20px;
            color: #888;
            margin-top: 40px
        }
    </style>
""", unsafe_allow_html=True)

# Password Strength Checker
st.markdown("<div class='main-title'>🔐 Password Strength Checker</div>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    entropy = calculate_entropy(password)
    strength = "Weak 🔴" if entropy < 40 else "Moderate 🟠" if entropy < 60 else "Strong 🟢"
    st.success(f"**Password Strength:** {strength}")
    st.info(f"**Entropy:** {entropy:.2f} bits")

st.markdown("---")

# Password Generator
st.markdown("<div class='main-title'>🔑 Password Generator</div>", unsafe_allow_html=True)
length = st.slider("Select password length", min_value=6, max_value=30, value=12)
use_digit = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

def generate_password(length, use_digit, use_special):
    characters = string.ascii_letters
    if use_digit:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if st.button("Generate Password"):
    generated_password = generate_password(length, use_digit, use_special)
    st.markdown(f"""
        <div style="
            background-color: #e8f5e9;
            color: #388e3c;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 1.2em;
            font-weight: bold;
        ">
             {generated_password}
        </div>
    """, unsafe_allow_html=True)

# Footer
# st.markdown("<p class='footer'>🚀 Built by <b>Kabir Iqbal</b></p>", unsafe_allow_html=True)
st.markdown("""
    <div style="
        text-align: center;
        font-size: 14px;
        margin-top: 30px;
        color: #888;
    ">
        🚀 Built by <b>Kabir Iqbal</b>
    </div>
""", unsafe_allow_html=True)

