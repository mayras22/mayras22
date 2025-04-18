import requests
import os
import sys

def get_languages(token):
    if not token:
        print("Error: LANGUAGES_USED environment variable is not set.")
        sys.exit(1)

    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    languages = {}

    page = 1
    while True:
        response = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            sys.exit(1)

        repos = response.json()
        if not repos:
            break

        for repo in repos:
            lang_url = repo["languages_url"]
            lang_response = requests.get(lang_url, headers=headers)
            if lang_response.status_code != 200:
                print(f"Error retrieving languages for {repo['name']}")
                continue

            repo_languages = lang_response.json()
            for lang, count in repo_languages.items():
                languages[lang] = languages.get(lang, 0) + count

        page += 1

    sorted_languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))
    return sorted_languages

if __name__ == "__main__":
    token = os.getenv("LANGUAGES_USED")  # Retrieve token from environment variable
    languages = get_languages(token)

    if languages:
        with open("languages.md", "w") as f:
            f.write("# Languages Used in Repositories\n\n")
            for lang, count in languages.items():
                f.write(f"- {lang}: {count} bytes\n")