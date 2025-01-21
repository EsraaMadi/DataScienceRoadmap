import streamlit as st
# st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# # show logo image
# _, im_col, _ = st.columns([0.35, 0.3, 0.35])
# with im_col:
#     st.image("ulits/images/tuwaiq-academy-logo.png")
# st.markdown("""---""")

def get_instructions():
    # st.markdown('#')
    st.markdown('#')
    
    
    # show arabic welcome message
    st.markdown("""<h5 style="text-align: center">      
    تنبيهات عامة 📝
       </h5>
    """, unsafe_allow_html=True)
    _, col, _ = st.columns([0.35, 0.3, 0.35])
    col.markdown("""---""")
    
    _, col, _ = st.columns([0.25, 0.5, 0.25])
    with col:
        st.warning('يُمنع مشاركة أو نشر المحتوى التعليمي', icon="⚠️")
        st.warning('يُمنع تصوير مرافق المبنى أو الأشخاص أو المحتوى التعليمي', icon="⚠️")
        st.warning('عدم البقاء في القاعة بعد انتهاء وقت المعسكر', icon="⚠️")
        st.warning('يُمكنك الاستراحة و العمل في الأماكن المخصصة (Rest Area)', icon="⚠️")
        st.warning('لا يسمح للطلاب بالدخول إلى منطقة مكاتب الموظفين', icon="⚠️")
        

