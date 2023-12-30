import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import helpercwc,preprocess
df=pd.read_csv('CWC23_all_innings.csv')
st.title("Cricket World Cup 2023 Analysis")
st.image("th.png",width=600)
user_menu=st.radio("Select an option",("Country Analysis","Player Analysis"))
df=preprocess.preprocessed(df)
if user_menu=='Country Analysis':
    st.header("COUNTRY WISE ANALYSIS")
    
    st.subheader("Choose Options to Get Graphs")
    choice1=st.selectbox("Select an option",("opposition","runs","bb_bf","wkts","team","mdns"))
    choice2=st.selectbox("Select an option 2",("opposition","runs","bb_bf","wkts","team","mdns"))
    if choice1 == "opposition" and choice2 == "runs":
        plt.figure(figsize=(10, 8))
        total_team_runs = df[df['bat_or_bowl'] == 'bowl'].groupby(choice1)[choice2].sum()
        sns.barplot(x=total_team_runs.index, y=total_team_runs.values)
        plt.xlabel("Countries")
        plt.ylabel(f"Total {choice2}")
        plt.title(f"Teams with Highest {choice2} in World Cup")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif choice1 =="team" and choice2=="bb_bf":
        plt.figure(figsize=(10, 8))
        total_team_runs = df[df['bat_or_bowl'] == 'bowl'].groupby(choice1)[choice2].sum()
        sns.barplot(x=total_team_runs.index, y=total_team_runs.values)
        plt.xlabel("Countries")
        plt.ylabel(f"Total {choice2}")
        plt.title(f"Teams with Highest bowls bowled in World Cup")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif choice1=="team" and choice2=="wkts":
        plt.figure(figsize=(10, 8))
        total_team_runs = df[df['bat_or_bowl'] == 'bowl'].groupby(choice1)[choice2].sum()
        sns.barplot(x=total_team_runs.index, y=total_team_runs.values)
        plt.xlabel("Countries")
        plt.ylabel(f"Total {choice2}")
        plt.title(f"Teams who took Highest {choice2} in World Cup")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif choice1=="team" and choice2=="mdns":
        plt.figure(figsize=(10, 8))
        total_team_runs = df[df['bat_or_bowl'] == 'bowl'].groupby(choice1)[choice2].sum()
        sns.barplot(x=total_team_runs.index, y=total_team_runs.values)
        plt.xlabel("Countries")
        plt.ylabel(f"Total {choice2}")
        plt.title(f"Teams who took Highest Maiden Over in World Cup")
        plt.xticks(rotation=90)
        st.pyplot(plt)
        
    else:
        st.write("Please choose some other options!!!")
        
    
    st.subheader("Countries Who Scored and Performed Good on Different Grounds")
    countries_strongness_ground_reset=helpercwc.countries_strongest_ground(df)
    custom_colors = sns.color_palette("tab10", 10)
    plt.figure(figsize=(12, 20))
    sns.barplot(x='runs', y='ground', hue='opposition', data=countries_strongness_ground_reset,dodge=False,palette=custom_colors)
    plt.xlabel('Runs')
    plt.ylabel('Ground')
    plt.title('Team with Highest Runs on Each Ground')
    plt.legend(title='Opposition', bbox_to_anchor=(1, 1), loc='upper left')
    st.pyplot(plt)
    
    
    st.subheader("Indian Team Performance on Different Grounds")
    india_ground_score =helpercwc.india_ground_score(df)
    sns.barplot(x=india_ground_score.index, y=india_ground_score.values)
    plt.xlabel("Grounds")
    plt.ylabel("Total Score")
    plt.xticks(rotation=45)
    plt.title("India's Performance on Different Grounds")
    st.pyplot(plt)
    
    st.subheader("Relation among Features")
    correlation_matrix=helpercwc.correlation_of_numeric_cols(df)
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix: Player Performance and Match Conditions')
    st.pyplot(plt)
    
    
    st.subheader("Search Match Score Card")
    score_card=helpercwc.showing_specific_matches(df)
    score_card
    
    plt.figure(figsize=(10,10))
    plt.subplot(3,1,1)
    sns.barplot(x='player',y='runs',hue='team',data=score_card)
    plt.xticks(rotation=90)
    plt.xlabel("Players")
    plt.ylabel("Runs")
    plt.subplot(3,1,2)
    sns.barplot(x='player',y='sr',hue='team',data=score_card)
    plt.xticks(rotation=90)
    plt.xlabel("Players")
    plt.ylabel("Strike Rate")
    
    plt.subplot(3,1,3)
    sns.barplot(x='player',y='mins',hue='team',data=score_card)
    plt.xticks(rotation=90)
    plt.xlabel("Players")
    plt.ylabel("Minutes")

    st.pyplot(plt.gcf())
    
