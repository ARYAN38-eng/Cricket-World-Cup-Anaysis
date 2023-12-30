import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st

df=pd.read_csv("CWC23_all_innings.csv")

def countries_strongest_ground(df):
    countries_strongness_ground=df[df['bat_or_bowl']=='bowl'].groupby(['opposition','ground'])['runs'].sum().sort_values(ascending=False)
    countries_strongness_ground_reset=countries_strongness_ground.reset_index()
    return countries_strongness_ground_reset

def india_ground_score(df):
    india_ground_score=df[(df['bat_or_bowl']=='bat') & (df['team']=='IND')].groupby('ground')['runs'].sum()
    return india_ground_score


def correlation_of_numeric_cols(df):
    df=df.select_dtypes(include=[int,float])
    columns_of_interest=df.columns
    selected_data=df[columns_of_interest]
    correlation_matrix=selected_data.corr()
    return correlation_matrix

    
def showing_specific_matches(df):
    user_choice=st.radio("Select an Option",("Search by date","ground","Other"))
    if user_choice=="Search by date":
        chosen_date=st.selectbox("Select a Date",df['start_date'].unique())
        return df[df["start_date"]==chosen_date]
    elif user_choice=="ground":
        chosen_date=st.selectbox("Select a ground",df['ground'].unique())
        return df[df['ground']==chosen_date]
    else:
        choice1=st.radio("Select bat or bowl",("bat","bowl",None))
        choice2=st.selectbox("Select a team",df['team'].unique())
        choice3=st.selectbox("Select an opposition team",df['opposition'].unique())
        if choice1==None:
            return df[(df['team']==choice2)&(df['opposition']==choice3)]
        else:
            return df[(df['bat_or_bowl']==choice1)& (df['team']==choice2)&(df['opposition']==choice3)]
        
    
        
        
    
    
    

        

