import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder


def load_model():
    with open('ipl_saved.pkl', 'rb') as file:
        data = pickle.load(file) 
    return data
data = load_model()

best_model_model = data["model"]
le_team1 = data["le_team1"]
le_team2 = data["le_team2"]
le_TossWinner = data["le_TossWinner"]
le_TossDecision = data["le_TossDecision"]


def show_predict_page():
    st.title("IPL winner prediction")
    st.write("Lets predict next ")
    
    Team1 = (
        'Gujarat Titans', 
        'Rajasthan Royals',
        'Royal Challengers Bangalore', 
        'Punjab Kings',
        'Mumbai Indians',
        'Lucknow Super Giants', 
        'Sunrisers Hyderabad', 
        'Delhi Capitals',
        'Kolkata Knight Riders', 
        'Chennai Super Kings'
    )
    Team2 = (
        'Gujarat Titans', 
        'Rajasthan Royals',
        'Royal Challengers Bangalore', 
        'Punjab Kings',
        'Mumbai Indians',
        'Lucknow Super Giants', 
        'Sunrisers Hyderabad', 
        'Delhi Capitals',
        'Kolkata Knight Riders', 
        'Chennai Super Kings'
    )
    
    TossDecision = ("bat","field")
    
    Winner_Team = {5: 'Gujarat Titans', 
                  13: 'Rajasthan Royals', 
                  16: 'Royal Challengers Bangalore',
                  12: 'Punjab Kings', 
                  10: 'Mumbai Indians', 
                  9: 'Lucknow Super Giants',
                  17: 'Sunrisers Hyderabad', 
                  2: 'Delhi Capitals', 
                  8: 'Kolkata Knight Riders', 
                  0: 'Chennai Super Kings',
                  18: 'n/r', 
                  }
    
    team1 = st.selectbox("Pick your Team 1",Team1 )
    team2 = st.selectbox("Pick your Team 2",Team2)
    tossWinner = st.radio(f"Toss won by",{team1,team2})
    tossDecision = st.radio("Toss decision",TossDecision)
    button = st.button("predict")
    if button:
        X = np.array([[team1,team2,tossWinner, tossDecision]])
        X[:, 0] = le_team1.transform(X[:,0])
        X[:, 1] = le_team2.transform(X[:,1])
        X[:, 2] = le_TossWinner.transform(X[:,2])
        X[:, 3] = le_TossDecision.transform(X[:,3])
        X = X.astype(float)
        
        winner = best_model_model.predict(X)
        winnerteam = Winner_Team[winner[0]]

        # Inverse transform the label-encoded predictions to get categorical values
        # y_pred_categorical = le_WinningTeam.inverse_transform(winner)
        st.subheader(f"the predicted winner is {winnerteam}")

