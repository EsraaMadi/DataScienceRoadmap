import streamlit as st
import pandas as pd
from datetime import datetime
import ulits.load_data as ld
import plotly.graph_objects as go


st.set_page_config(layout='wide')

@st.cache_data(show_spinner="Fetching TOC...")
def _get_raw_roadmap():
    df = ld.load_roadmap('Bootcamp TOC')
    return df

def _filter_groups(today, df):
    finished_list = []
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df["Is Finished"] = df['Date'].dt.date < today
    return df

def split_text_column(df, text_col):
    # Split the text column and create a new DataFrame
    df = df[['Date', 'Title','type','general_type', text_col]]
    splitted_df = (
    df.set_index(['Date', 'Title', 'type', 'general_type'])
    .apply(lambda x: x.str.split(',').explode())  # Split and explode the 'text' column
    .reset_index()  # Reset the index to bring 'id' and 'other_column' back to columns
    )
    splitted_df[text_col] = splitted_df[text_col].str.strip()
    return splitted_df

@st.cache_data(show_spinner="Drawing Chart...")
def plot_stats(finished_df):
    
    labels_df = finished_df.groupby(['general_type',
                                   'type'], as_index=False).count()[['general_type',
                                                                     'type',
                                                                     "Is Finished"]]
    parents_df = finished_df.groupby(['general_type'], as_index=False).count()[['general_type',
                                                                     "Is Finished"]]

    uc_df = finished_df[finished_df['general_type'] == 'Usecases'][['Title',
                                                                    'type', "Is Finished"]].drop_duplicates()
    print(uc_df, "----------")
    uc_df = uc_df.groupby(['type'], as_index=False).count()[['type',"Is Finished"]]
    
    labels = ['Bootcamp','Activity', 'Interactive Activity',
              'Jeopardy Activity', 'Penguin Activity','Assessment',
              'Self Assessment', 'Practical exercise', 'Hands-on_Session',
              'Lab','Session', 'Main_session', 'Side_session',
              'Usecases', 'Usecase', 'Usecase - Lab','Usecase - Project']
    parents = ['','Bootcamp','Activity', 'Activity',
                                         'Activity', 'Bootcamp', 'Assessment', 'Bootcamp',
                                         'Practical exercise', 'Practical exercise', 'Bootcamp',
                                         'Session', 'Session', 'Bootcamp',
                                         'Usecases', 'Usecases', 'Usecases']
    values = []
    for l in labels:
        temp1_df = labels_df[labels_df['type'] == l]
        temp2_df = parents_df[parents_df['general_type'] == l]
        temp3_df = uc_df[uc_df['type'] == l]
        if l in ['Usecase', 'Usecase - Lab','Usecase - Project'] and temp3_df.shape[0]>0:
            values.append(uc_df["Is Finished"].values[0])
        elif temp1_df.shape[0] > 0:
            values.append(temp1_df["Is Finished"].values[0])
        elif temp2_df.shape[0] > 0:
            values.append(temp2_df["Is Finished"].values[0])
        elif l == 'Bootcamp':
            values.append(finished_df.shape[0])
        else:
            values.append(0)

    values[-4] = sum(values[-3:])
    # update usecase
    fig =go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        values=values,
    ))
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    return fig


# Get today's date
# today = datetime.now().date()
today = datetime(2024, 5, 15).date()

# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
st.markdown('#')

# show title of page
st.write(
    """
    ### Table of Content! 💻
    """
)
s_col, _, _ = st.columns([0.3, 0.35, 0.35])
with s_col:
    st.markdown("""---""")
st.markdown('#')
st.markdown('#')

# show the first dropdown list
roadmap_df = _get_raw_roadmap()
make_choice = st.selectbox('Filter TOC By:',options = ['General Topics', 'Data Skill', 'Project Phase'])
st.markdown('#')

# show the dataframe
if make_choice == 'General Topics':
    toc_df = roadmap_df[roadmap_df['type']=='Main_session']
    toc_df.index = list(range(1,toc_df.shape[0]+1))
    toc_df = _filter_groups(today, toc_df)
    toc_plot_df = toc_df[toc_df["Is Finished"]]
    toc_df = toc_df[['Title', 'Phase',"Is Finished"]]
    toc_df.columns = ['Lesson', 'Bootcamp Phase', "Is Finished"]
elif make_choice == 'Data Skill':
    toc_df = split_text_column(roadmap_df, 'Skill')
    skill_choice = st.selectbox('Choose data skill:',options = list(toc_df['Skill'].unique()))
    toc_df = toc_df[toc_df['Skill']==skill_choice][['Date','Title', 'type', 'general_type']]
    toc_df = _filter_groups(today, toc_df)
    toc_plot_df = toc_df[toc_df["Is Finished"]]
    toc_df.index = list(range(1,toc_df.shape[0]+1))
    toc_df = toc_df [['Title', 'type', "Is Finished"]]
    toc_df.columns = ['Session', 'Session Type', "Is Finished"]
    toc_df = toc_df.drop_duplicates()
    
else:
    toc_df = split_text_column(roadmap_df, 'DS_step')
    step_choice = st.selectbox('Choose data project phase:',options = sorted(list(toc_df['DS_step'].unique())))
    toc_df = toc_df[toc_df['DS_step']==step_choice][['Date','Title', 'type', 'general_type']]
    toc_df = _filter_groups(today, toc_df)
    toc_plot_df = toc_df[toc_df["Is Finished"]]
    toc_df.index = list(range(1,toc_df.shape[0]+1))
    toc_df = toc_df [['Title', 'type', "Is Finished"]]
    toc_df.columns = ['Session', 'Session Type', "Is Finished"]
    toc_df = toc_df.drop_duplicates()

# draw the chart
fig = plot_stats(toc_plot_df)
st.plotly_chart(fig, use_container_width=True)

st.dataframe(toc_df, height=1000, width=900) 
