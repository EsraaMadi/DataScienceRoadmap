import streamlit as st
import ulits.load_data as ld
import math
import plotly.express as px
from datetime import datetime

#st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")

# start_date = datetime(2024, 7, 21).date()
# today = datetime.now().date()

# # Calculate the difference in days
# days_difference = (today - start_date).days

# # Calculate the week number
# week_no = days_difference // 7 + 1 
# week_no = week_no -1

@st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_chanpion():
    df_lst, all_df = ld.load_champian()
    return df_lst, all_df

MATRIC_COLORS = {
    "Interactive Activity": "rgba(103, 36, 222, 0.2)",
    'Week Activity': "rgba(140, 46, 0, 0.2)",
    "Hackerrank": "rgba(251, 182, 66, 0.8)",
    "Career Coach": "rgba(221, 0, 129, 0.2)",
    "Active / initiative score": "rgba(0, 120, 223, 0.2)",
    "Best Code": "rgba(0, 135, 107, 0.2)",
    "Help Others": "rgba(254, 241, 96, 0.6)",
}

MATRIC_EMOJI = {
    "Interactive Activity": "🥙",
    'Week Activity': "🦋",
    "Hackerrank": "🌚",
    "Career Coach": "👭🏻",
    "Active / initiative score": "☂️",
    "Best Code": "🏄🏻‍♂️",
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

def get_champion():
    # # show logo image
    # _, im_col, _ = st.columns([0.35, 0.3, 0.35])
    # with im_col:
    #     st.image("ulits/images/tuwaiq-academy-logo.png")
    # st.markdown("""---""")
    # st.markdown('#')
    st.markdown('#')
    
    # Get dictionery of each week
    df_dict, all_df = _get_raw_chanpion()
    
    # aggregate all weeks data in one datafram
    df_students = ld.get_champions(df_dict)
    # st.dataframe(df_students)
    
    # first section
    st.write( """### Based on:""")
    cols_row1 = st.columns(3)
    cols_row2 = st.columns(3)
    cols_row3 = st.columns(3)
                           
    display_matrices = _get_materic(df_students.columns[1:])
    for c, i in zip(cols_row1,display_matrices):
        c.markdown(f"{i}", unsafe_allow_html=True)
    for c, i in zip(cols_row2,display_matrices[len(cols_row1):]):
        c.markdown(f"{i}", unsafe_allow_html=True)
    for c, i in zip(cols_row3,display_matrices[len(cols_row1)+len(cols_row2):]):
        c.markdown(f"{i}", unsafe_allow_html=True)
        
    #st.markdown('#')
    st.markdown('#')
    st.markdown("""---""")
    #st.markdown('#')
    st.markdown('#')

    
    st.write( """### Our Champions Are:""")
    _, im_col, _ = st.columns([0.1, 0.8, 0.1])
    with im_col:
        st.data_editor(
        all_df,
        column_config={
            "Rank": st.column_config.ImageColumn(
                "Week Champion", help="Streamlit app preview screenshots", width="small"
            )
        },
            hide_index=True, use_container_width=True)

    st.markdown('#')
    st.markdown('#')
    st.markdown("""---""")
    st.markdown('#')
    st.markdown('#')
    
    if df_students.shape[0] > 0 :
    
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
        
        
        
        lst_fig = []
        for col in df_students.columns[1:]:
            top_5_df_sorted = df_students.sort_values(by=col, ascending=False).head(5)
            fig = px.bar(top_5_df_sorted, x='Name', y=col)
            lst_fig.append(fig)
        
        row_no = len(lst_fig)/2
        cols_row3 = st.columns(math.ceil(row_no))
        cols_row4 = st.columns(math.floor(row_no))
        
        for col, fig in zip(cols_row3, lst_fig):
            with col:
                st.plotly_chart(fig, use_container_width=True)
        
        for col, fig in zip(cols_row4, lst_fig[len(cols_row3):]):
            with col:
                st.plotly_chart(fig, use_container_width=True)
