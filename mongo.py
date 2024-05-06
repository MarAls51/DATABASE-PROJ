# Database stuff
from pymongo.mongo_client import MongoClient
import certifi
import os
from pymongo.errors import PyMongoError

db_name = "store"
client = None
db = None
collection = None
connection = ""

def open_db(custom_db=None, custom_collection=None):
    global client, db, collection
        
    client = MongoClient(connection, tlsCAFile=certifi.where())
    selected_db_name = db_name
    if(custom_db):
        selected_db_name = custom_db
    try:
        db = client[selected_db_name]
        print("connected")

    except PyMongoError as e:
        print(str(e))

def insert_item(crap_to_insert, collection):
    try:
        collection = db[collection]
        result = collection.insert_one(crap_to_insert)
        return result
    except PyMongoError as e:
        print(str(e))

def remove_item(name, collection):
    try:
        collection = db[collection]
        result = collection.delete_one({"name": name})
        return result.deleted_count == 1
    except PyMongoError as e:
        print(str(e))

def query_user(username, password = None, user_type = None):
    try:
        if(user_type == "admin"):
            collection = db["Admin"]
        else:
            collection = db["User"]
        result = None
        if(password):
            result = collection.find_one({"name": username, "password": password})
        else:
            result = collection.find_one({"name": username})
        if result:
            return result
        else:
            return False
    except PyMongoError as e:
        print(str(e))
        
def query_primary_key(id, collection):
    try:
        collection = db[collection]
        item = collection.find_one({"_id": id})
        return item
    except PyMongoError as e:
        print(str(e))

def remove_data_using_primary_key(name, id, field, collection):
    try:
        collection = db[collection]
        result = collection.update_one({"name": name}, {"$pull": {field: id}})
        return result
    except PyMongoError as e:
        print(str(e))

def update_data(name, field, data, collection):
    try:
        collection = db[collection]
        result = collection.update_one({"name": name}, {"$set": {field: data}})
        return result  
    except PyMongoError as e:
        print(str(e))

def query_supervised_users(username):
    try:
        collection = db["Admin"]
        users = collection.find_one({"name": username})
        return users["users"]
    except PyMongoError as e:
        print(str(e))

def query_orders(username):
    try:
        collection = db["User"]
        orders = collection.find_one({"name": username})
        return orders["orders"]
    except PyMongoError as e:
        print(str(e))

def query_products():
    try:
        collection = db["Product"]
        products = list(collection.find()) 
        return products
    except PyMongoError as e:
        print( str(e))

def close_db():
    try:
        client.close()
        print("logged out")

    except PyMongoError as e:
        print(str(e))

