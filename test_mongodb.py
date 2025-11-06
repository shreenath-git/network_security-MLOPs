
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://shreenath6362_db_user:Admin123@cluster0.yjdd20i.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
