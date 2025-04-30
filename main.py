import matplotlib.pyplot as plt

# Data from JSON
data = {
          "Scenery": 13,
          "Shopping": 8,
          "Dining": 9,
          "Entertainment": 8,
          "Special Events": 4,
          "Culture/Architecture": 3
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

plt.title('Main Reasons to Visist', pad=20)
plt.tight_layout()
plt.savefig('Qn4.png', dpi=300, bbox_inches='tight')
