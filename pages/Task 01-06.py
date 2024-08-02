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
    
    st.write("""
    - CNN effective for image segmentation; named for a U-Shaped architecture
    - Various backbones tried; Resnet101 achieved 0.90 IOU on TA385

    For Unet architecture, out of 7 backbones (ResNet34, ResNet50, RseNet101, VGG16, VGG19, EfficientNet3 and Efficientnet5), ResNet101 outperformed the other backbones because of following reasons.

    **a) Depth and capacity**<br>
    ResNet101 is a deeper network compared to ResNet34, ResNet50, RseNet101, VGG16, VGG19, EfficientNet3 and EfficientNet5. It has 101 layers which allows it to learn from more complex and detailed features from the data. This greater depth enables ResNet to capture intricate patterns and nuances that shallower networks might miss.<br>

    **b) Residual connections**<br>
    The residual connections in ResNet101 help mitigate the vanishing gradient problem, which can hinder the training of very deep networks.<br>

    **c) Skip connections**<br>
    ResNet architectures use skip connections to allow the gradient to flow directly through the network layers, which help in maintaining the flow of information and prevents the degradation problem. This feature ensures that ResNet101 retains important features and gradients that contribute to more accurate learning. <br>

    **d) Rich feature extraction**<br>
    The deeper structure of ResNet101 can extract richer and more detailed feature representations, which are essential for precise segmentation tasks.<br> 
    """, unsafe_allow_html=True)