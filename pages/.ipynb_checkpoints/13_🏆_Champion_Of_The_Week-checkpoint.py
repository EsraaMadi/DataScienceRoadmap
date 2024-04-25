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

cols = st.columns(len(df_students.columns[1:]))

for col, name in zip(cols, df_students.columns[1:]):
    col.metric(name, "", "")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")

st.balloons()

import numpy as np

st.title("Matrix Display in Streamlit")

# Create a random matrix
matrix_size = st.slider("Select the size of the matrix", min_value=2, max_value=10, value=5)
matrix = np.random.randint(0, 10, size=(matrix_size, matrix_size))

# Display the matrix
st.write("Here is a random matrix:")
st.dataframe(matrix)

# Optional: Use matplotlib to display the matrix as a heatmap
if st.checkbox("Show as heatmap"):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='viridis')
    for (i, j), val in np.ndenumerate(matrix):
        ax.text(j, i, val, ha='center', va='center', color='white')
    plt.title('Matrix Heatmap')
    st.pyplot(fig)