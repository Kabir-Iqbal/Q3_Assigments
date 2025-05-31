# import streamlit as st
# import hashlib
# from cryptography.fernet import Fernet



# # Generate a key (this should be stored securely in production)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # In-memory data storage
# stored_data = {}  # {"user1_data": {"encrypted_text": "xyz", "passkey": "hashed"}}
# failed_attempts = 0

# # Function to hash passkey
# def hash_passkey(passkey):
#     return hashlib.sha256(passkey.encode()).hexdigest()

# # Function to encrypt data
# def encrypt_data(text, passkey):
#     return cipher.encrypt(text.encode()).decode()

# # Function to decrypt data
# def decrypt_data(encrypted_text, passkey):
#     global failed_attempts
#     hashed_passkey = hash_passkey(passkey)

#     for key, value in stored_data.items():
#         if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
#             failed_attempts = 0
#             return cipher.decrypt(encrypted_text.encode()).decode()
    
#     failed_attempts += 1
#     return None

# # Streamlit UI
# st.title("🔒 Secure Data Encryption System")

# # Navigation
# menu = ["Home", "Store Data", "Retrieve Data", "Login"]
# choice = st.sidebar.selectbox("Navigation", menu)

# if choice == "Home":
#     st.subheader("🏠 Welcome to the Secure Data System")
#     st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

# elif choice == "Store Data":
#     st.subheader("📂 Store Data Securely")
#     user_data = st.text_area("Enter Data:")
#     passkey = st.text_input("Enter Passkey:", type="password")

#     if st.button("Encrypt & Save"):
#         if user_data and passkey:
#             hashed_passkey = hash_passkey(passkey)
#             encrypted_text = encrypt_data(user_data, passkey)
#             stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
#             st.success("✅ Data stored securely!")
#         else:
#             st.error("⚠️ Both fields are required!")

# elif choice == "Retrieve Data":
#     st.subheader("🔍 Retrieve Your Data")
#     encrypted_text = st.text_area("Enter Encrypted Data:")
#     passkey = st.text_input("Enter Passkey:", type="password")

#     if st.button("Decrypt"):
#         if encrypted_text and passkey:
#             decrypted_text = decrypt_data(encrypted_text, passkey)

#             if decrypted_text:
#                 st.success(f"✅ Decrypted Data: {decrypted_text}")
#             else:
#                 st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - failed_attempts}")

#                 if failed_attempts >= 3:
#                     st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
#                     st.experimental_rerun()
#         else:
#             st.error("⚠️ Both fields are required!")

# elif choice == "Login":
#     st.subheader("🔑 Reauthorization Required")
#     login_pass = st.text_input("Enter Master Password:", type="password")

#     if st.button("Login"):
#         if login_pass == "admin123":  # Hardcoded for demo, replace with proper auth
#             global failed_attempts
#             failed_attempts = 0
#             st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
#             st.experimental_rerun()
#         else:
#             st.error("❌ Incorrect password!")

import base64
import streamlit as st 
import hashlib
import json
import os
import time
from hashlib import pbkdf2_hmac
# from base64 import urlsafe_b64decode
from cryptography.fernet import Fernet


# Data information of user

DATA_FILE = 'secure_data.json'
SALT = b'secure_salt_value'
LOKOUT_DURATION = 60

# Section login details
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None


if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state :
    st.session_state.lockout_time = 0



# if data is load 
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


def  generate_key(passkey):
    key = pbkdf2_hmac("sha256", passkey.encode(), SALT,100000)
    return Fernet(base64.urlsafe_b64encode(key))


def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()


# cryptography.fernet used

def encrypt_text(text, key):
    cipher = generate_key(key)
    return cipher.encrypt(text.encode()).decode()


def decrypt_text(encrypt_text, key):
    try:
        cipher = generate_key(key)
        return cipher.decrypt(encrypt_text.encode()).decode()
    except:
        return None
    

stored_data = load_data()

# Navigation bar 

st.title("🔒 Secure Data Encryption System")
menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data" ]
choice = st.sidebar.selectbox("Navigation", menu)


if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.markdown("""Use this app to **securely store and retrieve data** using unique passkeys""")
elif choice == "Register":
    st.subheader(" ✏️ Register new user")
    username = st.text_input("Choose Username")
    password = st.text_input("Choose password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning(" ⚠️ User already exists")
            else :
                stored_data[username] = {
                    "password" : hash_password(password),
                     "data" : []
                }
                save_data(stored_data)
                st.success(" ✅ User registered succsessfull!")

        else : 
            st.error("Both fields are required.")
elif choice == "Login":
    st.subheader("🔑 User login")

    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"⏱️ Too mainy failed attempts: please wait {remaining} seconds. ")
        st.stop()

    username = st.text_input("Username")
    password = st.text_input("password", type="password")

    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f" ✅ Welcome {username} ")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invailed Credentials! Attempts left: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOKOUT_DURATION
                st.error ("Too many failed attempts. Locked for 60 seconds")
                st.stop()


# Data store section
elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("Please Login first")
    else :
        st.subheader("📂 Store Data Securely")
        data = st.text_area("Enter Data to encrypty")
        passkey = st.text_input("Encryption key (passphrase)", type="password" )

        if st.button("Encrypt And Save"):
            encrypted = encrypt_text(data, passkey)
            stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
            save_data(stored_data)
            st.success("Data encrypted and Save sucessfuly !")
        else : 
            st.error("All fields are required to fill.")


# Data Retieve  section
elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("Please Login first")
    
    else:
        st.subheader("Retieve Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

        if not user_data:
            st.info("No data found")
        else:
            st.write("Encrypted Data Entries:")
            for i, item in enumerate(user_data, 1):
                st.code(item, language="text")
            
            encrypted_data = st.text_area("Enter Encrypted Data").strip()
            passkey = st.text_input("Enter Passkey T Descrypt", type="password")

            if st.button("Decrypt"):
                result = decrypt_text(encrypted_data, passkey)
                if result:
                    st.success(f"Decrypted Data: {result}")
                    
                else:
                    st.error("Failed to decrypt data. Please check your passkey.")



     






















