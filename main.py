import streamlit as st

st.set_page_config( page_title="test",
            page_icon=":shark:",
            layout="wide")

st.markdown("# Hello, world")
st.sidebar.write("This is the main page")
st.sidebar.image('dell_logo.png')