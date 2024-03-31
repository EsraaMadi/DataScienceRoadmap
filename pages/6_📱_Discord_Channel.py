import streamlit as st
st.set_page_config(layout='wide')


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

_, col2, _ = st.columns([0.15, 0.7, 0.15])
with col2:
    st.image("ulits/discord.png")
    st.markdown('#')