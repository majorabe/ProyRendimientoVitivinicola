import streamlit as st
import requests

icono_url = "uvas.png"  

# Configurar layout con dos columnas para el titulo
col1, col2 = st.columns([4,0.5])
with col1:
    st.title("Predicción de Rendimiento Vitivinícola")
with col2:
    st.image(icono_url, width=75)

st.write(f"Tipo de Uva: Malbec")
st.write(f"Región: Mendoza - Argentina - (Considerando sus 18 Dptos)")
st.write(f"Periodo de recoleccion de datos: 2013 a 2023")

# Agregar select con opciones
opciones = ["2024", "2025", "2026", "2027", "2028"]

st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        width: 200px !important;
    }
    </style>
    """, unsafe_allow_html=True)

seleccion = st.selectbox("Año a Pronosticar:", opciones)

st.write(f"Has seleccionado: {seleccion}")


# Solicitar un ítem al usuario
item_id = st.number_input("Ingrese el ID del ítem:", min_value=0, value=1)

# Botón para obtener el ítem
if st.button("Obtener ítem"):
    response = requests.get(f"http://127.0.0.1:8000/items/{item_id}")
    if response.status_code == 200:
        data = response.json()
        st.success(f"Ítem obtenido: {data}")
    else:
        st.error("Error al obtener el ítem.")
        