import joblib
import random
from fastapi import FastAPI
from pydantic import BaseModel
import csv
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class ClientData(BaseModel):
    card_num: int


app = FastAPI()

db = pd.read_csv('dashboard_database.csv')
START_DATE = datetime(2024, 12, 1)
db['TransactionDT'] = pd.to_datetime(START_DATE) + pd.to_timedelta(db['TransactionDT'], unit='s')
db['TransactionDate'] = db['TransactionDT'].dt.date
db['TransactionTime'] = db['TransactionDT'].dt.time
db = db.drop("TransactionDT", axis=1)
db["isFraud"] = round(db["isFraud"]*100, 1)

db = db[['TransactionID', 'TransactionDate', 'TransactionTime', 'TransactionAmt', 'isFraud', 'card1', 'card4']]

@app.post("/score")

def score(data: ClientData):

    x = db[db["card1"] == data.card_num]

 #   payment_system = x['card4'].unique()
 #   payment_system = payment_system[0]
    x = x.drop(["card1", "card4"], axis=1)
  #  x = x[['TransactionID', 'TransactionDate', 'TransactionTime', 'TransactionAmt', 'isFraud']]
    result = x.to_dict(orient='records')
    return result