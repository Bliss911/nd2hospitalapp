import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
        
        
def main(req: func.HttpRequest) -> func.HttpResponse:
        
    logging.info('Python getPosts trigger function processed a request.')
        
    try:
        url = "mongodb://nd2hospitalcosmos:AfxPATz1CbyX6S8jSZZl7raUblTkB6OLjeWJYsXqxFAgYumFzt9AHeFpGd3GGscLoGyjdItswYA2P30xm6hA0w==@nd2hospitalcosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@nd2hospitalcosmos@"
        client = pymongo.MongoClient(url)
        database = client['nd2hospitaldb']
        collection = database['posts']
        
        result = collection.find({})
        result = dumps(result)
        
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)