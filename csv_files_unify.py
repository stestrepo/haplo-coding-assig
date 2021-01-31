import os
import pandas as pd

def unify():
    df = []
    path = "Files_required"
    dirs = os.listdir(path)
    count_file = list(map(lambda x: "Files_required/"+str(x),dirs))
    numberofsheets = len(count_file)

    for i in range(0,numberofsheets):
        try:
            data = pd.read_csv(count_file[i],header=None)
            df.append(data)
        except:
            pass
        print(i)

    filename= "Unified_csv.csv"
    df = pd.concat(df)
    df.to_csv(filename,header=None,index=False)

unify()