import streamlit as st
# st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# # show logo image
# _, im_col, _ = st.columns([0.35, 0.3, 0.35])
# with im_col:
#     st.image("ulits/images/tuwaiq-academy-logo.png")
# st.markdown("""---""")


def get_instructor_team():
    # st.markdown('#')
    st.markdown('#')
    st.write("## Lead Instructor:")
    _, col2, _ = st.columns([0.325, 0.35, 0.325])
    with col2:
        st.info("""## 👩🏻‍🏫 Eng. Esraa Madhi
        Data scientist | AI Educator
        """)
        st.image("ulits/images/Esraa.png")
        st.markdown('#')
        st.markdown("""---""")
    
    st.write("## Teaching Assistant")
    _, col1, _, col3, _ = st.columns([0.12, 0.28, 0.2, 0.28, 0.12])
    with col1:
        st.success("""## 🧑🏼‍🏫 Mohammed Alamri
        Data scientist
        """)
        st.image("ulits/images/Mohammed.png")
        st.markdown('#')
    with col3:
        st.success("""## 🧑🏼‍🏫 Yasser Almubaddil
        Data scientist
        """)
        st.image("ulits/images/Yasser.png")
        st.markdown('#')