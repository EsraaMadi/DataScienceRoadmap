import streamlit as st
import ulits.flip_cards as fc
import ulits.instructors_team as it
import ulits.load_data as ld



st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.png")
#st.markdown("""---""")
# st.markdown('#')
# st.markdown('#')

tab_student, tab_instractors, tab_about, tab_certificate = st.tabs(["Students",
                                        "Trainers",
                                        "Bootcamp Overview",
                                        "Certificate"])

with tab_student:
    #fc.drow_cards()
    st.dataframe(ld.load_students_names())

with tab_instractors:
    it.get_instructor_team()