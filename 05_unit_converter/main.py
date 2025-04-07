import streamlit as st

def convert_units(value , unit_from, unit_to):

    conversions= {
        "meters_kilometers"  :    0.001,     # 1 meter  = 0.001 kilometer
        "kilometers_meters" :    1000,      # 1 kilometer = 1000 meter
        "grams_kilograms"   :    0.001,     # 1 gram  = 0.001 kilograms
        "kilograms_grams"   :    1000,      # 1 kilogram = 1000 grams
         "feet_inches"      :    12,  # 1 foot = 12 inches
        "inches_feet"       :    1/12,  # 1 inch = 0.083 feet
        "pounds_kilograms"  :    0.453592,  # 1 pound = 0.453592 kg
        "kilograms_pounds"  :    2.20462,  # 1 kg = 2.20462 pounds

    }

    key = f"{unit_from}_{unit_to}"       #genrate a key based on input and ouput units

    #logic convert to units
    if key in conversions:    
        conversion = conversions[key]
        return value * conversion
    else :
        return "Conversion not Supported"
    


st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSelectbox, .stNumberInput {
            border-radius: 5px;
            padding: 5px;
            background-color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

    

st.title("Unit Converter")

value = st.number_input("Enter the value", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms","feet", "inches", "pounds", "kilograms"])

unit_to = st.selectbox("Convert to: ", ["meters", "kilometers", "grams", "kilograms", "feet", "inches", "pounds", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {round(result,2)}")

