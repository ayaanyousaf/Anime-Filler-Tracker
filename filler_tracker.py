import requests
from bs4 import BeautifulSoup

def get_filler_episodes(anime_name, anime_url): 
    # Make HTTP request to access content of Anime Filler List website 
    response = requests.get(anime_url)

    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser')

        # Parse through HTML contents of web page to find all filler episodes 
        filler_ep_links = soup.find_all('tr', class_=['filler odd', 'filler even'])
        output_str = "" 

        if len(filler_ep_links) > 0:
            for link in filler_ep_links: 
                episode_title = link.find('td', class_='Title').text.strip()
                episode_number = link.find('td', class_='Number').text.strip()
                output_str += f'{episode_number} - {episode_title}\n'
        else: 
            output_str += f'{anime_name.upper()} has no filler episodes.'
    return output_str

def format_name(anime_name): 
    # Format anime name so it is valid to use in the URL
    formatted = anime_name.lower().replace('/', '-').replace("'", '').replace(':', '')

    # Store exceptions and shortcuts/abbreviations
    exceptions = {
        "attack on titan": "attack-titan",
        "boruto": "boruto-naruto-next-generations",
        "berserk": "berserk-2016",
        "demon slayer": "demon-slayer-kimetsu-no-yaiba",
        "jojos bizarre adventure": "jojos-bizarre-adventure-tv",
        "shingeki no kyojin": "attack-titan",
        "jjk": "jujutsu-kaisen"
        # Add more exceptions as needed
    }
    return exceptions.get(formatted, formatted.replace(' ', '-'))

def get_filler_percentage(anime_name, anime_url):
    response = requests.get(anime_url) 

    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML table representing the list of episodes 
        episode_list = soup.find('table', class_='EpisodeList')

        # Find the total episode count and filler episode count by counting <tr> tags in table
        total_episode_count = len(episode_list.find_all('tr')[1:]) 
        filler_episode_count = len(episode_list.find_all('tr', class_=['filler odd', 'filler even']))

        percentage_filler = round(((filler_episode_count / total_episode_count) * 100), 1)
        
    return f'\n{percentage_filler}% of {anime_name.upper()} is filler.'
