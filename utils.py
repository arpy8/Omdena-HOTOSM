import base64, streamlit as st
from constants import  PAGE_BACKGROUND

from streamlit_extras.switch_page_button import switch_page


def set_page_background():
    @st.cache_data()
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    bin_str = get_base64_of_bin_file(bin_file=PAGE_BACKGROUND)
    page_bg_images = '''
        <style>
        {header_css}
        .stApp {{
                background-image: url("data:image/png;base64,{bin_str}");
                backdrop-filter: blur(10px ) !important;
                background-size: cover;
            }}
        </style>
    '''.format(
        header_css=open('./assets/css/styles.css').read(),
        bin_str=bin_str
    )
    
    st.markdown(page_bg_images, unsafe_allow_html=True)
    

def create_container(task, title, lead, image_path, description):
    try:
        with st.expander(task, expanded=True):
            st.write(f"""
                <h5>{title}</h5>
                <p>Lead: {lead}</p>
            """, unsafe_allow_html=True)
            st.image(f"{image_path}", use_column_width=True)
            st.write(f"""
                <p>
                {description}
                </p>
                """, unsafe_allow_html=True)
            
            know_more = st.button("Know More", key=f"{task}", use_container_width=True)
            if know_more:
                switch_page(task)
        return True
    
    except Exception as e:
        st.error(f"Error: {e}")
        return False