import matplotlib.pyplot as plt

# Data from JSON
data = {
    "Tourism/Sightseeing": 10,
    "Business/Work": 5,
    "Friends/Family": 4,
    "Food/Culture": 4,
    "Media/Entertainment": 3,
    "Other/Unspecified": 3
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

plt.title('What Attracted You to Singapore', pad=20)
plt.tight_layout()
plt.savefig('Qn1.png', dpi=300, bbox_inches='tight')
