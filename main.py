# Importamos FastAPI del módulo fastapi
from fastapi import FastAPI

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Definimos una ruta para la raíz ("/") usando el método HTTP GET
@app.get("/")
def read_root():
    # Esta función se ejecuta cuando se accede a la ruta raíz
    # Retorna un diccionario que será convertido a JSON automáticamente
    return {"Hello": "World"}

# Definimos una ruta para "/items/{item_id}" usando el método HTTP GET
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    # Esta función se ejecuta cuando se accede a la ruta /items/{item_id}
    # item_id es un parámetro de ruta que debe ser un entero
    # q es un parámetro de consulta opcional de tipo string
    # Retorna un diccionario con el item_id y el parámetro de consulta q
    return {"item_id": item_id, "q": q}
