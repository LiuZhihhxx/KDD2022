import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
import datetime

# def data_prepare():

# readfull.csv
data_path = os.path.join(os.getcwd(), 'data')
filename = 'wtbdata_245days.csv'  # 'sdwpf_baidukddcup2022_full.CSV'
# location_name = 'sdwpf_baidukddcup2022_turb_location.CSV'
df_raw = pd.read_csv(os.path.join(data_path, filename))

# 1.Patv<0
df = df_raw.copy(deep=True)
df['Patv'].loc[df['Patv'] < 0] = 0


# KNN imputer
# df_raw[df_raw['Patv'].isnull()].index  # index of nulls
def knn_Imputer(df, neighbors=10):
    t1 = datetime.datetime.now()
    print('present time: ', t1)
    print('KNN running...')
    imputer = KNNImputer(n_neighbors=neighbors)  # imputer
    df_knn = imputer.fit_transform(df.iloc[:, 3:])  # numpy.ndarray
    print('time consumption: ', datetime.datetime.now() - t1)
    return pd.DataFrame(df_knn)  # pd.df


df_knn = knn_Imputer(df)
df_knn = pd.concat([df.iloc[:, :3], df_knn], axis=1)
df_knn.isna().index  # check null

df_knn.columns = df_raw.columns
df_knn.to_csv('wtdata_245days_knned.CSV', index=False, encoding='utf-8')
