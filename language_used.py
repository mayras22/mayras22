import requests
import os
import json

# GitHub API token and username
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Read the token from the environment variable
USERNAME = "mayras22"

# Headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# Fetch all repositories (including private, forked, and collaborator repos)
def get_repositories():
    all_repos = []
    
    # Get repositories you own or are a member of
    url1 = f"https://api.github.com/user/repos?per_page=100&type=all"
    response1 = requests.get(url1, headers=headers)
    response1.raise_for_status()
    owned_repos = response1.json()
    all_repos.extend(owned_repos)
    
    # Get repositories where you're a collaborator
    url2 = f"https://api.github.com/user/repos?per_page=100&affiliation=collaborator"
    response2 = requests.get(url2, headers=headers)
    if response2.status_code == 200:
        collaborator_repos = response2.json()
        all_repos.extend(collaborator_repos)
    
    # Remove duplicates (in case a repo appears in both lists)
    unique_repos = {}
    for repo in all_repos:
        unique_repos[repo['id']] = repo
    
    final_repos = list(unique_repos.values())
    
    print(f"Found {len(final_repos)} total repositories:")
    print(f"  - Owned/Member repos: {len(owned_repos)}")
    print(f"  - Collaborator repos: {len(collaborator_repos) if response2.status_code == 200 else 0}")
    
    for repo in final_repos:
        owner_type = "YOU" if repo['owner']['login'] == USERNAME else repo['owner']['login']
        print(f"  - {repo['full_name']} ({'private' if repo['private'] else 'public'}) [Owner: {owner_type}]")
    
    return final_repos

# Fetch language data for a repository
def get_languages(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/languages"
    print(f"Fetching languages for repository: {repo_full_name} (URL: {url})")  # Debugging
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print(f"Repository not found: {repo_full_name}")
    response.raise_for_status()
    return response.json()

# Aggregate language data
def aggregate_languages():
    repos = get_repositories()
    language_totals = {}

    for repo in repos:
        repo_full_name = repo["full_name"]  # This includes owner/repo_name
        repo_name = repo["name"]
        print(f"Processing repository: {repo_full_name}")  # Show which repos are being processed
        try:
            languages = get_languages(repo_full_name)
            for lang, bytes_used in languages.items():
                language_totals[lang] = language_totals.get(lang, 0) + bytes_used
        except requests.exceptions.HTTPError as e:
            print(f"Error fetching languages for {repo_full_name}: {e}")  # Log the error and continue
            continue

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
    
    print("\n=== AGGREGATED LANGUAGE DATA ===")
    total_bytes = sum(language_totals.values())
    for lang, bytes_used in sorted(language_totals.items(), key=lambda x: x[1], reverse=True):
        percentage = (bytes_used / total_bytes) * 100
        print(f"{lang}: {bytes_used:,} bytes ({percentage:.1f}%)")

    percentages = calculate_percentages(language_totals)
    save_to_file(percentages)
    print(f"\nLanguage usage data saved to language_data.json")
    print(f"Total code analyzed: {total_bytes:,} bytes across {len(language_totals)} languages")