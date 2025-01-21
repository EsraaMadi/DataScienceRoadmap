import streamlit as st
# st.set_page_config(page_title='DS Bootcamp',layout='wide', page_icon="ulits/images/Logos_Colored.png")


# # show logo image
# _, im_col, _ = st.columns([0.35, 0.3, 0.35])
# with im_col:
#     st.image("ulits/images/tuwaiq-academy-logo.png")
# st.markdown("""---""")


def get_bootcamp_overview():
    # st.markdown('#')
    st.markdown('#')
    # show arabic welcome message
    st.markdown(
        """<h4 style="text-align: right">      
      : وصف المعسكر  
       </h4>
       <div style="text-align: right"> 
       يهدف معسكر علم البيانات وتعلم الآلة إلى التعرف على علم البيانات وكيفية التعامل مع أنواع البيانات المختلفة، يتخذ هذا المعسكر نهجًا تطبيقيًا يٌرَكز على تطوير المهارات العملية من خلال مشاريع واقعية يتعلم فيها المشاركون كيفية استخراج البيانات وتحليلها واستخدام التقنيات الحديثة في تعلم الآلة لبناء نماذج تنبؤية تحليلية تهدف لحل المشكلات العملية وتطوير الأعمال
        </div>
    """
                    , unsafe_allow_html=True)
    
    st.markdown('#')
    st.markdown("""---""")
    st.markdown(
        """<h4 style="text-align: right">      
    : يشمل هذا المعسكر مشاريع عملية تغطي الموضوعات الأساسية التالية
       </h4>
       <ul dir="rtl">
      <li>مراحل دورة حياة مشروع البيانات، ابتداءً من تحديد المشكلة وصولاً إلى طرح التوصيات استنادًا إلى التحليلات </li>
      <li>أساسيات علم البيانات بما في ذلك جمع البيانات، تنظيفها, عرضها, والتحليل الاستكشافي لها. (Exploratory Data Analysis) </li>
      <li>تطوير نماذج تنبؤية باستخدام خوارزميات تعلم الآلة وتقييمها وتحسين أدائها (Machine Learning Models) </li>
      <li>مقدمة في التعلم العميق (Deep learning)، وتطبيقاتها مثل التعرف على الصور ومعالجة اللغة الطبيعية. (computer vision )(Natural language processing)</li>
      <li>تنظيم وعرض النتائج التحليلية بطرق تساعد في اتخاذ القرارات (Data storytelling)
    </li>
    </ul>
    """
                    , unsafe_allow_html=True)
    
    st.markdown('#')
    st.markdown("""---""")
    
    st.markdown(
        """<h4 style="text-align: right">      
    : الأهداف
       </h4>
    <ul dir="rtl">
      <li>تعزيز مهارات التعاون والعمل الجماعي ضمن الفريق من خلال القيام بمشاريع مشتركة في علم البيانات</li>
      <li>التعرف على أنواع البيانات والتحديات التي قد تظهر أثناء التعامل معها</li>
      <li>تطبيق مبادئ التعلم الآلي في تحليل البيانات ونمذجتها لحل مشكلات حقيقية</li>
      <li>تطوير قدرة المشاركين على تقديم نتائج المشاريع بصورة احترافية ومفهومة
    </li>
    </ul>
    """
                    , unsafe_allow_html=True)
    
    st.markdown('#')
    st.markdown("""---""")
    
    st.markdown("""<h4 style="text-align: right">      
    المتطلبات 
       </h4>
    <ul dir="rtl">
      <li>الإلمام والمعرفة المسبقة بمستوى ممتاز في لغة Python</li>
        <li>الإلمام والمعرفة المسبقة بالتعامل مع Git</li>
          <li>الإلمام والمعرفة المسبقة بأساسيات لغة SQL</li>
            <li>جهاز لاب توب بنظام macOS أو Windows</li>
              <li>لغة إنجليزية متوسطة</li>
                <li>أن تكون حاصلًا على شهادة جامعية في أحد التخصصات التقنية أو الإحصاء</li>
                  <li>الرغبة الصادقة في التعلم والمشاركة الفعالة طوال مدة المعسكر، والالتزام بإكمال الأعمال والمشاريع الموكلة</li>
    </ul>
    
    """
                    , unsafe_allow_html=True)