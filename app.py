import pandas as pd
import streamlit as st
import plotly_express as px

# Leer el dataset
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.title('Análisis Exploratorio de Datos de Vehículos Usados')

st.write(
    """
    Selecciona una o más casillas para construir gráficos interactivos
    sobre el mercado de vehículos usados.
    """
)

# Casilla 1: Histograma de precios
build_histogram = st.checkbox('Construir histograma de precios')

if build_histogram:
    st.write('Histograma de la distribución de precios')

    fig_hist = px.histogram(
        df,
        x='price',
        nbins=50,
        title='Distribución de precios de vehículos'
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla 2: Gráfico de dispersión precio vs kilometraje
build_scatter = st.checkbox('Construir diagrama de dispersión (precio vs kilometraje)')

if build_scatter:
    st.write('Relación entre el precio y el kilometraje del vehículo')

    # Eliminamos valores nulos para evitar errores
    df_scatter = df.dropna(subset=['odometer', 'price'])

    fig_scatter = px.scatter(
        df_scatter,
        x='odometer',
        y='price',
        title='Precio vs Kilometraje',
        opacity=0.5
    )

    st.plotly_chart(fig_scatter, use_container_width=True)




