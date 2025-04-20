import json
import matplotlib.pyplot as plt

# Load language data from the JSON file
with open("language_data.json", "r") as f:
    data = json.load(f)

# Prepare data for plotting
languages = list(data.keys())
percentages = list(data.values())

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(languages, percentages, color="skyblue")
plt.xlabel("Languages")
plt.ylabel("Usage Percentage")
plt.title("Programming Language Usage")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as an image
plt.savefig("language_usage_chart.png")
plt.show()