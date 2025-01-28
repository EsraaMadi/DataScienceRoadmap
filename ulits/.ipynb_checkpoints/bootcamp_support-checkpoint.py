import streamlit as st
# st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# # show logo image
# _, im_col, _ = st.columns([0.35, 0.3, 0.35])
# with im_col:
#     st.image("ulits/images/tuwaiq-academy-logo.png")
# st.markdown("""---""")


def get_bootcamp_support():
    # st.markdown('#')
    st.markdown('#')
    # show arabic welcome message
    st.markdown(
        """<h4 style="text-align: right">      
      : الإرشاد المهني  
       </h4>
       <div style="text-align: right"> 

يهدف هذا المسار إلى مساعدة الطلاب في بدء مسيرتهم المهنية بثقة واحترافية، ومعالجة أي تحديات تواجههم أثناء المعسكر ومنها:
- رفع الوعي حول المهارات المطلوبة في سوق العمل
- ⁠تزويدهم بالأدوات اللازمة لمواجهة التحديات واتخاذ القرارات المهنية المناسبة

- استمارة الإرشاد المهني الخاصة بالطلاب 
  تتيح للطلاب تسجيل بياناتهم بشكل مباشر،وسيتم التواصل معهم لتقديم الدعم والإرشاد
        </div>
    """
                    , unsafe_allow_html=True)
    
    st.markdown('#')
    st.markdown("""---""")
    st.write("[Link](https://forms.gle/u53DXWSD8h3qEtT9A)")
 