import streamlit as st
# st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# # show logo image
# _, im_col, _ = st.columns([0.35, 0.3, 0.35])
# with im_col:
#     st.image("ulits/images/tuwaiq-academy-logo.png")
# st.markdown("""---""")


def get_assessment():
    # st.markdown('#')
    st.markdown('#')
    # show arabic welcome message
    st.markdown("""<h4 style="text-align: center">      
      آلية التقييم 
       </h4>
    """, unsafe_allow_html=True)
    
    
    _, col2, _ = st.columns([0.4, 0.2, 0.4])
    with col2:
        st.image("ulits/images/assessment.png")
        st.markdown('#')
    
    _, col, _ = st.columns([0.35, 0.3, 0.35])
    with col:
        st.text_input('التفاعل و المشاركة', '10%', disabled=True)
        st.text_input('الاختبارات', '10%', disabled=True)
        st.text_input('الواجبات و التمارين', '20%', disabled=True)
        st.text_input('المشاريع الأسبوعية', '30%', disabled=True)
        st.text_input('المشروع النهائي', '30%', disabled=True)
    
    st.markdown('#')
    st.markdown("""---""")
    st.markdown('#')
    
    # show arabic welcome message
    st.markdown("""<h5 style="text-align: center">      
     معايير تقييم المشاريع
       </h5>
    """, unsafe_allow_html=True)
    _, col, _ = st.columns([0.35, 0.3, 0.35])
    col.markdown("""---""")
    
    _, col2,col3, _ = st.columns([0.45, 0.2, 0.05, 0.35])
    with col2:
        st.write("استيفاء المعايير المطلوبة")
        st.write("جودة المشروع")
        st.write("التسليم في الوقت")
    with col3:
        st.checkbox("", value=True,disabled=True, key="t1", label_visibility="hidden")
        st.checkbox("", value=True,disabled=True, key="t2", label_visibility="hidden")
        st.checkbox("", value=True,disabled=True, key="t3", label_visibility="hidden")