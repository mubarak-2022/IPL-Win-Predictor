import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Mumbai', 'Bengaluru', 'Chennai', 'Kolkata', 'Jaipur',
       'Delhi', 'Dharamsala', 'Port Elizabeth', 'Ahmedabad', 'Pune',
       'Raipur', 'Cape Town', 'Bangalore', 'Durban', 'Johannesburg',
       'Bloemfontein', 'Chandigarh', 'Nagpur', 'Mohali', 'Visakhapatnam',
       'Ranchi', 'Abu Dhabi', 'Centurion', 'Indore', 'Cuttack',
       'East London', 'Kimberley', 'Sharjah']

pipe = pickle.load(open('pipe.pkl','rb'))


st.markdown("<h1 style='text-align: center;'>IPL Predictor</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select the host City',cities)

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs Completed')
with col5:
    wicket = st.number_input('Wicket Out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wicket
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                             'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets_left': [wickets_left],
                             'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.subheader(batting_team + "- " + str(round(win * 100)) + "%")
    st.subheader(bowling_team + "- " + str(round(loss * 100)) + "%")