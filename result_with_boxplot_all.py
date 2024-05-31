import matplotlib.pyplot as plt

from statics import labels, all_data

fig, ax = plt.subplots(figsize=(12, 8))
ax.boxplot(all_data, labels=labels, notch=True, patch_artist=True)

ax.set_ylabel('실행시간 (s)')
ax.set_title('실행시간 분포 비교')
ax.grid(True, linestyle='--', alpha=0.6)

# Use setp function to set xtick labels rotation
labels = ax.get_xticklabels()
plt.setp(labels, rotation=90)

# Adjust the space between plots
plt.subplots_adjust(wspace=2)

plt.show()
