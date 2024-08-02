import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from constants import TASKS_DICT
from utils import set_page_background, task_header

st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)
set_page_background()

with st.columns(12)[0]:
    back_button = st.button("🔙", key="1", use_container_width=True)

if back_button:
    switch_page("app")

file_name = os.path.basename(__file__)
key = file_name.replace(".py"
                        , "").strip()

with st.expander(key, expanded=True):
    task_header(key)