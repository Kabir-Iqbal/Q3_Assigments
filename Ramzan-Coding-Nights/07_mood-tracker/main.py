# import streamlit as st
# import pandas as pd      # for data manipullation
# import datetime          # handling date
# import csv               #for reading and writing csv files
# import os                # for file operation


# MOOD_FILE = "mood_log.csv"

# def load_mood_data():
#     if not os.path.exists(MOOD_FILE):
#         return pd.DataFrame(columns=["Date", "Mood"])
#     return pd.read_csv(MOOD_FILE)


# def save_mood_data(date, mood):
#     with open(MOOD_FILE, "a")as file:

#         writer = csv.writer(file)
        
#         writer.writerow([date, mood])


# st.title("Mood Tracker")

# today = datetime.date.today()

# st.subheader("How are you feeling today ?")

# mood = st.selectbox("Select your mood", ["Happy", "Sad", "Neutral", "Ängry"])

# if st.button("Log mood"):

#     save_mood_data(today, mood)
#     st.success("Mood Loggged Successfully")


# data = load_mood_data()


# if not data.empty:

#     st.subheader("Mood Trends Over Time")

#     data["Date"] = pd.to_datetime(data["Date"])

#     mood_counts =  data.groupby("Mood").count()["Date"]


#     st.bar_chart(mood_counts)


import streamlit as st # For creating web interface
import pandas as pd # For data manipulation
import datetime # For handling dates
import csv # For reading and writing CSV file
import os # For file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create empty DataFrame with columns
        return pd.DataFrame(columns=["Date", "Mood"])
    # Read and return existing mood data
    # return pd.read_csv(MOOD_FILE)
    data = pd.read_csv(MOOD_FILE, sep=",", encoding="utf-8")  # Ensure correct encoding & separator
    data.columns = data.columns.str.strip()  # Remove unwanted spaces from column names
    return data
    


# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:

        # Create CSV writer
        writer = csv.writer(file)

        # Add new mood entry
        writer.writerow([date, mood])

# Streamlit app title
st.title("Mood Tracker")

# Get today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are your feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):
    
    # Save mood when button is clicked
    save_mood_data(today, mood)

    # Show success message
    st.success("Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:

    # Create section for Visualization
    st.subheader("Mood Trends Over Time")

    # Convert date stings to datetime Objects
    data["Date"] = pd.to_datetime(data["Date"])

    # Count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)