import json
import matplotlib.pyplot as plt

# Load language data from the JSON file
with open("language_data.json", "r") as f:
    data = json.load(f)

# Prepare data for plotting
languages = list(data.keys())
percentages = list(data.values())

# Create a bar chart
plt.figure(figsize=(8, 4))  # Adjusted size for better fit in README
plt.bar(languages, percentages, color="skyblue", edgecolor="black")
plt.xlabel("Languages", fontsize=10)
plt.ylabel("Usage Percentage", fontsize=10)
plt.title("Programming Language Usage", fontsize=12)
plt.xticks(rotation=45, fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=1.5)  # Adjust padding for better spacing

# Save the chart as an image
plt.savefig("language_usage_chart.png", dpi=150)  # Higher DPI for better quality
plt.show()