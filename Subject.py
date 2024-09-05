from wtforms import Form
from wtforms.fields import StringField
from wtforms.fields.numeric import IntegerField
import pandas as pd


class subjectForm(Form):
    name =StringField('Nombre')
    note = IntegerField('Notas')

def readSubjects():
    df = pd.read_csv("data_notas.csv")
    return df

def addSubjects(df, name, mark):
    df_new = pd.DataFrame([{'Nombre': name, 'Nota': mark}])
    df = pd.concat([df, df_new], ignore_index=True)
    return df

def saveSubjects(df):
    df.to_csv("data_notas.csv", index=False)
