# import streamlit as st

# def main():
#     st.title("Simple Calculator")
#     st.write("Enter your numbers and choose an operation")

#     col1, col2 = st.columns(2)

#     with col1:
#         num1 = st.number_input("Enter first number", value=0.0)
    
#     with col2:
#         num2 = st.number_input("Enter second number", value=0.0)

#     operation = st.selectbox("Choose operation", ["Addition (+)", "Subtraction (-)", "Maltiplication (x)", "Divison (/)"])

#     if st.button("Calculate"):
#         try:
#             if operation == "Addition (+)":
#                 result = num1 + num2
#                 symbol = "+"
#             elif operation == "Subtraction (-)":
#                 result = num1 - num2
#                 symbol = "-"
#             elif operation == "Maltiplication (x)":
#                 result = num1 * num2
#                 symbol = "x"
#             else :
#                 if num2 == 0:
#                     st.error("Error: Divison by zero:")
#                     return
#                 result = num1 / num2
#                 symbol = "/"

#             st.success(f"{num1} {symbol} {num2} = {result} ")

#         except Exception as e:
#             st.error(f"An error occured: {str(e)}")


# if __name__ == "__main__":
#     main()

# i




import streamlit as st

st.markdown(
    """
    <style>
    .calculator {
        background: #f9f9f9;
        height :  0px;
    
        border-radius: 10px;
        width: 250px;
        text-align: center;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
        margin: auto;
    }
    .display {
        background: black;
        color: white;
        font-size: 24px;
        padding: 10px;
        height : 35px
        text-align: right;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .btn-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        
    
    }
    .btn {
        font-size: 18px;

        border-radius: 5px;
        background: white;
        cursor: pointer;
        border: none;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .btn:hover {
        background: #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="calculator">', unsafe_allow_html=True)

if "expression" not in st.session_state:
    st.session_state.expression = ""

st.markdown(f'<div class="display">{st.session_state.expression}</div>', unsafe_allow_html=True)

buttons = [
    ["7", "8", "9", "C"],
    ["4", "5", "6", "➗"],
    ["1", "2", "3", "✖"],
    ["0", ".", "=", "➕"],
    ["(", ")", "⌫", "➖"]
]

st.markdown('<div class="btn-grid">', unsafe_allow_html=True)

for row in buttons:
    cols = st.columns(4)
    for i, button in enumerate(row):
        if cols[i].button(button, key=button):
            if button == "=":
                try:
                    # Operators کو replace کر کے eval() کو process کروانا
                    safe_expr = st.session_state.expression.replace("➕", "+").replace("➖", "-").replace("✖", "*").replace("➗", "/")
                    st.session_state.expression = str(eval(safe_expr))
                except:
                    st.session_state.expression = "Error"
            elif button == "C":
                st.session_state.expression = ""
            elif button == "⌫":
                st.session_state.expression = st.session_state.expression[:-1]
            else:
                st.session_state.expression += button
            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

             
