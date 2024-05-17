from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
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
            description = " "
        language = repo.find('span', {'itemprop': 'programmingLanguage'})
        if language:
            language = language.text.strip()
        else:
            language = "Unknown"
        last_updated = repo.find('relative-time')
        if last_updated:
            last_updated = last_updated.text.strip()
            last_updated = datetime.strptime(last_updated, "%b %d, %Y").strftime("%Y-%m-%d")
            last_updated_date = datetime.strptime(last_updated, "%Y-%m-%d")
            current_date = datetime.now()
            time_diff = current_date - last_updated_date
            if time_diff.days < 7:
                last_updated_readable = f"{time_diff.days} days ago"
            elif time_diff.days < 365:
                last_updated_readable = f"{time_diff.days // 7} weeks ago"
            else:
                last_updated__readable = f"{time_diff.days // 365} years ago"
        else:
            last_updated = "Unknown"
            last_updated_readable = "Unknown"
        repo_list.append({
            'name': repo_name,
            'url': repo_url,
            'description': description,
            'language': language,
            'last_updated': last_updated,
            'last_updated_-_readable': last_updated_readable
        })

    return repo_list

@app.route('/<username>', methods=['GET'])
def repos(username):
    repos = get_public_repos(username)
    response = {
        'made_by': 'Sankeer',
        'my_source_code': 'https://github.com/sankeer28/Git-Scraper',
        'repos': repos
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
