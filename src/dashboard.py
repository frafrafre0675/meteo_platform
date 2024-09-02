import streamlit as st
from cassandra.cluster import Cluster
import pandas as pd

cluster = Cluster(['cassandra'])
session = cluster.connect('locations')

st.title('Tableau de Bord Météo')

@st.cache
def load_data():
    rows = session.execute('SELECT * FROM places')
    df = pd.DataFrame(rows)
    return df

data_load_state = st.text('Chargement des données...')
df = load_data()
data_load_state.text('Données chargées !')

st.subheader('Données Météo')
st.write(df)

# Afficher les données sur une carte
st.map(df[['latitude', 'longitude']])
