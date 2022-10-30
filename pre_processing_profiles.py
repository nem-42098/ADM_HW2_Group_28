def pre_processing_profiles(df):
    list_null=[]
    for i in df.columns:
        if df[i].isna().sum()>0:
            list_null.append(i)
    for j in list_null:
        if j=='firstname_lastname':
            df[j].fillna('',inplace=True)  ##Replace NAN username with empty string
        elif j=='description':
            df[j].fillna('',inplace=True)  ##Replcae NAN profile description as empty string
        elif j=='following':
            df[j].fillna(0,inplace=True)  ##Replcae NAN following(number of other instagram profiles being followed by the user) as 0
        elif j=='followers':
            df[j].fillna(0,inplace=True)  ##Replcae NAN followers(number of other instagram profile following the user) as 0
        elif j=='n_posts':
            df[j].fillna(0,inplace=True)  ##Replcae NAN number of posts by the user as 0
        elif j=='url':
            df[j].fillna('',inplace=True)  ##Replcae NAN profile link as empty string
        elif j=='cts':
            df[j]=pd.to_datetime(df[j],utc=True)
        elif j=='is_business_account':
            df[j].fillna(False,inplace=True) ## Assuming the NAN field in 'is_buisness_account' column corresponds to False(it is not a buisness account)
    
    return df