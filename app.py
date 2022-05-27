###########################################################################################################
###########################################################################################################
###########################################################################################################
######## author = João Pedro Borges
######## insitution = N/A
######## website = 
######## version = 1.0
######## status = 
######## deployed at = 
######## layout inspired by https://share.streamlit.io/tdenzl/bulian/main/BuLiAn.py
###########################################################################################################
###########################################################################################################
###########################################################################################################

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import time
from matplotlib import pyplot as plt
from  matplotlib.ticker import FuncFormatter
import seaborn as sns



st.set_page_config(layout="wide")


DATE_COLUMN = 'date'
DATA = 'historico_partidas_cblol22_clean.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data




#data_load_state = st.text('Loading data...')

#data_load_state.text("Done! (using st.cache)")

data = load_data(90)






def wins_side(data): #total #against, #conceived
    
	blue_wins = len(data.loc[data['winner'] == data['blue']]['winner'])
	red_wins = len(data.loc[data['winner'] == data['red']]['winner'])



	fig = plt.figure(figsize = (8, 4.5))
	ax = fig.add_axes([0,0,1,1])
	names = ['Blue Wins', 'Red Wins']
	values = [blue_wins, red_wins]
	bar = ax.bar(names,values)
	bar[1].set_color('r')

	st.pyplot(fig)




row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('CBLOL - Data Analytics')
with row0_2:
    st.text("")
    #st.subheader('App by [João Pedro Borges](https://www.linkedin.com/in/joaopedroborges98/)')
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("CBLOL é o campeonato brasileiro de League of Legends. Ocorre duas vezes ao ano e reuni milhares de espectatores. Com a medida que os times vão competindo no campeonato, diversos dados são gerados por partida, o desempenho dos atletas é refletido nos números, e com isso podemos realizar diversas analises a respeito do jogo e do campeonato como um todo. Anlytics é uma ferramenta importante para o auxilio a tomada de decisões estrategicas em jogo.")
    #st.markdown("You can find the source code in the [BuLiAn GitHub Repository](https://github.com/tdenzl/BuLiAn)")
   

row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3, row2_3, row2_spacer4, row2_4, row2_spacer5   = st.columns((.2, 1.6, .2, 1.6, .2, 1.6, .2, 1.6, .2))
with row2_1:
    unique_games_in_df = 10
    str_games = "💰 " + str(unique_games_in_df) + " Gold"
    st.markdown(str_games)
with row2_2:
    unique_teams_in_df = len(np.unique(10).tolist())
    t = " Kills"
    if(unique_teams_in_df==1):
        t = " Kills"
    str_teams = "💥 " + str(10) + t
    st.markdown(str_teams)
with row2_3:
    total_goals_in_df = 10
    str_goals = "🧱" + str(total_goals_in_df) + " Towers"
    st.markdown(str_goals)
with row2_4:
    total_shots_in_df = 10
    str_shots = "🐲 " + str(total_shots_in_df) + " Dragons"
    st.markdown(str_shots)


row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("")
    see_data = st.expander('Clique aqui para ver os dados 👉')
    with see_data:
        st.dataframe(data=data)
st.text('')


row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))

with row4_1:

	st.markdown("")
	st.subheader("Quantidade de vitorias de acordo com o lado do mapa")
	wins_side(data)



