from src.data_generation import data_generation, fechas_y_probabilidades, create_empty_df

def test_fechas():
    start_date = "2023-01-01"
    end_date = "2024-12-31"
    test = True
    fechas = fechas_y_probabilidades(start_date,end_date)
    for fecha in fechas["fecha"]:
        if (fecha > end_date) | (fecha < start_date):
            test = False
            break
    assert test

def test_probabilidades():
    start_date = "2023-01-01"
    end_date = "2024-12-31"
    test = True
    fechas = fechas_y_probabilidades(start_date,end_date)
    if (fechas["prob_norm"].sum() > 1) | (fechas["prob_norm"].sum() < 0.99):
        test = False
    assert test

