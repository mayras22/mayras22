import requests
import os
import json

# GitHub API token and username
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]  # Read the token from the environment variable
USERNAME = "mayras22"

# Headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# Fetch all repositories (including private and forked)
def get_repositories():
    url = f"https://api.github.com/user/repos?per_page=100&type=all"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Fetch language data for a repository
def get_languages(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/languages"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Aggregate language data
def aggregate_languages():
    repos = get_repositories()
    language_totals = {}

    for repo in repos:
        repo_name = repo["name"]
        languages = get_languages(repo_name)
        for lang, bytes_used in languages.items():
            language_totals[lang] = language_totals.get(lang, 0) + bytes_used

    return language_totals

# Calculate percentages
def calculate_percentages(language_totals):
    total_bytes = sum(language_totals.values())
    return {lang: (bytes_used / total_bytes) * 100 for lang, bytes_used in language_totals.items()}

# Save data to a JSON file
def save_to_file(data, filename="language_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Main function
if __name__ == "__main__":
    language_totals = aggregate_languages()
    percentages = calculate_percentages(language_totals)
    save_to_file(percentages)
    print("Language usage data saved to language_data.json")