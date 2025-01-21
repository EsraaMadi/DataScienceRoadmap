import streamlit as st
# st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# # show logo image
# _, im_col, _ = st.columns([0.35, 0.3, 0.35])
# with im_col:
#     st.image("ulits/images/tuwaiq-academy-logo.png")
# st.markdown("""---""")

def get_map():
    # st.markdown('#')
    st.markdown('#')
    # show arabic welcome message
    st.markdown("""<h5 style="text-align: center">      
    مرافق تُهمك 🚻
       </h5>
    """, unsafe_allow_html=True)
    _, col, _ = st.columns([0.35, 0.3, 0.35])
    col.markdown("""---""")
    
    _, col, _ = st.columns([0.25, 0.5, 0.25])
    with col:
        st.info('مصلى الرجال في الدور الأول قرب المصاعد ممر  C 👨🏼', icon="🕌")
        st.info('مصلى النساء في الدور الأول قرب المصاعد ممر  A 👩🏼', icon="🕌")
        st.info(' DUNKIN في الدور الأرضي قرب المصاعد ممر  A', icon="☕")
        st.info(' Subway في الدور الأرضي ممر  A', icon="🥙")
        st.info(' استراحة الرجال في الدور الأرضي ممر  A 👨🏼', icon="🛋️")
        st.info(' استراحة النساء في الدور الأرضي ممر  A 👩🏼', icon="🛋️")
        st.markdown('#')
        # st.markdown('#')
    _, col, _ = st.columns([0.45, 0.1, 0.45])
    with col:
        st.markdown("""---""")
        # st.markdown('#')
        st.markdown('#')
        st.write("[خريطة المبنى](https://github.com/Tuwaiq-DS-ML-bootcamp-V-6/Others/blob/main/Building_Map.pdf)")
        
    
