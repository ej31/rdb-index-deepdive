import matplotlib.pyplot as plt
import pandas as pd

from statics import file_paths, averages, labels

for file in file_paths:
    data = pd.read_csv(file)
    average_time = data['Execution Time'].mean()
    averages.append(average_time)

plt.figure(figsize=(10, 6))
# plt.bar(labels, averages,width=0.6, color='skyblue')
plt.bar(range(len(labels)), averages, tick_label=labels, width=0.6, color='skyblue')

plt.ylabel('평균 실행 시간 (s)')
plt.title('평균 실행시간 비교')
plt.xticks(rotation=45)
plt.show()