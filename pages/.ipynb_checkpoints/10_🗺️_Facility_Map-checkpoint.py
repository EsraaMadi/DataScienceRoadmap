import streamlit as st
st.set_page_config(layout='wide')


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/tuwaiq-academy-logo.svg")
st.markdown("""---""")
st.markdown('#')
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
    st.info('مصلى الرجال في الدور الأول قرب المصاعد ممر  C', icon="ℹ️")
    st.info('مصلى النساء في الدور الأول قرب المصاعد ممر  A', icon="ℹ️")
    st.info(' DUNKIN في الدور الأرضي قرب المصاعد ممر  A', icon="ℹ️")
    st.info(' Quiznos في الدور الأرضي قرب المصاعد ممر  C', icon="ℹ️")


    

