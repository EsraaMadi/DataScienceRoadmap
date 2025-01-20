import streamlit as st
import os



st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# show logo image
_, im_col, _ = st.columns([0.35, 0.3, 0.35])
with im_col:
    st.image("ulits/images/tuwaiq-academy-logo.png")
st.markdown("""---""")
st.markdown('#')

# show arabic welcome message
st.markdown("""<h4 style="text-align: right">      
   🚀 مرحبا بك في معسكر علم البيانات وتعلم الآلة 
   </h4>

   
   <div style="text-align: right"> 
   حيث تبدأ رحلتكم في عالم البيانات! نحن متحمسون لأن تنطلقوا في هذا المسار التحويلي، لفك أسرار البيانات الخفية وتحويل المعلومات إلى رؤى قابلة للتنفيذ معًا، سنستكشف ونتعلم ونبتكر باستخدام أدوات وتقنيات رائدة ستشكل مستقبلكم كمحترفين في علم البيانات
    </div>
"""
                , unsafe_allow_html=True)

st.markdown('#')

# show english welcome message

st.markdown("""<h4 style="text-align: left">      
   Welcome to Our Data Science Bootcamp! 🚀
   </h4>

   
   <div style="text-align: left"> 
   Where your journey into the world of data begins! We're thrilled to have you embark on this transformative path, unlocking the secrets hidden within data and turning information into actionable insights. Together, we will explore, learn, and create with the leading tools and techniques that will shape your future as a data science professional.
    </div>
"""
                , unsafe_allow_html=True)


st.markdown('#')








