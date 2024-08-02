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
key = file_name.replace(".py", "").strip()

with st.expander(key, expanded=True):
    task_header(key)
    
    with st.columns([1,6,1])[1]:
        st.image('./assets/images/05.png', use_column_width=True)
    
    st.write(f"""
    This task sought space for different models that were not being used throughout the project and raised tests on the model that seemed more feasible time-wise. Four main research areas were encountered: Multi-Agents + SAM, LTCNs, GNNs, and VLMs.  The model that has proven to be ready to use is the Graph Neural Networks, which enabled our team to make initial tests. 

             
    ##### 1. Multi-Agents LLM + Segment model
    The founding idea was to leverage the multi-agents approach to improve current models, seeking to integrate LLMs (LM Studio) and SAM with text prompt. The attempt proved to be heavy research-wise. At the end of the project, our team encountered research in progress that may become a potential technology to test in the future - Multimodal-Maestro. Another model in this line we found is Catlip. 
    
    ##### 2. Liquid-Time Constant Models ( LTCNs )
    A second direction encountered during research is the idea of using “Liquid Constant Time Networks” (LTCNs) raised by MIT students (Math), given that identifying roofs in different regions can be a changing task. The fact that these neural cells adapt in time to changing conditions, has the potential to be a promising powerful tool for changing regions evaluation in time. This approach has proven to be too new, with few sources of good code available to be quickly leveraged during the time we had, but is a potential area to be observed and tested in the future if research evolves enough within the research area.
    
    ##### 3. Graph Neural Networks (GNNs)
    Later, the idea of using Graph Neural Networks (GNNs) was raised, given its ability to map points and create connections around buildings. We found the ready-to-use distribution of Polyworld, which promises to find the roofs of buildings with reasonable accuracy. Polyworld is a pre-trained model in which the architecture depends on COCO formatting for inferencing, leveraging the need to transform our input data from the tiff format into the COCO format.

    ##### 4. Visual Language Models (VLMs) Fine-Tunning
    A last item raised throughout the research is using Visual Language Models (VLMs) that are already pre-trained, such as the PaliGemma, (HuggingFace Description), and later fine-tuning the model to our specific task.

    ###  Methods & Tools
    The model that has proven to be feasible to use within the boundaries of the project timeline is the Graph Neural Network (GNN) Polyworld.  To run the model, first a pre-processing step took place to transform the .tiff and .mask.tiff files into the coco format. With the adapted dataset at hand, the next step was to run Polyworld. First an adaptation of the code to run on CPU was made, and then the inputs were adjusted with an initial run being taken by the final weeks of the project. 
    ### Results & Insights
    From the initial runs of Polyworld GNN, a visual inspection was made and can be demonstrated here: 
    """)
    
    with st.columns([1,10,1])[1]:
        st.image("assets/images/05-img.png")

    st.write("""
    As can be seen in the figure above, the Polyworld GNN identifies the roofs with few imperfections, but seems like it also misclassifies car roofs as a house roof, raising the need for future fine-tuning of the model for improvements (for example, augmenting the minimum line size to higher than 1 meter). 
    """)
    
    #Footer
    st.write(open("./assets/html/page.html", "r").read().split("---")[1].format(
            links = "".join([f"<li><a href=\"{link['url']}\">{link['title']}</a></li>" for link in TASKS_DICT[key][0]['links']])
        ), unsafe_allow_html=True
    )