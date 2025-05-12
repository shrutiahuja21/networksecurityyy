from pymongo import MongoClient
from urllib.parse import quote_plus

# Encode the password
username = "216963shrutiahuja"
password = quote_plus("Admin@123")  # This will convert '@' to '%40'

uri = f"mongodb+srv://{username}:{password}@cluster0.4mtunmb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
