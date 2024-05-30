import pandas as pd

file_paths = [
    "employees_indexed_query_execution_times_140101-140105_loop_1000.csv",
    "employees_indexed_query_execution_times_140101-140110_loop_1000.csv",
    "employees_indexed_query_execution_times_140101-140120_loop_100.csv",
    "employees_nonindexed_query_execution_times_140101-140105_loop_10.csv",
    "employees_nonindexed_query_execution_times_140101-140110_loop_10.csv",
    "employees_nonindexed_query_execution_times_140101-140120_loop_10.csv"
]
averages = []
labels = [
    "Indexed 140101-140105 (1000x)",
    "Indexed 140101-140110 (1000x)",
    "Indexed 140101-140120 (100x)",
    "Non-Indexed 140101-140105 (10x)",
    "Non-Indexed 140101-140110 (10x)",
    "Non-Indexed 140101-140120 (10x)"
]
all_data = [pd.read_csv(file)['Execution Time'] for file in file_paths]
