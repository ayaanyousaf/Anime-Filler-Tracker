import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import process

def find_url(anime_name): 
    # Make HTTP request to access the web page containing all shows
    response = requests.get("https://www.animefillerlist.com/shows")

    if response.status_code == 200: 
        # Parse through HTML contents of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <div> containing a list of all shows
        show_list = soup.find('div', id='ShowList')
        
        # Store names of all shows
        anime_names = []
        for a in show_list.find_all('a'): 
            anime_names.append(a.text)

        # Retrieve the closest match and score of similarity 
        closest, score = process.extractOne(anime_name, anime_names)

        if score >= 93:
            # Find URL in HTML <a> tag by accessing href attribute
            show_name_tag = show_list.find('a', string=closest)
            url = f"https://animefillerlist.com{show_name_tag['href']}"
            return url, closest
    return None, None

def get_filler_episodes(anime_name, url): 
    # Make HTTP request to access content of anime's webpage 
    response = requests.get(url)

    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and store all filler episodes
        filler_episodes = soup.find_all('tr', class_=['filler odd', 'filler even'])
        output = "" # Output string to return 

        if len(filler_episodes) > 0:
            for episode in filler_episodes: 
                episode_title = episode.find('td', class_='Title').text.strip()
                episode_number = episode.find('td', class_='Number').text.strip()
                output += f'{episode_number} - {episode_title}\n'
        else: 
            output += f'{anime_name.upper()} has no filler episodes.'
    return output
    
def get_filler_percentage(anime_name, url):
    response = requests.get(url) 

    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML table representing the list of episodes 
        episode_list = soup.find('table', class_='EpisodeList')

        # Find the total episode count and filler episode count by counting <tr> tags in table
        total_episode_count = len(episode_list.find_all('tr')[1:]) 
        filler_episode_count = len(episode_list.find_all('tr', class_=['filler odd', 'filler even']))

        # Calculate filler percentage
        percentage = round(((filler_episode_count / total_episode_count) * 100), 1)

    return f'\n{percentage}% of {anime_name} is filler.'
