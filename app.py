import streamlit as st
import fastf1
import plotly.graph_objects as go

@st.cache_data
def load_session(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load()
    return session

# Add text elements
st.title("F1 Telemetry Board")

#Add a selectbox
year = st.selectbox("Choose Year",['2022','2023','2024','2025','2026'])
race = st.selectbox("Choose Race/Grand Prix",['Monza','SilverStone','Spa'])
session_type = st.selectbox("Choose Session",['FP1','FP2','FP3','Q','R'])

#load session
session = load_session(int(year),race,session_type)

st.dataframe(session.laps)
#get the driver list
driver1 = st.selectbox("Choose Driver1",session.laps['Driver'].unique())
driver2 = st.selectbox("Choose Driver2",session.laps['Driver'].unique())
if(driver1 == driver2):
    st.write("Can't choose same driver")
else:
    driver1_laps = session.laps.pick_drivers([driver1])
    driver2_laps = session.laps.pick_drivers([driver2])
    driver1_fastest_laps = driver1_laps.pick_fastest()
    driver2_fastest_laps = driver2_laps.pick_fastest()
    #get telemetry
    d1_tel = driver1_fastest_laps.get_car_data().add_distance()
    d2_tel = driver2_fastest_laps.get_car_data().add_distance()
    #plot chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=d1_tel['Distance'], y=d1_tel['Speed'], name=driver1, mode='lines'))
    fig.add_trace(go.Scatter(x=d2_tel['Distance'], y=d2_tel['Speed'], name=driver2, mode='lines'))
    st.plotly_chart(fig)


    