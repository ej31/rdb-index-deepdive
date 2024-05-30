import matplotlib.pyplot as plt

from statics import labels, all_data

plt.figure(figsize=(12, 8))
plt.boxplot(all_data, labels=labels, notch=True, patch_artist=True)

plt.ylabel('실행시간 (s)')
plt.title('실행시간 분포 비교')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
