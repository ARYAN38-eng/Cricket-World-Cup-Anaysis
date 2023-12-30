import pandas as pd
def preprocessed(df):
    df['start_date']=pd.to_datetime(df['start_date'])
    df['opposition']=df['opposition'].replace('v','',regex=True)
    return df
    