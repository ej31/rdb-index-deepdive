from matplotlib import pyplot as plt

from statics import all_data, labels

indexed_data = all_data[:3]
non_indexed_data = all_data[3:]

labels_indexed = labels[:3]
labels_non_indexed = labels[3:]

plt.figure(figsize=(14, 10))

plt.subplot(1, 2, 1)
plt.boxplot(indexed_data, labels=labels_indexed, notch=True, patch_artist=True)
plt.title('Indexed Query 실행시간 분포')
plt.ylabel('실행 시간 (s)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

plt.subplot(1, 2, 2)
plt.boxplot(non_indexed_data, labels=labels_non_indexed, notch=True, patch_artist=True)
plt.title('Non-Indexed Query 실행시간 분포')
plt.ylabel('실행시간 (s)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
