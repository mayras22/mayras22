import json
import matplotlib.pyplot as plt

# Load language data from the JSON file
with open("language_data.json", "r") as f:
    data = json.load(f)

# Prepare data for plotting
languages = list(data.keys())
percentages = list(data.values())

# Define colors for the chart
colors = ["#8FBCBB", "#88C0D0", "#81A1C1", "#B48EAD", "#D08770"]  # Blue, purple, orange tones

# Create a pie chart
plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(
    percentages,
    labels=languages,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    textprops={"color": "white", "fontsize": 10}  # Ensure text is visible
)

# Adjust label positions to avoid overlap
for text in texts:
    text.set_color("white")  # Set label color to white for visibility
    text.set_fontsize(10)    # Increase font size for better readability

# Add a circle at the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc="#2E3440")  # Dark background
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add a title
plt.title("Programming Language Usage", color="white", fontsize=14)

# Save the chart as an image
plt.savefig("language_usage_chart.png", dpi=150, facecolor="#2E3440")  # Match background color
plt.show()