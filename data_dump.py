import pymongo
import pandas as pd
import json
from sensor.config import mongo_client
# Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb+srv://turey_dany:arul2304@cluster0.egy97.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME="aps"
Collection_name="sensor"

if __name__=="__main__":
    df=pd.read_csv("/config/workspace/aps_failure_training_set1.csv")
    print(f"Rows and columns :{df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())     #loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary
    print(json_record[0])

    mongo_client[DATABASE_NAME][Collection_name].insert_many(json_record)