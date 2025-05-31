import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the API """

    try:

        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n \n {joke_data['punchline']}"
        else: 
            return "Failed to fetch API. Please try again later"
    except Exception as e:
        return f"why did programmer quit his job? \n because he didn't get array"

def main():
    st.title("Randome Joke Genrator")
    st.write("Click the button below to generate a randome joke")

    if st.button("Tell me a Joke"):
        joke = get_random_joke()
        st.success(joke)
    st.divider()

    st.markdown(
        """ 
    <div style= "text-align:center">
    <p>  Joke from Oficial Joke API </p>
    <p>Build By <a herf="https://www.linkedin.com/in/kabeer-iqbal/" >  Kabir Iqbal  </a>using Streamlit </p>
    </div>
""", 
 unsafe_allow_html=True
    )


if __name__== "__main__":
    main()