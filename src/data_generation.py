import uuid
import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta


def fechas_y_probabilidades(start_date, end_date):
    fechas = pd.DataFrame(columns=["fecha","prob"])
    start_date = start_date
    end_date = end_date
    current_date = start_date
    i = 0
    while end_date >= current_date:
        año = datetime.strptime(current_date, "%Y-%m-%d").year
        mes = datetime.strptime(current_date, "%Y-%m-%d").month
        día = datetime.strptime(current_date, "%Y-%m-%d").day
        prob = (((mes%7)+(mes%13))*((2+(año-2024))/2)) #Falta normalizar las probabilidades
        fechas.at[i, "fecha"] = current_date
        fechas.at[i, "prob"] = prob
        current_date = (datetime.strptime(current_date, "%Y-%m-%d")+timedelta(days=1)).strftime("%Y-%m-%d")
        i+=1

    #Normalizando las probabilidades
    fechas["prob_norm"] = (fechas["prob"]/(fechas["prob"].sum()))
    return fechas

def create_empty_df():
    raw_data = pd.DataFrame(columns=[
        "order_id", # "uuid", 
        "customer_id", # "random_int(1, 10_000)", 
        "product_id", # "random_int(1, 1_000)", 
        "quantity", # "random_int(1, 20)", 
        "price", # "random_float(1.0, 500.0)", 
        "discount", # "random_float(0.0, 0.3)", 
        "order_date", # "random_date(2023-01-01, 2024-12-31)", 
        "shipping_priority", # "random_choice(['Low', 'Medium','High'])", 
        "region" # "random_choice(['North', 'South', 'East', 'West'])" 
    ])
    return raw_data

def data_generation():
    raw_data = create_empty_df()
    #Se definen los tipos de shipping y regiones
    shipping = ['Low', 'Medium','High']
    region = ['North', 'South', 'East', 'West']
    fechas = fechas_y_probabilidades(start_date='2023-01-01', end_date='2024-12-31')

    for i in range(55000):
        raw_data.at[i,"order_id"] = uuid.uuid4()
        raw_data.at[i,"customer_id"] = np.random.randint(1,10001)
        raw_data.at[i,"product_id"] = np.random.randint(1,1001)
        raw_data.at[i,"quantity"] = np.random.randint(1,21)
        raw_data.at[i,"discount"] = np.random.random(1)*0.3
        raw_data.at[i,"price"] = (np.random.random(1)*500) * (1-raw_data.at[i,"discount"])
        raw_data.at[i,"order_date"] = np.random.choice(fechas["fecha"], p = fechas["prob_norm"]) #Distribución creciente, y con mayor probabilidades en junio y diciembre
        raw_data.at[i,"shipping_priority"] = shipping[np.random.randint(len(shipping))]
        raw_data.at[i,"region"] = region[np.random.randint(len(region))]

    raw_data

    return raw_data