import unittest
from filler_tracker import get_filler_episodes, get_filler_percentage, format_name

class TestFillerTrackerFunctions(unittest.TestCase):
    def test_get_filler_episodes(self):
        anime_name = "Naruto"
        anime_url = "https://animefillerlist.com/shows/naruto"
        result = get_filler_episodes(anime_name, anime_url)
        self.assertTrue(result)

    def test_format_name(self):
        anime_name = "Attack on Titan"
        result = format_name(anime_name)
        self.assertEqual(result, "attack-titan")

    def test_get_filler_percentage(self):
        anime_name = "One Piece"
        anime_url = "https://animefillerlist.com/shows/one-piece"
        result = get_filler_percentage(anime_name, anime_url)
        self.assertIn("%", result)