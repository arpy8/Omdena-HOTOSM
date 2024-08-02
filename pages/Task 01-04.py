import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from constants import TASKS_DICT
from utils import set_page_background


st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)
set_page_background()

with st.columns(12)[0]:
    back_button = st.button("🔙", key="1", use_container_width=True)

if back_button:
    switch_page("app")


file_name = os.path.basename(__file__)
key = file_name.replace(".py", "").strip()

with st.expander(key, expanded=True):
    st.write(open("./assets/html/page.html", "r").read().split("---")[0].format(
            title=TASKS_DICT[key][0]["title"],
            lead=TASKS_DICT[key][0]["lead"],
            members=", ".join(TASKS_DICT[key][0]["members"]),
            description="",
        ), unsafe_allow_html=True
    )
    
    st.write("""To test the applicability of FastSAM, five experiments were performed. These experiments aimed to evaluate the performance and accuracy of the FastSAM model on the HOT dataset under various conditions. Below is a summary of each experiment:

### Experiment 1
- **Objective:** Test FastSAM inference on an original HOT dataset image (256x256 px) with an Intersection Over Union (IOU) of 0.7 and confidence threshold (conf) of 0.3.
- **Method:** Used FastSAM inference command with specified parameters.
- **Result:** All objects, lakes, and trees in the image were segmented successfully. CLIP was installed to predict the most relevant text snippet for the image.

### Experiment 2
- **Objective:** Test FastSAM inference on the same image with a text prompt ("buildings").
- **Method:** Added a text prompt to the FastSAM inference command.
- **Result:** The model identified all the buildings correctly, but in addition to other segments, one vegetated area (“tree”) was segmented as well.

### Experiment 3
- **Objective:** Test FastSAM inference on another image with different settings (256x256 px, IOU=0.9, conf=0.4) and text prompt ("building roof").
- **Method:** Modified IOU and confidence threshold values and provided a text prompt.
- **Result:** The model did not perform well with the higher IOU and confidence interval using either prompt.

### Experiment 4
- **Objective:** Test FastSAM inference on a larger image size (1024x1024 px, IOU=0.9, conf=0.4).
- **Method:** Used a larger image and specified parameters.
- **Result:** The "everything" prompt did not segment everything, and the text prompt misidentified a trash can as a building.

### Experiment 5
- **Objective:** Test with a 768x768 px image created by merging 9 images in a 3x3 grid.
- **Method:** Merged images using QGIS software and assessed accuracy with FastSAM inference.
- **Result:** Only four buildings were successfully segmented, indicating a decrease in segmentation accuracy. Other objects like lakes, plants, or trees were not segmented.

### Additional Experiments (Unstructured)
- **Objective:** Test various IOU values (0.5 to 0.8) and confidence thresholds (0.25 to 0.5) for optimization.
- **Method:** Experimented with different settings and image resolutions.
- **Result:** Successfully segmented all buildings in some images. Modified the prompt script file to predict all buildings instead of just the one with the maximum threshold. Results varied between images, with some missegmentations (e.g., cars as buildings).

### General Findings
- Different settings and prompts affect segmentation accuracy.
- Larger image sizes and different IOU/confidence values can improve or reduce accuracy.
- The model's performance can be inconsistent, varying between images and prompt types.

#### Findings:
- The FastSAM team has not released the training code yet.
- FastSAM inferences are better if the base image is of a bigger size compared to the original 256x256 px image.
- Choosing an IOU < 0.9 and conf_thres < 0.4 yields better results.
- Explored FastGeoSAM, which uses the segment-geospatial package built on SAM to work with geospatial data, gave better results. It can directly work with the TMS server, create GeoTIFF files, and give results in vector format.
- Considering the current case where we are provided with chips and masks of manageable size, working directly with SAM (its base model) and fine-tuning it could be more beneficial for the project.

### Overall Conclusion
- FastSAM is an image segmentation model like SAM, but much faster.
- Currently, FastSAM cannot be trained, which may improve performance, but more importantly, this creates a black-box which makes it incompatible with the fAIr principles of HOTOSM.
- Discontinued after initial testing.
             """)

    st.write(open("./assets/html/page.html", "r").read().split("---")[1].format(
            links = "".join([f"<li><a href=\"{link['url']}\">{link['title']}</a></li>" for link in TASKS_DICT[key][0]['links']])
        ), unsafe_allow_html=True
    )