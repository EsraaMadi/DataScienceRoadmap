import streamlit as st
st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

_, col2, _ = st.columns([0.15, 0.7, 0.15])
with col2:
    st.image("ulits/images/discord.png")
    st.markdown('#')

_, col, _ = st.columns([0.45, 0.1, 0.45])
with col:
    st.markdown("""---""")
    st.markdown('#')
    st.markdown('#')
    st.write("[Link](https://discord.tuwaiqadmin.com/invite/clvf6drr100nno43of4e1dep3)")