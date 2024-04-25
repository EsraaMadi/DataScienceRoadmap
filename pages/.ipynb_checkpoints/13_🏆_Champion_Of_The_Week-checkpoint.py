import streamlit as st
import ulits.load_data as ld
st.set_page_config(layout='wide')

# @st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_chanpion(week_no):
    df_lst = ld.load_champian(week_no)
    return df_lst

MATRIC_COLORS = {
    "Interactive Activity": "rgba(103, 36, 222, 0.2)",
    'Week Activity': "rgba(140, 46, 0, 0.2)",
    "Hackerrank": "rgba(251, 182, 66, 0.8)",
    "Career Coach": "rgba(221, 0, 129, 0.2)",
    "Clean Code": "rgba(30, 0, 150, 0.2)",
    "Best Submit": "rgba(221, 0, 129, 0.2)",
    "Help Others": "rgba(254, 241, 96, 0.6)",
}

MATRIC_EMOJI = {
    "Interactive Activity": "🥙",
    'Week Activity': "🦋",
    "Hackerrank": "🌚",
    "Career Coach": "👭🏻",
    "Clean Code": "☂️",
    "Best Submit": "🏄🏻‍♂️",
    "Help Others": "🧗🏻‍♀️",
}

def _get_materic(cols):
    display_matrices = []
    for name in cols:
        item_color = MATRIC_COLORS.get(name, "rgba(206, 205, 202, 0.5)")
        item_emojy = MATRIC_EMOJI.get(name,"⏺")
        display_matrices.append((
        f'<span style="background-color: {item_color}; padding: 1px 6px; '
        "margin: 0 5px; display: inline; vertical-align: middle; "
f"border-radius: 0.25rem; font-size: 0.75rem; font-weight: 400; "
f'white-space: nowrap">{item_emojy} {name}'
"</span>"))
    return display_matrices


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

display_matrices = _get_materic(df_students.columns[1:])
for c, i in zip(cols,display_matrices):
    html_code = f"{i}"
    c.markdown(html_code, unsafe_allow_html=True)
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

