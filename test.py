import unittest
from filler_tracker import get_filler_episodes, get_filler_percentage, find_url

class TestFillerTrackerFunctions(unittest.TestCase):
    def test_get_filler_episodes(self):
        anime_name = "Naruto"
        anime_url = "https://animefillerlist.com/shows/naruto"
        result = get_filler_episodes(anime_name, anime_url)
        self.assertIn("26 - ", result)

    def test_find_url(self):
        anime_name = "Jujuts kaisen"
        result = find_url(anime_name)
        self.assertEqual(("https://animefillerlist.com/shows/jujutsu-kaisen", "Jujutsu Kaisen "), result)

    def test_get_filler_percentage(self):
        anime_name = "One Piece"
        anime_url = "https://animefillerlist.com/shows/one-piece"
        result = get_filler_percentage(anime_name, anime_url)
        self.assertIn("%", result)