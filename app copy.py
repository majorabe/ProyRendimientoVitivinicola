import streamlit as st
import requests

st.title("API FastAPI con Streamlit")

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
        