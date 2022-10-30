import pandas as pd
def pre_processing_posts(df):
    list_null=[]
    for i in df.columns:
        if df[i].isna().sum()>0:
            list_null.append(i)
        elif i=='cts':
            df[i]=pd.to_datetime(df[i],utc=True)
    for j in list_null:
        if j=='profile_id':
            df[j].fillna(0,inplace=True)  ##Replace Null Profile ID with empty string
        elif j=='description':
            df[j].fillna('',inplace=True) ## Replace NAN values with empty string
    
    return df