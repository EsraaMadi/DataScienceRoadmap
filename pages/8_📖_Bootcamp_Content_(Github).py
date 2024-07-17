import streamlit as st
st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.png")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

_, col2, _ = st.columns([0.15, 0.7, 0.15])
with col2:
    st.image("ulits/images/Github.png")
    st.markdown('#')

    st.markdown('#')
    st.write("[Link](https://github.com/Tuwaiq-DS-ML-bootcamp-V-6)")