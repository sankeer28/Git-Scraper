from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from hyperlink import URL

app = Flask(__name__)

def get_public_repos(username):
    url = f"https://github.com/{username}?tab=repositories&q=&type=public&language=&sort="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    repos = soup.find_all('div', {'class': 'col-10 col-lg-9 d-inline-block'})

    repo_list = []
    for repo in repos:
        repo_name = repo.find('h3').text.strip().split('\n')[0]
        repo_url = f"https://github.com/{username}/{repo_name}"
        description = repo.find('p', {'class': 'col-9 d-inline-block color-fg-muted mb-2 pr-4'})
        if description:
            description = description.text.strip()
        else:
            description = "No description provided"
        repo_list.append({
            'name': repo_name,
            'url': repo_url,
            'description': description
        })

    return repo_list

@app.route('/<username>', methods=['GET'])
def repos(username):
    repos = get_public_repos(username)
    return jsonify(repos)

if __name__ == '__main__':
    app.run(debug=True)
