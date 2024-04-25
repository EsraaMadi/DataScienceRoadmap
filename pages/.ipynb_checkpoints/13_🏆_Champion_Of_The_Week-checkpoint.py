import streamlit as st
import ulits.load_data as ld
st.set_page_config(layout='wide')

# @st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_chanpion():
    df_lst = ld.load_champian()
    return df_lst

Week_no = 3
# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

# Get dictionery of each week
df_dict = _get_raw_chanpion(Week_no)

# aggregate all weeks data in one datafram
df_students = ld.get_champions(df_dict)
st.dataframe(df_students)

cols_lst = [st.columns(len(df_students.columns[1:]))]

for idx, col in enumerate(df_students.columns[1:]):
    cols_lst[idx].metric(col, "", "")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")