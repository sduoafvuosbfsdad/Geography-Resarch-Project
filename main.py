import matplotlib.pyplot as plt

# Data from JSON
data = {
        "Tourist": 24,
        "Visitor": 6
      }

# Prepare data
categories = list(data.keys())
values = list(data.values())

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(values,
        labels=categories,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops={'edgecolor': 'white'})

plt.title('Tourist vs Visitor', pad=20)
plt.tight_layout()
plt.savefig('Qn7.png', dpi=300, bbox_inches='tight')
