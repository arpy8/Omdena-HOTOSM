import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from utils import set_page_background


st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)
set_page_background()

with st.columns(5)[0]:
    back_button = st.button("🔙", key="1")

if back_button:
    switch_page("app")


file_name = os.path.basename(__file__)
st.write(f"""# {file_name.split('.')[0]}

This is an example page
""")