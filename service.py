import joblib
import random
from fastapi import FastAPI
from pydantic import BaseModel
import csv
import pandas as pd
import numpy as np
app = FastAPI()
db = pd.read_csv('dashboard_database.csv')
@app.get("/score")

def score(card_num: int):
    x = db[db["card1"] == card_num]
    payment_system = x['card4'].unique()
    payment_system = payment_system[0]
    x = x.drop(["card1", "card4"], axis=1)
    result = x.to_dict(orient='records')
    return result