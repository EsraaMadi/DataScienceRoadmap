import streamlit as st
import ulits.load_data as ld
import math
import plotly.express as px
st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")

week_no = 5

@st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_chanpion(week_no):
    df_lst = ld.load_champian(week_no)
    return df_lst

MATRIC_COLORS = {
    "Interactive Activity": "rgba(103, 36, 222, 0.2)",
    'Week Activity': "rgba(140, 46, 0, 0.2)",
    "Hackerrank": "rgba(251, 182, 66, 0.8)",
    "Career Coach": "rgba(221, 0, 129, 0.2)",
    "Clean Code": "rgba(0, 120, 223, 0.2)",
    "Best Submit": "rgba(0, 135, 107, 0.2)",
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
f"border-radius: 0.25rem; font-size: 1.5rem; font-weight: 400; "
f'white-space: nowrap">{item_emojy} {name}'
"</span>"))
    return display_matrices

def _get_champian_name(name):
    return (
        f'<span style="background-color: rgba(0, 135, 107, 0.2); padding: 1px 6px; '
        "margin: 0 5px; display: inline; vertical-align: middle; "
f"border-radius: 0.25rem; font-size: 3.0rem; font-weight: 400; "
f'white-space: nowrap">{name}🌟'
"</span>")


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
# st.dataframe(df_students)

# first section
st.write( """### Based on:""")
row_col_no = len(df_students.columns[1:])/2
cols_row1 = st.columns(math.ceil(row_col_no))
cols_row2 = st.columns(math.floor(row_col_no))
                       
display_matrices = _get_materic(df_students.columns[1:])
for c, i in zip(cols_row1,display_matrices):
    c.markdown(f"{i}", unsafe_allow_html=True)
for c, i in zip(cols_row2,display_matrices[len(cols_row1):]):
    c.markdown(f"{i}", unsafe_allow_html=True)
    
st.markdown('#')
st.markdown('#')
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

df_champian = df_students.copy()
df_champian['total'] = df_students.iloc[:, 1:].sum(axis=1)
top_1_df = df_champian.nlargest(1, 'total')
st.write( """### 🏆 Our Champion Of The Week is:""")
name = top_1_df["Name"].values[0]
st.markdown(f"{_get_champian_name(name)}", unsafe_allow_html=True)
st.balloons()

st.markdown('#')
st.markdown('#')
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

st.write( """### Top 10 in our class:""")
top_10_df = df_champian.nlargest(10, 'total')
top_10_df_sorted = top_10_df.sort_values(by='total', ascending=False)
fig = px.bar(top_10_df_sorted, x='Name', y='total')
st.plotly_chart(fig, use_container_width=True)
# st.dataframe(top_10_df_sorted)
st.markdown('#')
st.markdown('#')
st.markdown("""---""")
st.markdown('#')
st.markdown('#')
st.write( """### Top in each:""")


# Find the student with the highest grade in each course
df_students_i = df_students.set_index('Name')
cols_row3 = st.columns(math.ceil(row_col_no))
cols_row4 = st.columns(math.floor(row_col_no))


for c, col in zip(cols_row3, df_students_i.columns):
    df_sort = df_students_i[col].sort_values(by=col)
    c.bar_chart(df_sort[[col]].head(5))
    break

# display_matrices = _get_materic(df_students.columns[1:])
# for c, col in zip(cols_row3, df_students_i.columns):
#     max_total = df_students_i[col].max()  # Get the maximum grade in the course
#     top_student = df_students_i[col].idxmax()  # Get the student name with the maximum grade
#     c.metric(col, top_student, int(max_total))
# for c, col in zip(cols_row4, df_students_i.columns[len(cols_row3):]):
#     max_total = df_students_i[col].max()  # Get the maximum grade in the course
#     top_student = df_students_i[col].idxmax()  # Get the student name with the maximum grade
#     c.metric(col, top_student, int(max_total))
