import streamlit as st
import ulits.load_data as ld
st.set_page_config(layout='wide')

# @st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_chanpion(week_no):
    df_lst = ld.load_champian(week_no)
    return df_lst

week_no = 3
# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

# Get dictionery of each week
df_dict = _get_raw_chanpion(week_no)

# aggregate all weeks data in one datafram
df_students = ld.get_champions(df_dict)
st.dataframe(df_students)

# first section
st.write( """### 🏆 Champion Of The Week based on:""")
cols = st.columns(len(df_students.columns[1:]))

for col, name in zip(cols, df_students.columns[1:]):
    col.metric(name, "14.2%", "")
    
st.markdown('#')
st.markdown('#')
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

st.success(f'🏆 Our Champion Of The Week is :')
st.balloons()

st.markdown('#')
st.markdown('#')
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

st.write( """### Top 5 in our class:""")

st.markdown('#')
st.markdown('#')
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

st.write( """### Top 1 in each:""")

