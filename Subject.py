
import pandas as pd


def readSubjects():
    df = pd.read_csv("data_notas.csv")
    return df

def addSubjects(df, name, mark):
    df_new = pd.DataFrame([{'Nombre': name, 'Nota': mark}])
    df = pd.concat([df, df_new], ignore_index=True)
    df.to_csv("data_notas.csv", index=False)
