import matplotlib.pyplot as plt

# Data from JSON
data = {
          "0-20k": 4,
          "20k-40k": 5,
          "40k-60k": 8,
          "60k-80k": 4,
          "80k-100k": 4,
          ">100k": 3,
          "Unspecified/Other": 5
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

plt.title('Income Levels', pad=20)
plt.tight_layout()
plt.savefig('Qn9.png', dpi=300, bbox_inches='tight')
