import os

print("📍 Directorio actual (cwd):", os.getcwd())
print("📁 Archivos en ese directorio:", os.listdir(os.getcwd()))
import pandas as pd
import plotly.express as px
import streamlit as st

st.header('analisis de ventas de vehiculos usados')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir evolucion precio promedio por dia')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('evolucion precio promedio segun condicion del vehiculo')

    df_agrupado= car_data.groupby(['date_posted','condition'])['price'] .mean().reset_index()

    fig2= px.line(df_agrupado, x="date_posted", y="price", color='condition',
    title= 'precio promedio de los vehiculos segun estado')
    st.plotly_chart(fig2, use_container_width=True)