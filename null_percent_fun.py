def percent_null (df):
    total_null = df.isnull().sum().sort_values(ascending=False) #First sum and order all null values for each variable
    percentage = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False) #Get the percentage
    missing_data = pd.concat([total_null, percentage], axis=1, keys=['Total', 'Percentage'])
    return missing_data