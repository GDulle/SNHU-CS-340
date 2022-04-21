#Gunnar Dulle
#CS 340
from pymongo import MongoClient
from bson.objectid import ObjectId
import json


class AnimalShelter(object):
    #CRUD operations fro Animal collection in MongoDB
    
    def __init__(self,username,password):
        """initializing the MongoCLient. This helps to
        access the MongoDB databases and collections."""
        #init to connect to MongoDB without authentication
        #self.client = MongoClient('mongodb://localhost:47705')
        #init to connect to MongoDB with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:47705/?authMechanism=DEFAULT&authSource=AAC'%(username,password))
        self.database = self.client['AAC']
        
    #Create method to implement C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) #data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")     
            
    #Create method to implement R in CRUD        
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False} ) #Return a cursor with a pointer to a list of results (Documents)
        return cursor
    
    def read(self, data):
        return self.database.animals.find_one(data) #Returns only one document as a python dictionary
    
    #Create method to implement U in CRUD
    def update(self, find=dict(), replace=dict()):
        if find is not None:
            x = self.database.animals.update_many(find, {'$set':replace})
            return json.dumps(str(x.modified_count) + " records updated") #Returns in JSON format
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    #Create method to implement D in CRUD
    def delete(self, data):
        if data is not None:
            return json.dumps(self.database.animals.remove(data), indent = 4) #Returns in JSON format
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
        