import json
import matplotlib.pyplot as plt

# Load language data from the JSON file
with open("language_data.json", "r") as f:
    data = json.load(f)

# Sort data by percentage (descending)
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
languages = [item[0] for item in sorted_data]
percentages = [item[1] for item in sorted_data]

# Define colors for the chart (extended palette)
colors = ["#8FBCBB", "#88C0D0", "#81A1C1", "#B48EAD", "#D08770", "#A3BE8C", "#EBCB8B", "#BF616A"]

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
plt.style.use('dark_background')

bars = plt.barh(languages, percentages, color=colors[:len(languages)])

# Add percentage labels on the bars
for i, (bar, percentage) in enumerate(zip(bars, percentages)):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
             f'{percentage:.1f}%', 
             va='center', ha='left', color='white', fontweight='bold')

# Customize the chart
plt.xlabel('Percentage (%)', color='white', fontsize=12)
plt.title('Programming Languages Used Across Public and Private Repositories', color='white', fontsize=16, fontweight='bold', pad=20)
plt.gca().set_facecolor('#2E3440')
plt.gcf().patch.set_facecolor('#2E3440')

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('white')
plt.gca().spines['bottom'].set_color('white')

# Set tick colors
plt.gca().tick_params(colors='white')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart as an image
plt.savefig("language_usage_chart.png", dpi=150, facecolor="#2E3440", bbox_inches='tight')
plt.show()