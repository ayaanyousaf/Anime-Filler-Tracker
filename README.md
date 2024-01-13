# Anime Filler Tracker

Anime Filler Tracker is an application designed to streamline the anime-watching experience for users. It allows users to search for any anime name and be able to view an up to date list of all filler episodes of the series, as well as the percentage of filler episodes in the anime. Users can seemlessly view an entire list of filler episodes and decide which episodes to skip or watch.

A filler episode is an episode that contains content not present or canon in the source material, which is often manga for anime. The episodes are not relevant to the main storyline, but may provide additional backstory or development for certain side characters.

This application was built using Python. It utilizes BeautifulSoup for web scraping and data collection, as well as CustomTkinter to implement a modern and elegant graphical user interface (GUI).

The website used by this application is [Anime Filler List](https://animefillerlist.com). Please note that only the shows listed on this site will be compatible with the application.

![Project Showcase Gif](/public/anime_filler_tracker.gif)

## Installation 
1. Clone Repository
     ```
     git clone https://github.com/ayaanyousaf/anime-filler-tracker.git
     ```
3. Change directory
     ```
     cd anime-filler-tracker
     ```
5. Install dependencies
     ```
     pip install beautifulsoup4
     pip install requests
     pip install customtkinter
     ```

7. Run application
     ```
     python filler_gui.py
     ```

## Usage 
1. Enter the name of an anime series in the search bar and click the search button to view results
2. Example output shows the case where an anime series has <b>no filler episodes</b>
3. Displays an error if the HTTP request fails, indicating the <b>show could not be found</b>

## Features
- **Searching:** Enter an anime series and quickly view all filler episode names and numbers.
- **Fuzzy Search:** Users have more freedom while searching and can make typos.
- **Filler Percentage:** Users can view the percentage of filler episodes in the anime.
- **Clear Button:** Can clear text in the search bar and all previous output with the click of a button.

## Testing 
To run tests, ensure you have the pytest framework installed: 
```
pip install pytest
```
Then type the following command in your terminal: 
```
pytest test.py
```

## Technologies 
- Python
- BeautifulSoup (web scraping)
- customtkinter (designing GUI)
- requests (making HTTP requests)
- fuzzywuzzy (fuzzy search functionality)
- PIL (image loading) 

## License 
This software is licensed under the [MIT License](LICENSE).
