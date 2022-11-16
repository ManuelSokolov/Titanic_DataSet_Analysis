import pandas as pd
import Data_Analysis
from preprocess import preprocess
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC



if __name__ == '__main__':
    # read data set
    df = pd.read_csv("./input/KCPD_Crime_Data_2016.csv", sep=',')
    df.drop(['From_Date', 'From_Time', 'To_Date', 'To_Time', 'IBRS', 'Beat', 'Rep_Dist','DVFlag', 'Invl_No'], axis=1, inplace=True)
    df = df.sort_values(["Reported_Date","Reported_Time"])
    train, test = train_test_split(df, test_size=0.85, shuffle=False)
    


    # preprocess the column with content
   # pd = preprocess(dataset)
   # dataset_clean = pd.preprocess_col('content')
    # da = Data_Analysis.Data_Analysis(df)
    # da.data_profiling()