else:
    st.header("PLAYER WISE ANALYSIS")
    user_menu=st.radio("Show Teams,Players,Oppositions,Grounds",("Yes","No"))
    if user_menu=='Yes':
        st.subheader("All Teams,Players,Oppositions,Grounds In the World Cup 2023")
        for cols in df.select_dtypes(include=['object']).columns:
            st.write(f"Unique categories in {cols} column")
            st.write(df[cols].unique())
            st.write("="*100)
    else:
        pass
    
    user_menu2='player'
    user_menu1="bat"
    user_menu3=st.selectbox("Choose an Options",("6s","4s","not_out","runs_per_ball"))
    if user_menu1=="bat" and user_menu2=="player" and user_menu3=="6s":
        plt.figure(figsize=(8,6))
        top_30=df[df['bat_or_bowl']==user_menu1].groupby(user_menu2)[user_menu3].sum().sort_values(ascending=False).head(30)
        sns.set(style='whitegrid')
        custom_colors = ["#FF5733", "#33FF57", "#3366FF", "#FF33D1", "#33FFEC", "#FFD033", "#BB33FF", "#33FF80", "#FF3366", "#33A2FF"]
        sns.barplot(x=top_30.index,y=top_30.values,palette=custom_colors)
        plt.xlabel("Players")
        plt.ylabel("Total sixes")
        plt.title("Top batsmen who hit most sixes in world cup")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif user_menu1=="bat" and user_menu2=="player" and user_menu3=="4s":
        plt.figure(figsize=(8,6))
        top_30=df[df['bat_or_bowl']==user_menu1].groupby(user_menu2)[user_menu3].sum().sort_values(ascending=False).head(30)
        sns.set(style='whitegrid')
        custom_colors = ['red','blue','green','yellow']
        sns.barplot(x=top_30.index,y=top_30.values,palette=custom_colors)
        plt.xlabel("Players")
        plt.ylabel("Total Fours")
        plt.title("Top batsmen who hit most 4s in world cup")
        plt.xticks(rotation=90)
        st.pyplot(plt)
        
    elif user_menu1=="bat" and user_menu2=="player" and user_menu3=="runs_per_ball":
        plt.figure(figsize=(8,6))
        top_30=df[df['bat_or_bowl']==user_menu1].groupby(user_menu2)[user_menu3].sum().sort_values(ascending=False).head(30)
        sns.set(style='whitegrid')
        custom_colors = ['red','blue','green','yellow']
        sns.barplot(x=top_30.index,y=top_30.values,palette=custom_colors)
        plt.xlabel("Players")
        plt.ylabel("Total runs_per_balls")
        plt.title("Top batsmen with highest runs in less balls")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif user_menu1=="bat" and user_menu2=="player" and user_menu3=="not_out":
        plt.figure(figsize=(8,6))
        top_30=df[df['bat_or_bowl']==user_menu1].groupby(user_menu2)[user_menu3].sum().sort_values(ascending=False).head(30)
        sns.set(style='whitegrid')
        custom_colors = ['red','blue','green','yellow']
        sns.barplot(x=top_30.index,y=top_30.values,palette=custom_colors)
        plt.xlabel("Players")
        plt.ylabel("Total Not Out")
        plt.title("Top batsmen with total Not Outs")
        plt.xticks(rotation=90)
        st.pyplot(plt)
        
    elif user_menu1=="bat" and user_menu2=="player" and user_menu3=="mins":
            plt.figure(figsize=(8,6))
            top_30=df[df['bat_or_bowl']==user_menu1].groupby(user_menu2)[user_menu3].sum().sort_values(ascending=False).head(30)
            sns.set(style='whitegrid')
            sns.barplot(x=top_30.index,y=top_30.values)
            plt.xlabel("Players")
            plt.ylabel("Total minutes")
            plt.title("Top batsmen who played for long duration")
            plt.xticks(rotation=90)
            st.pyplot(plt)
    elif user_menu1=="bat" and user_menu2=="player" and user_menu3=="mins":
            plt.figure(figsize=(8,6))
            bottom_30=df[df['bat_or_bowl']==user_menu1].groupby(user_menu2)[user_menu3].sum().sort_values(ascending=True).head(30)
            sns.set(style='whitegrid')
            sns.barplot(x=bottom_30.index,y=bottom_30.values)
            plt.xlabel("Players")
            plt.ylabel("Total minutes")
            plt.title("Top Batsmen who played for short duration")
            plt.xticks(rotation=90)
            st.pyplot(plt)
    else:
        st.write("Please Choose Correct Options")
        
        
    st.subheader("See Distributions of Runs,Strike Rates,Wickets")
    user_menu = st.radio("Choose an Option",("Runs","Wickets","Strike Rate","Maiden Overs"))
    if user_menu =="Runs":
        batsmen_data=df[df['bat_or_bowl']=='bat']
        plt.figure(figsize=(10,8))
        sns.distplot(batsmen_data['runs'],kde=False)
        plt.title("Distribution of Batsmen Runs")
        st.pyplot(plt)
    elif user_menu=="Strike Rate":
        batsmen_data=df[df['bat_or_bowl']=='bat']
        plt.figure(figsize=(10,8))
        sns.distplot(batsmen_data['sr'],kde=False)
        plt.title("Distribution of Batsmen Strike Rate")
        st.pyplot(plt)
    elif user_menu=="Wickets":
        bowler_df=df[df['bat_or_bowl']=='bowl']
        plt.figure(figsize=(10,8))
        sns.distplot(bowler_df['wkts'],kde=False)
        plt.title("Distribution of Bowlers taking  wickets")
        st.pyplot(plt)
    else:
        bowler_df=df[df['bat_or_bowl']=='bowl']
        plt.figure(figsize=(10,8))
        sns.distplot(bowler_df['mdns'],kde=False)
        plt.title("Distribution of Bowlers taking maiden over")
        st.pyplot(plt)
        
    
    st.subheader("See the barplot of top players")
    user_choose=st.selectbox("Choose an Option",("Top 30 bowlers who bowled Highest bowls","Top 30 bowlers who bowled lowest bowls","Top Bowlers Who Gave Highest Runs","Top Bowlers With Highest Wickets","Top Bowlers With Lowest Wickets","Top Bowlers With Highest Maiden Overs",
                                             "Top Bowlers With Lowest Maiden Overs"))
    if user_choose=="Top 30 bowlers who bowled Highest bowls":
        bowls='bb_bf'
        asce=False
        top_players = df[df['bat_or_bowl'] == 'bowl'].groupby(['player'])[bowls].sum().sort_values(ascending=asce).head(30)

        # Plotting the bar chart
        plt.figure(figsize=(15, 6))
        top_players.plot(kind='bar')
        plt.xlabel("Players")
        plt.ylabel("Total Bowls")
        plt.title("Top 30 Bowlers who bowled highest bowls in world cup")
        st.pyplot(plt)
    elif user_choose=="Top 30 bowlers who bowled lowest bowls":
        bowls='bb_bf'
        asce=True
        top_players = df[df['bat_or_bowl'] == 'bowl'].groupby(['player'])[bowls].sum().sort_values(ascending=asce).head(30)

        # Plotting the bar chart
        plt.figure(figsize=(15, 6))
        top_players.plot(kind='bar')
        plt.xlabel("Players")
        plt.ylabel("Total Bowls")
        plt.title("Top 30 Bowlers who bowled lowest bowls in world cup")
        st.pyplot(plt)


    elif user_choose=="Top Bowlers Who Gave Highest Runs":
        plt.figure(figsize=(15,8))
        runs_hit_to_bowlers=df[df['bat_or_bowl']=='bowl'].groupby('player')['runs'].sum().sort_values(ascending=False).head(30)
        sns.barplot(x=runs_hit_to_bowlers.index,y=runs_hit_to_bowlers.values)
        plt.xlabel("Players")
        plt.ylabel("Total runs given by bowler")
        plt.title("Top bowlers who gave highest runs")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif user_choose=="Top Bowlers With Highest Wickets":
        plt.figure(figsize=(15,8))
        total_wkts=df[df['bat_or_bowl']=='bowl'].groupby('player')['wkts'].sum().sort_values(ascending=False).head(30)
        sns.barplot(x=total_wkts.index,y=total_wkts.values)
        plt.xlabel("Players")
        plt.ylabel("Total Wickets")
        plt.title("Top bowlers with Highest Wickets")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif user_choose=="Top Bowlers With Lowest Wickets":
        plt.figure(figsize=(15,8))
        total_wkts=df[df['bat_or_bowl']=='bowl'].groupby('player')['wkts'].sum().sort_values(ascending=True).head(30)
        sns.barplot(x=total_wkts.index,y=total_wkts.values)
        plt.xlabel("Players")
        plt.ylabel("Total Wickets")
        plt.title("Top bowlers with Lowest Wickets")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif user_choose=="Top Bowlers With Highest Maiden Overs":
        plt.figure(figsize=(15,8))
        total_wkts=df[df['bat_or_bowl']=='bowl'].groupby('player')['mdns'].sum().sort_values(ascending=False).head(30)
        sns.barplot(x=total_wkts.index,y=total_wkts.values)
        plt.xlabel("Players")
        plt.ylabel("Total Maidens")
        plt.title("Top bowlers with Highest Maiden Overs")
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif user_choose=="Top Bowlers With Lowest Maiden Overs":
        plt.figure(figsize=(15,8))
        total_wkts=df[df['bat_or_bowl']=='bowl'].groupby('player')['mdns'].sum().sort_values(ascending=True).head(30)
        sns.barplot(x=total_wkts.index,y=total_wkts.values)
        plt.xlabel("Players")
        plt.ylabel("Total Maidens")
        plt.title("Top bowlers with Lowest Maiden Overs")
        plt.xticks(rotation=90)
        st.pyplot(plt)
        
    st.subheader("Show All Winners and their runs")
    choose=st.radio("Choose Yes/No",("Yes","No"))
    if choose=="Yes":
        # Iterate over unique combinations of 'opposition', 'team', 'year'
        df_unique=df[['opposition','team','start_date']].drop_duplicates()
        for opposition, team, year in df_unique.itertuples(index=False):
    
            # Filter the DataFrame based on conditions
            data = df[(df['team']==team)& (df['start_date']==year)&(df['opposition'] == opposition) & (df['bat_or_bowl'] == 'bowl')]
    
            # Calculate batting runs
            batting_runs = data.groupby('start_date')['runs'].sum()
            runs = batting_runs.values[0]  # Assuming a single value for runs
    
            # Calculate bowl played
            bowl_played = data.groupby('start_date')['bb_bf'].sum()
            bp = bowl_played.values[0]  # Assuming a single value for bowl played
    
            # Calculate count
            total_wkts=data.groupby('start_date')['wkts'].sum()
            wkts_sum=total_wkts.values[0]
            wkts_sum=np.abs(wkts_sum-10)
            # Print information for each match separately
            st.write(f"{opposition} made {runs} runs in {bp} balls by {wkts_sum} wickets on date {batting_runs.index[0].strftime('%Y-%m-%d')}")
    else:
        pass
        
        
    
        
        
    
        
    
        
    
    
        
    
    
        
        
        
            
        
    
        
    
    
    