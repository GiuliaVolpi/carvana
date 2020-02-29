import re

def add_features(df):
    ###########################################
    #Add features
    ###########################################

    df['TrimLevel']="nan" #index 34
    df['BodyStyle']="nan" #index 35

    ###########################################
    #Populate BodyStyle
    ###########################################
    a = df.index

    #Look SubModel (index 9)
    #Convertible
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" CONVERTIBLE ", txt) or re.search(" CONVERTIBLE", txt) or re.search("CONVERTIBLE ", txt):
            df.iat[x, 35] = "Convertible"

    #Sedan
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" SEDAN ", txt) or re.search(" SEDAN", txt) or re.search("SEDAN ", txt):
            df.iat[x, 35] = "Sedan"

    #Hatchback
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" HATCHBACK ", txt) or re.search(" HATCHBACK", txt) or re.search(" HATCKBACK ", txt):
            df.iat[x, 35] = "Hatchback"

    #Wagon
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" WAGON ", txt) or re.search("WAGON ", txt) or re.search(" WAGON", txt):
            df.iat[x, 35] = "Wagon"

    #Truck 
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" CAB ", txt) or re.search("CAB ", txt) or re.search(" CAB", txt):
            df.iat[x, 35] = "Truck"

    #SUV
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" SUV ", txt) or re.search(" SUV", txt) or re.search(" SUV*", txt) or re.search("SUV ", txt) or re.search("SPORT UTILITY", txt) or re.search(" SPORT UTILITY ", txt) or re.search(" SPORT UTILITY", txt):
            df.iat[x, 35] = "SUV"

    #Crossover
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" CROSSOVER ", txt) or re.search("CROSSOVER ", txt) or re.search(" CROSSOVER", txt) or re.search(" CUV ", txt) or re.search("CUV ", txt) or re.search(" CUV", txt) or re.search("XUV", txt):
            df.iat[x, 35] = "Crossover"

    #Coupe
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" COUPE ", txt) or re.search(" COUPE", txt) or re.search("COUPE ", txt):
            df.iat[x, 35] = "Coupe"

    #Van
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search(" MINIVAN ", txt) or re.search(" MINIVAN", txt) or re.search("MINIVAN ", txt) or re.search(" VAN ", txt) or re.search("VAN ", txt) or re.search(" VAN", txt):
            df.iat[x, 35] = "Van"

    #Jeep
    for x in a:
        txt = str(df.iat[x, 9])
        if re.search("JEEP ", txt):
            df.iat[x, 35] = "Jeep"

    #Look Size (index 16)
    b = df[df["BodyStyle"]=="nan"].index

    #Crossover
    for x in b:
        txt = str(df.iat[x, 16])
        if re.search("CROSSOVER", txt):
            df.iat[x, 35] = "Crossover"

    #Truck
    for x in b:
        txt = str(df.iat[x, 16])
        if re.search("SMALL TRUCK", txt):
            df.iat[x, 35] = "Truck"

    #SUV
    for x in b:
        txt = str(df.iat[x, 16])
        if re.search("LARGE SUV", txt) or re.search("MEDIUM SUV", txt) or re.search("SMALL SUV", txt):
            df.iat[x, 35] = "SUV"

    #Van
    for x in b:
        txt = str(df.iat[x, 16])
        if re.search("VAN", txt):
            df.iat[x, 35] = "Van"

    #Look Model (index 7)
    c = df[df["BodyStyle"]=="nan"].index 

    #Sedan
    for x in c:
        txt = str(df.iat[x, 7])
        if re.search("MAZDA3", txt) or re.search("LANCER", txt) or re.search("STRATUS", txt) or re.search("TAURUS", txt) or re.search("IMPALA 3.4L V6 SFI", txt) or re.search("GRAND AM V6 3.4L V6", txt):
            df.iat[x, 35] = "Sedan"

    #Convertible
    for x in c:
        txt = str(df.iat[x, 7])
        if re.search("ECLIPSE", txt) or re.search("SOLSTICE", txt):
            df.iat[x, 35] = "Convertible"

    #Truck
    for x in c:
        txt = str(df.iat[x, 7])
        if re.search("SIERRA 1500", txt):
            df.iat[x, 35] = "Truck"

    #Coupe
    for x in c:
        txt = str(df.iat[x, 7])
        if re.search("CELICA", txt):
            df.iat[x, 35] = "Coupe"