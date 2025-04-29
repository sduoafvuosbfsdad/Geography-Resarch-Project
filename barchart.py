import matplotlib.pyplot as plt

# Sample data
data = {
          "1 time": 19,
          "2 times": 4,
          "3 times": 2,
          "4 times": 2,
          "5 times": 3
        }

categories = data.keys()
values = data.values()

# Create figure and axis
fig, ax = plt.subplots()

# Plot bars
bars = ax.bar(categories, values, color='skyblue')

# Customize chart
ax.set_title('Sample Bar Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height}',
            ha='center', va='bottom')

plt.title('Frequency of Visit', pad=20)
plt.tight_layout()
plt.savefig('Qn3.png', dpi=300, bbox_inches='tight')