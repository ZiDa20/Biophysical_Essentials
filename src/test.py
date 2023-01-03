import matplotlib.pyplot as plt
import pandas as pd
# Assume that we have a Pandas dataframe with two columns:
# 'Category' and 'Amount'
df = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Amount': [10, 20, 30]})

# Calculate the total amount for all categories
total = df['Amount'].sum()

# Set the figure size
plt.figure(figsize=(6,6))

# Create the donut chart
plt.pie(df['Amount'], labels=df['Category'], autopct=lambda p: '{:.0f}'.format(p * total / 100))
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a title
plt.title("Category Breakdown")

# Display the plot
plt.show()
