# import streamlit as st
# from datetime import datetime
# from zoneinfo import ZoneInfo         # used for searching time and date in world

# # List of available time zones
# TIME_ZONES = [
#     "UTC",
#     "Asia/Karachi",
#     "America/New_York",
#     "Europe/London",
#     "Asia/Tokyo",
#     "Australia/Sydney",
#     "America/Los_Angeles",
#     "Europe/Berlin",
#     "Asia/Dubai",
#     "Asia/Kolkata",
# ]

# # Create app title
# st.title("Time Zone App")

# # Create a multi-select dropdown for choosing time zones
# selected_timezone = st.multiselect(
#     "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
# )


# # Display current time for selected time zones
# st.subheader("Selected Timezones")

# for tz in selected_timezone:
#      # Get and format current time for each selected timezone with AM/PM
#     current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
#     # Display timezone and its current time
#     st.write(f"**{tz}**: {current_time}")


# # Create section for time conversion
# st.subheader("Convert Time Between Timezones")
# # Create time input field with current time as default
# current_time = st.time_input("Current Time", value=datetime.now().time())
# # Dropdown to select source timezone
# from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
# # Dropdown to select target timezone
# to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# # Create convert button and handle conversion
# if st.button("Convert Time"):
#     # Combine today's date with input time and source timezone
#     dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
#     # Convert time to target timezone and format it with AM/PM
#     converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
#     # Display the converted time with success message
#     st.success(f"Converted Time in {to_tz}: {converted_time}")

import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


# Define colors for light mode
background_color = "white"
text_color = "black"
box_color = "#f0f0f0"
button_color = "#007BFF"

# Apply Custom CSS
st.markdown(f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {background_color};
            color: {text_color};
        }}

        [data-testid="stSidebar"] {{
            background-color: {background_color};
        }}

        .main-title {{
            text-align: center;
            color: {button_color};
            font-size: 2.5em;
            font-weight: bold;
        }}

        .subheader {{
            color: {button_color};
            font-size: 1.5em;
            margin-top: 20px;
        }}

        .timezone-box {{
            background: {box_color};
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
            color: {text_color};
        }}

        .stButton>button {{
            background-color: {button_color};
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: bold;
            transition: 0.3s;
        }}

        .stButton>button:hover {{
           background-color: #0056b3;  /* گہرا نیلا، جو پہلے دیے گئے button_color سے related ہے */
           box-shadow: 0px 0px 10px #007BFF;  /* ہلکی نیلی چمک */
           color: white;
        }}

        .center-text {{
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-top: 40px;
            color: {button_color};
        }}
    </style>
""", unsafe_allow_html=True)

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Create app title
st.markdown('<div class="main-title">Time Zone App</div>', unsafe_allow_html=True)

# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.markdown('<div class="subheader">Selected Timezones</div>', unsafe_allow_html=True)

for tz in selected_timezone:
     # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display timezone and its current time
    st.markdown(f'<div class="timezone-box"><b>{tz}</b>: {current_time}</div>', unsafe_allow_html=True)

# Create section for time conversion
st.markdown('<div class="subheader">Convert Time Between Timezones</div>', unsafe_allow_html=True)

# Create time input field with current time as default
current_time = st.time_input("Current Time", value=datetime.now().time())

# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

# Dropdown to select target timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Create convert button and handle conversion
if st.button("Convert Time"):
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display the converted time with success message
    st.success(f"Converted Time in {to_tz}: {converted_time}")

# Centered Footer
st.markdown('<p class="center-text">Build By Kabir Iqbal</p>', unsafe_allow_html=True)
