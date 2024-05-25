import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from constants import TASKS_DICT
from utils import set_page_background


st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)
set_page_background()

with st.columns(5)[0]:
    back_button = st.button("🔙", key="1")

if back_button:
    switch_page("app")


file_name = os.path.basename(__file__)
key = file_name.replace(".py", "").strip()

with st.expander(key, expanded=True):
    st.write(open("./assets/html/page.html", "r").read().split("---")[0].format(
        title=TASKS_DICT[key][0]["title"],
        lead=TASKS_DICT[key][0]["lead"],
        members=", ".join(TASKS_DICT[key][0]["members"]),
        description=TASKS_DICT[key][0]["description"],
    ), unsafe_allow_html=True)