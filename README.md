# Git-Scraper
```
  ________ __  __              _________
 /  _____/|__|/  |_           /   _____/ ________________  ______   ___________
/   \  ___|  \   __\  ______  \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \_  __ \ 
\    \_\  \  ||  |   /_____/  /        \  \___|  | \// __ \|  |_> >  ___/|  | \/
 \______  /__||__|           /_______  /\___  >__|  (____  /   __/ \___  >__|   
        \/                           \/     \/           \/|__|        \/    
```
### Given GitHub username, returns users' public repos and respective descriptions in CLI
### Simple Flask application that retrieves public repositories of a GitHub user and presents them in JSON format or as a web page.
![Demo](demo.gif)
## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sankeer28/Git-Scraper.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. For CLI tool use, or for JSON API tool use the [link](https://git-scraper.vercel.app/)

   ```bash
   python main.py
   ```

2. Enter the GitHub username when prompted.

3. The script will display the user's public repositories with clickable links.




### JSON Endpoint

To access repository data via JSON, make a GET request to the following endpoint:

```
https://git-scraper.vercel.app/<username>
```

Replace `<username>` with the GitHub username you want to query.

Example:

```
https://git-scraper.vercel.app/sankeer28
```

