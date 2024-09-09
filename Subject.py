
import pandas as pd


def readSubjects():
    df = pd.read_csv("data_notas.csv")
    return df

def addSubjects(df, name, note):
    df_new = pd.DataFrame([{'Nombre': name, 'Nota': note}])
    df = pd.concat([df, df_new], ignore_index=True)
    saveSubjects(df)

def updateSubjects(df, name, note):
    df.loc[df['Nombre'] == name, 'Nota'] = note
    saveSubjects(df)

def saveSubjects(df):
    df.to_csv("data_notas.csv", index=False)