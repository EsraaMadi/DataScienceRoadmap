import streamlit as st
st.set_page_config(layout='wide')


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

_, col2, _ = st.columns([0.4, 0.2, 0.4])
with col2:
    st.image("ulits/wi-fi.png")
    st.markdown('#')

_, col, _ = st.columns([0.2, 0.6, 0.2])
with col:
    st.text_input('Network Name', 'Student_Bootcamp', disabled=True)
    st.text_input('Password', 'Bootcamp@001', disabled=True)