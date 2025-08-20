from agents import Agent, Runner, function_tool
from connection import config
import requests
import streamlit as st
import asyncio



# Function to fetch real-time crypto price (example: Coinbase API)
@function_tool
def get_crypto_price(crypto="BTC", currency="USD"):     # default usd, btc 
    try:
        # fetching real time price from Coinbase API
        response = requests.get(f"https://api.coinbase.com/v2/prices/{crypto}-{currency}/spot")
        data = response.json()
        return f"Current {crypto} price in {currency}: {data['data']['amount']}"
    except Exception as e:
        return f"Error fetching price: {str(e)}"



# Function to simulate a trade (placeholder)
@function_tool
def execute_trade(crypto="BTC", amount=1, target="USDT"):
    # Placeholder: In real project, integrate with exchange API
    return f"Simulated trade: {amount} {crypto} converted to {target}"



# Define agent tool
# natural language handler if in price in query will called "get_crypto_price" function ,, if in query is trade will called "execute_trade" this function
@function_tool
def crypto_tool(query):
    if "price" in query.lower():
        return get_crypto_price()
    elif "trade" in query.lower() or "convert" in query.lower():
        return execute_trade()
    return "Sorry, I can only handle price checks or trades."


# Agent setup
agent = Agent(
    name="CryptoExchangeAgent",
    instructions="You are a crypto exchange assistant. Help users check prices or execute trades using natural language.",
    tools=[get_crypto_price, execute_trade, crypto_tool]
)


# Terminal Base Code
# result = Runner.run_sync(
#     agent,
#     'What is the price of BTC in euro?',
#     run_config = config

# )
# print(result.final_output)


# # Streamlit UI
# st.title("💱 Crypto Exchange Assistant")

# user_input = st.text_input("Enter your query (e.g. 'Price of BTC in EUR'):")

# if st.button("Submit"):
#     if user_input:
#         # result = Runner.run_sync(agent, user_input, run_config=config)
#         # st.success(result.final_output)
#         async def run_agent():
#             return await Runner.run(agent, user_input, run_config=config)

#         result = asyncio.run(run_agent())
#         st.success(result.final_output)
#     else:
#         st.warning("Please enter a query.")



# Page configuration for a professional look
st.set_page_config(
    page_title="Crypto Exchange Assistant",
    page_icon="💱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for attractive and professional styling
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: 0 auto;
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
        padding: 12px;
        border: 2px solid #4b5eAA;
        font-size: 16px;
        transition: border-color 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #3a4a88;
        box-shadow: 0 0 8px rgba(75, 94, 170, 0.2);
    }
    .stButton > button {
        background-color: #4b5eAA;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #3a4a88;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    .title {
        color: #2c3e50;
        font-size: 2.2em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #34495e;
        font-size: 1.1em;
        text-align: center;
        margin-bottom: 30px;
    }
    .success-box {
        background-color: #e8f4f8;
        border-left: 5px solid #4b5eAA;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
        font-size: 16px;
    }
    .warning-box {
        background-color: #fef6e7;
        border-left: 5px solid #f4b400;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
        font-size: 16px;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        font-size: 0.9em;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown('<div class="title">💱 Crypto Exchange Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Real-time crypto prices and trade simulations</div>', unsafe_allow_html=True)

# Input form
with st.container():
    user_input = st.text_input(
        "Enter your query (e.g., 'Price of BTC in EUR')",
        placeholder="Type your crypto query here...",
        key="crypto_query"
    )

    if st.button("Submit"):
        if user_input:
            with st.spinner("Processing your query..."):
                try:
                    async def run_agent():
                        return await Runner.run(agent, user_input, run_config=config)

                    result = asyncio.run(run_agent())
                    st.markdown(f'<div class="success-box">{result.final_output}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(f'<div class="warning-box">Error: {str(e)}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-box">Please enter a query.</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Powered by xAI | © 2025 Crypto Exchange Assistant</div>', unsafe_allow_html=True)