import streamlit as st
import ulits.load_data as ld
st.set_page_config(layout='wide')

@st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_chanpion():
    df = ld.load_champian('DS Bootcamp 6/Others/ChampionOfTheWeek template')
    return df


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

df = _get_raw_chanpion()
print(df.shape)
# col1, col2, col3، col4, col5, col6 = st.columns(6)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")