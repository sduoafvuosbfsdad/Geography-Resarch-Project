import matplotlib.pyplot as plt

# Data from JSON
data = {
          "Tourism/Leisure": 15,
          "Business/Work": 6,
          "Visiting Friends/Family": 4,
          "Study/Events": 2,
          "Other/Unspecified": 2
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

plt.title('Purpose of Visit', pad=20)
plt.tight_layout()
plt.savefig('Qn2.png', dpi=300, bbox_inches='tight')
