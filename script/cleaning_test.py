def fill_nall_with_mode(x):
    return x.fillna(x.mode(dropna=False)[0])

def fill_nall_with_median(x):
    return x.fillna(x.median())

def cleaning(df):
    ###########################################
    #Fill missing values
    ###########################################
    
    df.drop(df[df.WheelTypeID == 0.0].index, inplace=True)

    #For WheelTypeID we have applied a recursively groupby substitution
    df['WheelTypeID'] = df.groupby(['Make','Model','SubModel'])['WheelTypeID'].apply(fill_nall_with_mode)
    df['WheelTypeID'] = df.groupby(['Make', 'Model'])['WheelTypeID'].apply(fill_nall_with_mode)
    df['WheelTypeID'] = df.groupby(['Make'])['WheelTypeID'].apply(fill_nall_with_mode)
    #df['WheelType'] = df.groupby(['Make','Model','SubModel'])['WheelType'].apply(fill_nall_with_mode)
    df['Color'] = df['Color'].fillna(df['Color'].mode()[0])
    df['Transmission'] = df['Transmission'].fillna(df['Transmission'].mode()[0])
    df['Nationality'] = df['Nationality'].fillna('AMERICAN')

    df['MMRAcquisitionAuctionAveragePrice'] = df.groupby(['Model'])['VehBCost'].apply(fill_nall_with_median)

    # Acquisition missing valyueprice has been subst with the meadian
    #df['MMRAcquisitionAuctionAveragePrice'] = df['MMRAcquisitionAuctionAveragePrice'].fillna(df['MMRAcquisitionAuctionAveragePrice'].median())
    df['MMRAcquisitionAuctionCleanPrice'] = df['MMRAcquisitionAuctionCleanPrice'].fillna(df['MMRAcquisitionAuctionCleanPrice'].median())
    df['MMRAcquisitionRetailAveragePrice'] = df['MMRAcquisitionRetailAveragePrice'].fillna(df['MMRAcquisitionRetailAveragePrice'].median())
    df['MMRAcquisitonRetailCleanPrice'] = df['MMRAcquisitonRetailCleanPrice'].fillna(df['MMRAcquisitonRetailCleanPrice'].median())

    # current missing value price has been subst with most correlated acquisition same row
    df['MMRCurrentAuctionAveragePrice'] = df['MMRCurrentAuctionAveragePrice'].fillna(df['MMRAcquisitionAuctionAveragePrice'])
    df['MMRCurrentAuctionCleanPrice'] = df['MMRCurrentAuctionCleanPrice'].fillna(df['MMRAcquisitionAuctionAveragePrice'])
    df['MMRCurrentRetailAveragePrice'] = df['MMRCurrentRetailAveragePrice'].fillna(df['MMRAcquisitionRetailAveragePrice'])
    df['MMRCurrentRetailCleanPrice'] = df['MMRCurrentRetailCleanPrice'].fillna(df['MMRAcquisitonRetailCleanPrice'])
    
    ###########################################
    #Dropped features
    ###########################################
    del df['PRIMEUNIT']
    del df['AUCGUART']
    del df['RefId']
    del df['VNZIP1']
    #del df['Auction']
    del df['IsOnlineSale']
    del df['Transmission']
    del df['Nationality']
    del df['SubModel']
    del df['Model']
    del df['Make']
    del df['Color']
    del df['VehYear']
    del df['PurchDate']
    del df['Trim']
    del df['TopThreeAmericanName']
    del df['WheelType']
    del df['BYRNO']
    del df['MMRAcquisitionAuctionCleanPrice']
    #del df['MMRAcquisitionRetailAveragePrice']
    del df['MMRAcquisitonRetailCleanPrice']
    #del df['MMRCurrentAuctionAveragePrice']
    del df['MMRCurrentAuctionCleanPrice']
    #del df['MMRCurrentRetailAveragePrice']
    del df['MMRCurrentRetailCleanPrice']
    