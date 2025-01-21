import streamlit as st
# st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")

# # show logo image
# _, im_col, _ = st.columns([0.35, 0.3, 0.35])
# with im_col:
#     st.image("ulits/images/tuwaiq-academy-logo.png")
# st.markdown("""---""")


def get_certificate():
    # st.markdown('#')
    st.markdown('#')
    # show arabic welcome message
    st.markdown("""<h5 style="text-align: center">      
    شروط الحصول على شهادة نهاية المعسكر 👩🏻‍🎓👨🏻‍🎓
       </h5>
    """, unsafe_allow_html=True)
    _, col, _ = st.columns([0.35, 0.3, 0.35])
    col.markdown("""---""")
    
    _, col, _ = st.columns([0.3, 0.4, 0.3])
    with col:
        st.text_input('', 'عدم تجاوز الغياب بدون عذر 3 أيام', disabled=True)
        st.text_input('', 'تسليم الواجبات اليومية', disabled=True)
        st.text_input('', 'تسليم المشاريع الأسبوعية و المشروع النهائي', disabled=True)
        st.text_input('', 'الالتزام بوقت المعسكر وعدم التأخر', disabled=True)
        st.text_input('', 'تأخرك 3 مرات يساوي غياب يوم كامل', disabled=True)
        

