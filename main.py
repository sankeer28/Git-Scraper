import requests
from bs4 import BeautifulSoup
from hyperlink import URL
from colorama import init, Fore, Style

init()

def print_link(title, url, description):
    url = URL.from_text(url)
    print(f'{Fore.GREEN}\x1b]8;;{url}\x1b\\{title}\x1b]8;;\x1b\\{Style.RESET_ALL}: {Fore.BLUE}{description}{Style.RESET_ALL}')

def get_public_repos():
    purple = '\033[95m'  
    print(f'{purple}'
          '   ________.__  __              _________\n'
          '  /  _____/|__|/  |_           /   _____/ ________________  ______   ___________\n'
          ' /   \  ___|  \   __\  ______  \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \_  __ \ \n'
          ' \    \_\  \  ||  |   /_____/  /        \  \___|  | \// __ \|  |_> >  ___/|  | \/\n'
          '  \______  /__||__|           /_______  /\___  >__|  (____  /   __/ \___  >__|   \n'
          '         \/                           \/     \/           \/|__|        \/    '
          f'{Style.RESET_ALL}')

    github_link = URL.from_text("GitHub")
    github_link = f"\x1b]8;;{github_link}https://github.com/sankeer28/Git-Scraper\x1b\\{github_link}\x1b]8;;\x1b\\"
    print(f'{Fore.GREEN}{github_link}{Style.RESET_ALL}')
    print(f'{Fore.RED}Enter the GitHub username: ', end='', flush=True)  
    username = input(f'{Fore.YELLOW}')
    url = f"https://github.com/{username}?tab=repositories&q=&type=public&language=&sort="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    repos = soup.find_all('div', {'class': 'col-10 col-lg-9 d-inline-block'})

    for repo in repos:
        repo_name = repo.find('h3').text.strip().split('\n')[0]  
        repo_url = f"https://github.com/{username}/{repo_name}"  
        description = repo.find('p', {'class': 'col-9 d-inline-block color-fg-muted mb-2 pr-4'})
        if description:
            description = description.text.strip()
        else:
            description = "No description provided"
        print_link(repo_name, repo_url, description)  

get_public_repos()
