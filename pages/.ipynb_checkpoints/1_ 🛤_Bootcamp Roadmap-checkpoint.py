from datetime import datetime
from collections import defaultdict, namedtuple
import streamlit as st
import pandas as pd
import ulits.load_data as ld


STAGE_COLORS = {
    "Side_session": "rgba(219, 245, 39, 0.8)",
    'Interactive Activity': "rgba(140, 46, 0, 0.2)",
    'Penguin Activity': "rgba(39, 172, 245, 0.8)",
    "Self Assessment": "rgba(251, 182, 66, 0.8)",
    'Week Activity':"rgba(245, 73, 39, 0.8)",
    "Hands-on_Session": "rgba(221, 0, 129, 0.2)",
    "Lab": "rgba(30, 0, 150, 0.2)",
    "Usecase": "rgba(221, 0, 129, 0.2)",
    "Usecase - Project": "rgba(254, 241, 96, 0.6)",
    "Usecase - Lab": "rgba(0, 120, 223, 0.2)",
    "Main_session":"rgba(0, 135, 107, 0.2)"
}

STAGE_EMOJI = {
    "Side_session": "🥙",
    'Interactive Activity': "🦋",
    'Penguin Activity': "🐧",
    'Week Activity':"🎃",
    "Self Assessment": "🌚",
    "Hands-on_Session": "👭🏻",
    "Lab": "☂️",
    "Usecase": "🏄🏻‍♂️",
    "Usecase - Project": "🧗🏻‍♀️",
    "Usecase - Lab": "🏋🏻‍♂️",
    "Main_session":"👓"
}

ITEMS_NUMBERS = {
    1: "1️⃣", 
    2 : "2️⃣"
    ,3: "3️⃣"
    ,4: "4️⃣"
    ,5: "5️⃣"
    ,6: "6️⃣"
    ,7: "7️⃣"
    ,8: "8️⃣"
    ,9: "9️⃣"
}


@st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_roadmap():
    df = ld.load_roadmap('Bootcamp TOC')
    return df

def _get_item_tag(name):
    item_color = STAGE_COLORS.get(name, "rgba(206, 205, 202, 0.5)")
    item_emojy = STAGE_EMOJI.get(name,"⏺")
    return (
        f'<span style="background-color: {item_color}; padding: 1px 6px; '
        "margin: 0 5px; display: inline; vertical-align: middle; "
f"border-radius: 0.25rem; font-size: 0.75rem; font-weight: 400; "
f'white-space: nowrap">{item_emojy} {name}'
"</span>")

def _format_date(date):
    # Parse the date string into a datetime object
    date_object = datetime.strptime(date, '%d/%m/%Y')

    # Format the datetime object into the desired string format
    formatted_date = date_object.strftime('%d %B %Y')
    return formatted_date

def _filter_groups(today, groups):
    history_list = []
    current_list = []
    future_list = []

    for i in groups:
        item_date = datetime.strptime(i[0][2], '%d/%m/%Y').date()
        if item_date < today:
            history_list.append(i)
        elif item_date == today:
            current_list.append(i)
        else:
            future_list.append(i)
    return history_list, current_list, future_list

def _draw_groups(time, groups):
    week_no = 0
    for i in groups:
        day_agenda_df = i[1]
        if week_no < i[0][0]:
            week_no = i[0][0]
            phase = i[0][3]
            if time == 0:
                st.warning(f'## Week {week_no} 🗓 - {phase}')
            elif time == 1:
                st.success(f'## Week {week_no} 🗓 - {phase}')
            else:
                st.info(f'## Week {week_no} 🗓 - {phase}')
        st.subheader(f'Day {i[0][1]} : {_format_date(i[0][2])}')
        item_count = 1
        for index, row in day_agenda_df.iterrows():
            st.write("")
            item_tag = _get_item_tag(row['type'])
            description = f"<br /><small style='color: #808495'>{row['Description']}</small>"

            a, b = st.columns([0.03, 0.97])
            a.markdown(ITEMS_NUMBERS[item_count])
            if len(row['Display_link']) > 0:
                html_code = f"<a href={row['Display_link']}> {row['Title']}</a>{item_tag}{description}"
            else:
                html_code = f"<strong>{row['Title']}</strong> {item_tag}{description}"
            b.markdown(html_code, unsafe_allow_html=True)
            item_count+= 1
        st.markdown("""---""")
        

def _draw_agenda(df, today):

    groups_df = list(df.groupby(['#Week', '#Day', 'Date', 'Phase']))

    history_list, current_list, future_list = _filter_groups(today, groups_df)

    with st.expander("Show past days"):
        _draw_groups(time=0, groups=history_list)
        
    _draw_groups(time=1, groups=current_list)

    with st.expander("Show coming days"):
        _draw_groups(time=2, groups=future_list)
    
st.set_page_config(page_title='DS Program',layout='wide', page_icon="ulits/images/Logos_Colored.png")
# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

st.write(
    """
    ### Bootcamp Roadmap! 🛤
    
    Dive into our daily plan tailored for this bootcamp. You'll find a series of in-depth lessons, hands-on activities, collaborative projects, insightful talks from industry experts, as well as practical lab that we're eagerly tackling or anticipating. Approach each day with an open mind—there's always something new to uncover in the depths of data!
    """
)

# Get today's date
# today = datetime(2024, 5, 15).date()
today = datetime.now().date()

roadmap_df = _get_raw_roadmap()
_draw_agenda(roadmap_df, today)