import streamlit as st

tab1, tab2 = st.tabs(["concept", "기능 시연"])

with tab1:
    st.header("concept")
    st.image("concept.jpg", width=1020)
with tab2:
    st.title('kbo_weather_AI')
    st.subheader('직관하러 갈 수 있을까?')

    kbo_form = st.form('kbo_ground')

    # This is writing directly to the main body. Since the form container is
    # defined above, this will appear below everything written in the form.
    team = st.selectbox('team name', ['KIA','LG','롯데','두산','KT','삼성','SSG','NC','한화','키움'])
    #ground = st.selectbox('ground name', )
    # These methods called on the form container, so they appear inside the form.
    submit = kbo_form.form_submit_button('submit')
    user_month = st.selectbox('직관 월', ['3','4','5','6','7','8'])
    user_day = kbo_form.text_input('날짜 입력하세요):', 'dd')
    user_hour = st.selectbox('직관 시간', ['14:00','17:00','18:00','18:30'])

    say_it = '우천 취소될 확률은'


    if submit:
        kbo_form.subheader(say_it)
    else:
        kbo_form.subheader('&nbsp;')





# import numpy as np
# import joblib
# model = joblib.load('random_forest_model.pkl')
# feature = np.array([10, 1, 7, 1, 2, 1, 70]).reshape(1, -1)
# y_pred = model.predict(feature)
