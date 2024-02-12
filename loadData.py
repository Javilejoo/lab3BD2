from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
from config import MONGODB_URI

# Conexión a MongoDB Atlas
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Obtener la base de datos y la colección
db = client["lab3chart"]
collection = db["games"]

# Cargar el CSV
data = pd.read_csv("nuevoGames2.csv")

# Limitar los datos a 4000
data = data.head(4000)

# Convertir el DataFrame a formato de lista de diccionarios
data_dict = data.to_dict(orient="records")

# Insertar los datos en la colección de MongoDB
collection.insert_many(data_dict)

print("Los datos se han cargado exitosamente en MongoDB.")
