import streamlit as st  # for the web interface
import random  # for randomizing the questions
import time  # for the timer

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 20px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;

        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the Application
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📝 Quiz Application</h1>", unsafe_allow_html=True)

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]

# Initialize a random question if none exists in the session state
# agr cureent question variable state m nhi he to 
if "current_question" not in st.session_state:
    # to fr current_question variable bnao or usmy question.copy daldi 
    st.session_state.current_question = questions.copy()
    # hr ek question p shuffle method list ki ui change krega taky same question na aaye
    random.shuffle(st.session_state.current_question)
    #yahan variable bnaye 
    st.session_state.current_index = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0



# Check if there are remaining questions
if st.session_state.current_index < len(st.session_state.current_question):
    question = st.session_state.current_question[st.session_state.current_index]

    # Display question
    st.markdown(f"<h2 style='color: #333; text-align: center;'>{question['question']}</h2>", unsafe_allow_html=True)
    # Create radio buttons for the options
    selected_option = st.radio("Choose your answer", question["options"], key=f"q_{st.session_state.current_index}")

    # Submit button the check the answer
    if st.button("Submit Answer"):
    # check if the answer is correct
        if selected_option == question["answer"]:
            st.success("✅ Correct!")
            st.session_state.correct_count += 1
            st.balloons()
        else:
            st.session_state.wrong_count += 1
            st.error("❌ Incorrect! the correct answer is " + question["answer"])

        # Wait for 1 second before showing the next question
        time.sleep(1)
        st.session_state.current_index += 1
        st.rerun()
else:
    # Quiz completed
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Quiz Completed 🎉</h2>", unsafe_allow_html=True)
    st.success(f"✅ Correct Answers: {st.session_state.correct_count}")
    st.error(f"❌ Wrong Answers: {st.session_state.wrong_count}")
