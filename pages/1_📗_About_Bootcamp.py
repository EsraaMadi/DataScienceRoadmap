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
    students_list = ld.load_students_names()
    if "flipped_cards" not in st.session_state:
        st.session_state.cards = [ ("🧑🏼‍🎓", i) for i in students_list]
        card_flip_order = list(range(0, len(st.session_state.cards)))
        random.shuffle(card_flip_order)
        st.session_state.card_flip_order = card_flip_order
    fc.drow_cards()

with tab_instractors:
    it.get_instructor_team()