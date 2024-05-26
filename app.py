import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from menu import Menu
from constants import PAGE_FAVICON
from utils import set_page_background


st.set_page_config(page_title='Omdena HOTOSM Webapp', page_icon=PAGE_FAVICON, layout='wide', initial_sidebar_state="collapsed")
st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)
set_page_background()

if 'disable_button' not in st.session_state:
    st.session_state['disable_button'] = False

with st.sidebar:
    selected_task = on_hover_tabs(
        tabName=['Home Page', 'Task 1', 'About Us'],
        iconName=['home', 'settings', 'groups'],
        styles = {
            'navtab': {'background-color':'transparent',
                        'color': '#00000080',
                        'padding': '40px 0px 10px 0px',
                        'border-radius': '0px',
                        'font-size': '18px',    
                        'transition': '.5s',
                        'white-space': 'nowrap',
                        'text-transform': 'uppercase',
            },
            'tabOptionsStyle': {':hover :hover': {'color': '#170034',
                                            'cursor': 'pointer'},
                            },
            'iconStyle':{'position':'fixed',    
                        'left':'11.5px'},
            'tabStyle' : {'background-color':'rgba(0, 0, 0, 0)',
                        'list-style-type': 'none',
                        'margin-bottom': '30px',
                        },
        },
        key="1",
        default_choice=1)


menu = Menu()
if selected_task == 'Home Page':
    menu.home_page()

elif selected_task == 'Task 1':
    menu.model_page()

elif selected_task == 'About Us':
    menu.about_us_page()