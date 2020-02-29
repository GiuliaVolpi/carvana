def fill_nall_with_mode(x):
    return x.fillna(x.mode(dropna=False)[0])

def fill_nall_with_median(x):
    return x.fillna(x.median())

def cleaning(df):
    ###########################################
    #Fill missing values
    ###########################################

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

    #values 0.0 and 1.0 in MMRs are treated like missing values
    features = [    ['MMRAcquisitionAuctionAveragePrice','MMRCurrentAuctionAveragePrice'],
                    ['MMRAcquisitionAuctionCleanPrice','MMRCurrentAuctionCleanPrice'],
                    ['MMRAcquisitionRetailAveragePrice','MMRCurrentRetailAveragePrice'],
                    ['MMRAcquisitonRetailCleanPrice','MMRCurrentRetailCleanPrice'],
                    ['MMRCurrentAuctionAveragePrice','MMRAcquisitionAuctionAveragePrice'],
                    ['MMRCurrentAuctionCleanPrice','MMRAcquisitionAuctionAveragePrice'],
                    ['MMRCurrentRetailAveragePrice','MMRAcquisitionRetailAveragePrice'],
                    ['MMRCurrentRetailCleanPrice','MMRAcquisitionRetailAveragePrice']
                ]
    for feature in features:
        for value in [0.0, 1.0]:
            a = df[df[feature[0]]== value].index
            for x in a:
                df[feature[0]].values[x] = df[feature[1]].values[x]
            df.loc[df[feature[0]] == value, feature[0]] = df[feature[0]].median()

    
    ###########################################
    #Typo correction
    ###########################################
    df.iat[6895, 11]    =   'MANUAL'
    df.iat[42627, 6]    =   'SCION'

    #a = df[(df['Nationality']=='TOP LINE ASIAN') | (df['Nationality']=='OTHER ASIAN')].index
    #for x in a:
    #    df['Nationality'].values[x] = 'ASIAN'
    
    # WheelTypeID 0.0 correction
    df.iat[3897, 12]    =   1.0
    df.iat[23432, 12]   =   1.0
    df.iat[23831, 12]   =   2.0
    df.iat[45666, 12]   =   1.0

    # submodel la mode sui group by 
    # Praticamente è la mode sui group by (più o meno specifici)

    df.iat[28961, 9] = '4D SEDAN SE1'
    df.iat[35224, 9] = '4D SEDAN SXT FFV'
    df.iat[48641, 9] = '4D SEDAN SXT FFV'
    df.iat[28280, 9] = 'PASSENGER 3.9L SE'
    df.iat[33225, 9] = '4D SUV 4.6L'
    df.iat[50661, 9] = 'REG CAB 2.2L FFV'
    df.iat[23019, 9] = '4D SEDAN'

    # size la mode sui group by
    df.iat[18532, 16] = 'MEDIUM' #'MEDIUM SUV'
    df.iat[20016, 16] = 'MEDIUM' #'SMALL SUV'
    df.iat[35157, 16] = 'MEDIUM' #'SMALL SUV'
    df.iat[15769, 16] = 'MEDIUM' #'MEDIUM SUV'

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
    
    ###########################################
    #Row deletion outliers
    ###########################################

    #Continuos features
    features = [    'VehOdo',
                    'MMRAcquisitionAuctionAveragePrice',
                    #'MMRAcquisitionAuctionCleanPrice', 
                    'MMRAcquisitionRetailAveragePrice',
                    #'MMRAcquisitonRetailCleanPrice',
                    'MMRCurrentAuctionAveragePrice',
                    #'MMRCurrentAuctionCleanPrice',
                    'MMRCurrentRetailAveragePrice',
                    #'MMRCurrentRetailCleanPrice',
                    'VehBCost',
                    'WarrantyCost',
                    'VehicleAge']
    for feature in features:
        for isBadBuy in [0,1]:
            q1 = df[(df.IsBadBuy == isBadBuy)][feature].quantile(0.25)
            q3 = df[(df.IsBadBuy == isBadBuy)][feature].quantile(0.75)
            iqr = q3 - q1
            qlow = q1 - 1.5*iqr
            qhigh = q3 + 1.5*iqr

            df.drop(df[(df.IsBadBuy == isBadBuy) & (df[feature] <= qlow)].index, inplace=True)
            df.drop(df[(df.IsBadBuy == isBadBuy) & (df[feature] >= qhigh)].index, inplace=True)
