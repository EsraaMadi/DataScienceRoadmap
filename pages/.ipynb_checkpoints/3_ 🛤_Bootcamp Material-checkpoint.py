import streamlit as st
import ulits.data_science_lifecycle as ds
import ulits.toc as toc
import ulits.bootcamp_roadmap as br



st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.png")

tab_road_map, tab_toc, tab_ds = st.tabs(["🛤 Bootcamp Roadmap", "💻 TOC","🛺 Data Science Lifecycle"])

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:18px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

with tab_road_map:
    br.get_roadmap_page()

with tab_toc:
    toc.get_toc()

with tab_ds:
    ds.get_ds_lifecycle()