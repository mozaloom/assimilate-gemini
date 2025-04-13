import streamlit as st
from olib.solutions import create_code


st.title("Code Generation Web App")
st.write(
    "This web app generates code snippets based on the programming language and prompt you provide."
)
st.write(
    "Enter a programming language and a prompt, then click the button to generate code."
)


lang = st.text_input("Enter the programming language (e.g., Python, JavaScript): ")
prompt = st.text_area("Enter the prompt for code generation:")


if st.button("Generate Code"):
    if lang and prompt:
        code = create_code(lang, prompt)
        st.code(code, language=lang)
    else:
        st.warning("Please enter both a programming language and a prompt.")
