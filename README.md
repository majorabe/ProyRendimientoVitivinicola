# Predicción Vitivinícola con IA :grapes:

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un modelo de predicción del rendimiento vitivinícola utilizando técnicas de inteligencia artificial. La solución se basa en la recopilación de datos climáticos y de producción para predecir la cantidad de uvas Malbec que se pueden obtener en diferentes regiones de Mendoza, Argentina.

El proyecto fue realizado como parte de la formación de **[Mil Mujeres IA](https://milmujeresia.com/)**, que busca empoderar a mujeres en el campo de la inteligencia artificial y la tecnología. 

## Tecnologías Utilizadas

- **FastAPI**: Se utiliza para crear una API que facilita la interacción con el modelo de predicción.
- **Streamlit**: Se implementa para desarrollar una interfaz de usuario interactiva que permite a los usuarios visualizar los resultados de las predicciones de manera intuitiva.
- **Python**: El lenguaje principal para el desarrollo del modelo de IA y la lógica de la aplicación.
- **Pandas**: Para el manejo y análisis de datos.
- **Scikit-Learn**: Para la implementación de algoritmos de machine learning.

## Instalación
Para ejecutar este proyecto localmente, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/prediccion-vitivinola.git
   cd prediccion-vitivinola
2. **Crea un entorno virtual (opcional pero recomendado)**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    # En Windows usa `venv\Scripts\activate`
3. **Instala las dependencias**:
   ```bash
   ip install -r requirements.txt
   ```
4. **Ejecuta la API**:
  ```bash
  uvicorn app:api –reload
  ```
5. **Ejecuta la interfaz de Streamlit**:
  ```bash
  streamlit run app/streamlit_app.py
  ```

## Uso
Una vez que la API y la aplicación de Streamlit estén en funcionamiento, podrás ingresar datos climáticos y obtener predicciones sobre la producción de uvas Malbec. La interfaz es fácil de usar y proporciona resultados visuales claros.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

## Agradecimientos
Agradecemos a Mil Mujeres IA por la oportunidad de aprender y desarrollar este proyecto, y a todas las mentoras y compañeras que han hecho posible esta experiencia.

