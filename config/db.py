from pymongo import MongoClient,errors
from decouple import config
import urllib.parse
# global variables for MongoDB host (default port is 27017)

DOMAIN = config("MONGO_HOST")
PORT = 27017
DB_NAME = config('DB_NAME')
USERNAME = urllib.parse.quote_plus(config('DB_USERNAME'))
PWD = urllib.parse.quote_plus(config('DB_PASSWORD'))

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(
        f"mongodb://{USERNAME}:{PWD}@{DOMAIN}:{PORT}/",
        # host = [ str(DOMAIN) + ":" + str(PORT) ],
        serverSelectionTimeoutMS = 3000 # 3 second timeout
        # username = config('DB_USERNAME'),
        # password = config('DB_PASSWORD'),
    )

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])

    # get the database_names from the MongoClient()
    database_names = client.list_database_names()
    DB = client[DB_NAME]



except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    client = None
    database_names = []

    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)

print ("\ndatabases:", database_names)