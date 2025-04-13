import streamlit as st
from olib.solutions import ask_model

# Setting up the Title
st.title("🕹️ AI Question Answering Bot")

st.write(
    "_**Intelligent QA bot that will answer all your questions in zero shot based on the context from the internet.**_"
)

QUESTION = st.text_input("Input Question 👇")

if st.button("Ask"):
    with st.spinner("Asking the model..."):
        answer = ask_model(QUESTION)
    st.success(answer)

st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1517841905240-472988babdf9");
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
        .stTextInput {
            background-color: #f0f0f0;
            border-radius: 5px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
