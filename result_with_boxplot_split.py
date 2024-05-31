from matplotlib import pyplot as plt

from statics import all_data, labels

non_indexed_data = all_data[0:3]
indexed_data = all_data[3:6]
comp_indexed_data = all_data[6:9]

labels_non_indexed = labels[0:3]
labels_indexed = labels[3:6]
labels_comp_indexed = labels[6:9]

plt.figure(figsize=(14, 10))

# Plot non-indexed data
plt.boxplot(non_indexed_data, positions=range(len(non_indexed_data)), widths=0.4, patch_artist=True, labels=labels_non_indexed)
plt.xticks(range(len(non_indexed_data)), labels_non_indexed, rotation=45)

# Plot composite indexed data
plt.boxplot(comp_indexed_data, positions=[i + len(non_indexed_data) + len(comp_indexed_data) for i in range(len(comp_indexed_data))], widths=0.4,
            patch_artist=True,
            labels=labels_comp_indexed)
plt.xticks([i + len(non_indexed_data) + len(comp_indexed_data) for i in range(len(comp_indexed_data))], labels_comp_indexed, rotation=45)

# Plot indexed data
plt.boxplot(indexed_data, positions=[i + len(non_indexed_data) for i in range(len(indexed_data))], widths=0.4,
            patch_artist=True, labels=labels_indexed)
plt.xticks([i + len(non_indexed_data) for i in range(len(indexed_data))], labels_indexed, rotation=45)

plt.title('Query 실행시간 분포')
plt.ylabel('실행 시간 (s)')
plt.grid(True, linestyle=':', alpha=0.2)
plt.show()
