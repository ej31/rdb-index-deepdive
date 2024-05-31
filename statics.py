import pandas as pd

file_paths = [
    "240531_012314_employees_nonindexed_2014-01-01_2015-01-01_loop_100.csv",
    "240531_012314_employees_nonindexed_2014-01-01_2016-01-01_loop_100.csv",
    "240531_012314_employees_nonindexed_2014-01-01_2017-01-01_loop_100.csv",
    "240531_012314_employees_indexed_2014-01-01_2015-01-01_loop_100.csv",
    "240531_012314_employees_indexed_2014-01-01_2016-01-01_loop_100.csv",
    "240531_012314_employees_indexed_2014-01-01_2017-01-01_loop_100.csv",
    "240531_012314_employees_indexed_with_composite_2014-01-01_2015-01-01_loop_100.csv",
    "240531_012314_employees_indexed_with_composite_2014-01-01_2016-01-01_loop_100.csv",
    "240531_012314_employees_indexed_with_composite_2014-01-01_2017-01-01_loop_100.csv",
]
averages = []
labels = (
    "noIdx y1",
    "noIdx y2",
    "noIdx y3",
    "idx y1",
    "idx y2",
    "idx y3",
    "cidx y1",
    "cidx y2",
    "cidx y3",
)


def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1

    # 이상치 범위를 정의 (Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)
    outlier_range = (df[column_name] >= Q1 - 1.5 * IQR) & (df[column_name] <= Q3 + 1.5 * IQR)

    # 이상치 범위에 속하지 않는 값을 제거
    return df.loc[outlier_range]


all_data = [pd.read_csv(file)['Execution Time'] for file in file_paths]

# 각 파일에 대해 이상치 제거
for i, file_path in enumerate(file_paths):
    data = pd.read_csv(file_path)
    data = remove_outliers(data, 'Execution Time')
    all_data[i] = data['Execution Time']
