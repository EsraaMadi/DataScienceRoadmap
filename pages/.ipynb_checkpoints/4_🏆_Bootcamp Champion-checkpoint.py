import streamlit as st
import ulits.champion as uc
import ulits.penguin_cards as pc


st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.png")

tab_champion, tab_penguin = st.tabs(["🏆 Champion", "🐧 Penguin Cards"])

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:18px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

with tab_champion:
    uc.get_champion()

with tab_penguin:
    pc.get_cards()