import streamlit as st
import ulits.discord_channel as dc
import ulits.bootcamp_github as bg
import ulits.wi_fi_access as wi
import ulits.bootcamp_support as us



st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.png")

tab_discord, tab_github, tab_wifi, tab_suport = st.tabs(["📺 Discord Channel", " 📖 Github","📶 Wi-Fi Access", "🫶🏼 Career Guidance"])

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:18px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

with tab_discord:
    dc.get_discord()

with tab_github:
    bg.get_github()

with tab_wifi:
    wi.git_wifi()

with tab_suport:
    us.get_bootcamp_support()