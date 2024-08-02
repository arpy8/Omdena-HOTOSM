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
In the rapidly evolving field of computer vision, object segmentation plays a pivotal role in extracting meaningful information from images. Among the array of segmentation algorithms, YOLOv8 and YOLOv9 have emerged as robust and adaptable solutions, offering efficient segmentation capabilities with remarkable accuracy. In this project, we delved into training YOLOv8 and YOLOv9 for object segmentation on our datasets and performed inference on validation data. We also explored YOLOv8 and YOLOv9 object detection with SAM.

### Overview

#### YOLOv8
YOLOv8 is the latest stable release in the YOLO series of real-time object detectors, known for its outstanding performance in both accuracy and speed. Building on the enhancements of its predecessors, YOLOv8 introduces several innovative features and optimizations, making it a premier choice for a wide array of object detection and segmentation tasks across various applications. 

Key features of YOLOv8:
- **Advanced Backbone and Neck Architectures**: These significantly enhance feature extraction and detection capabilities.
- **Anchor-Free Split Ultralytics Head**: Improves detection accuracy and efficiency compared to traditional anchor-based approaches.
- **Model Varieties**: Available in nano, small, medium, large, and extra-large (xl) variants, catering to different performance needs.

For this project, the small variant was chosen due to its faster processing times, even though it is less accurate compared to the medium, large, and xl versions.

#### YOLOv9
YOLOv9 marks a significant advancement in the field of real-time object detection, introducing innovative techniques such as Programmable Gradient Information (PGI) and the Generalized Efficient Layer Aggregation Network (GELAN). These enhancements provide notable improvements in efficiency, accuracy, and adaptability, setting new benchmarks, particularly on the MS COCO dataset.

Key features of YOLOv9:
- **Programmable Gradient Information (PGI)**: Enhances the learning capacity of the model and preserves critical data across network layers.
- **Generalized Efficient Layer Aggregation Network (GELAN)**: Allows for efficient parameter utilization and computational flexibility, making YOLOv9 adaptable to various applications.

### Performance Metrics

#### YOLOv8
- **Accuracy**: High performance in terms of speed and accuracy.
- **Suitability**: Does not recognize rooftops out-of-the-box but can be trained on custom datasets for various tasks.
- **Model Variety**: Ultralytics provides five model varieties (nano, small, medium, large, and xl). The small version is faster but less accurate than medium, large, and xl versions.

#### YOLOv9
- **Innovations**: Incorporates PGI and GELAN for enhanced performance.
- **Efficiency**: High speed and accuracy, addressing information loss in lightweight models.

### YOLOv8/YOLOv9 + SAM Integration

#### Segment Anything Model (SAM)
SAM, developed by Meta, revolutionizes image segmentation by simplifying this essential task across diverse applications. Utilizing the extensive Segment Anything 1-Billion (SA-1B) mask dataset, SAM significantly reduces the need for specialized expertise and computational resources. Trained on over 1 billion diverse masks, SAM facilitates zero-shot segmentation across new domains.

By integrating YOLOv8 and YOLOv9 object detection with SAM, this powerful combination minimizes the need for extensive retraining or data annotation. YOLOv8/YOLOv9 provides efficient detection capabilities, while SAM generates precise segmentation masks.

### Data Preparation

#### Conversion of Images and Mask Formats
- **TIFF to JPEG**: TIFF images were converted to JPEG format to ensure compatibility with the YOLO models.
- **GeoJSON to YOLO Format**: GeoJSON labels were converted to the YOLO format (.txt labels) to facilitate efficient training.

#### Dataset Splitting
- **Training and Validation Sets**: The dataset was split into 80% for training and 20% for validation to ensure comprehensive performance assessment.

### Training Process

1. **Run YOLOv8/YOLOv9 on Training Dataset**: Each model was trained on data from a specific area for 100 epochs, allowing them to adapt to unique visual characteristics of each region.
2. **Extracting Bounding Boxes**: Post-training, the models generated bounding boxes around detected objects in each image.
3. **Convert Bounding Boxes to Segmentation Masks Using SAM**: Bounding boxes from YOLO models served as inputs to SAM, which generated detailed segmentation masks.
4. **Run Inference on Validation Images**: The trained models were applied to validation images to assess performance, with metrics such as Intersection over Union (IoU) and F1 scores computed to measure effectiveness.

### Conclusion

This project demonstrates the powerful capabilities of YOLOv8 and YOLOv9 for object segmentation, particularly when integrated with SAM. The combination of efficient detection and precise segmentation enhances the potential for diverse applications, from scientific research to creative projects.
    """)