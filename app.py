import streamlit as st 
import google.generativeai as genai 
genai.configure(api_key="AIzaSyDkns7eS1xnOJ-kuEGCDpiUTQNJAygwtJI")
def text_description(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text
inp = st.text_input("enter text")
if st.button("generate"):
    res = text_description(inp)
    st.success(res)