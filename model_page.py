import streamlit as st
    
def create_container(task, title, lead, image_path, description, link):
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
        
            st.link_button("Know More", link, use_container_width=True)
        return True
    
    except Exception as e:
        st.error(f"Error: {e}")
        return False

def models_page():
    st.write("""
        <div style='text-align:center;'>
            <h1 style='text-align:center; font-size: 300%;'>Models Generated</h1>
            <p style='color: #00000095'>Here are all the different models generated by the team.</p>
            <hr>
        </div>
    """
    , unsafe_allow_html=True)
    
    col = st.columns(3)
    
    with col[0]:
        create_container(
            task="Task 01-01",
            title="Ramp Sam Postprocessing",
            lead="John Doe",
            image_path="assets/img/01.png",
            description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt, autem! Laborum harum porro, earum provident enim ipsum alias doloribus aliquam quas dolores.",
            link=""
        )

        create_container(
            task="Task 01-04",
            title="Fast Segment Anything Model (FastSAM)",
            lead="John Doe",
            image_path="assets/img/04.png",
            description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt, autem! Laborum harum porro, earum provident enim ipsum alias doloribus aliquam quas dolores.",
            link=""
        )
            
    with col[1]:
        create_container(
            task="Task 01-02",
            title="Grounding DINO Sam",
            lead="John Doe",
            image_path="assets/img/02.png",
            description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt, autem! Laborum harum porro, earum provident enim ipsum alias doloribus aliquam quas dolores.",
            link=""
        )
    
        create_container(
            task="Task 01-05",
            title="GNN-Based Multimodal",
            lead="John Doe",
            image_path="assets/img/05.png",
            description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt, autem! Laborum harum porro, earum provident enim ipsum alias doloribus aliquam quas dolores.",
            link=""
        )
    
    with col[2]:
        create_container(
            task="Task 01-03",
            title="YOLO with Segment Anything Model",
            lead="John Doe",
            image_path="assets/img/03.png",
            description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt, autem! Laborum harum porro, earum provident enim ipsum alias doloribus aliquam quas dolores.",
            link=""
        )

        create_container(
            task="Task 01-06",
            title="U-Net",
            lead="John Doe",
            image_path="assets/img/06.png",
            description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt, autem! Laborum harum porro, earum provident enim ipsum alias doloribus aliquam quas dolores.",
            link=""
        )
    
if __name__ == '__main__':
    st.set_page_config(layout="wide")
    models_page()