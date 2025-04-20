import json
import seaborn as sns
import matplotlib.pyplot as plt

# Load language data from the JSON file
with open("language_data.json", "r") as f:
    data = json.load(f)

# Prepare data for plotting
languages = list(data.keys())
percentages = list(data.values())

# Set a dark theme and custom color palette
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#2E3440", "figure.facecolor": "#2E3440"})
custom_palette = ["#8FBCBB", "#88C0D0", "#81A1C1", "#B48EAD", "#D08770"]  # Blue, purple, orange tones

# Create a bar chart using seaborn
plt.figure(figsize=(8, 4))
sns.barplot(x=languages, y=percentages, palette=custom_palette, edgecolor="black")
plt.xlabel("Languages", fontsize=10, color="white")
plt.ylabel("Usage Percentage", fontsize=10, color="white")
plt.title("Programming Language Usage", fontsize=12, color="white")
plt.xticks(rotation=45, fontsize=8, color="white")
plt.yticks(fontsize=8, color="white")
plt.tight_layout(pad=1.5)

# Save the chart as an image
plt.savefig("language_usage_chart.png", dpi=150, facecolor="#2E3440")  # Match background color
plt.show()