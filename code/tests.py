import unittest
from code.url_utility import is_valid_url, trim_url, get_song_url_from_input
from code.admin_utility import get_admin_list_with_parameter

class ProjectsTests(unittest.TestCase):

    def test_url_validator(self):
        self.assertTrue(is_valid_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ'))
        self.assertFalse(is_valid_url(''))
        self.assertFalse(is_valid_url('dfsgsgf'))
        
    def test_trim_url(self):
        self.assertEqual(trim_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ'), 'https://www.youtube.com/watch?v=M-mtdN6R3bQ')
        self.assertEqual(trim_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ&list=PLw-VjHDlEOgvfn7wZ9I-9fZw0Ku8yZrQG&index=2'), 'https://www.youtube.com/watch?v=M-mtdN6R3bQ')
        self.assertEqual(trim_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ&list=PLw-VjHDlEOgvfn7wZ9I-9fZw0Ku8yZrQG'), 'https://www.youtube.com/watch?v=M-mtdN6R3bQ')
        self.assertEqual(trim_url('https://www.youtube.com/watch'), 'https://www.youtube.com/watch')
        self.assertEqual(trim_url(''), '')
        
    def test_get_song_url_from_input(self):
        self.assertEqual(get_song_url_from_input('play https://www.youtube.com/watch?v=M-mtdN6R3bQ'), 'https://www.youtube.com/watch?v=M-mtdN6R3bQ')
        self.assertEqual(get_song_url_from_input('play'), None)
        self.assertEqual(get_song_url_from_input('playhttps://www.youtube.com/watch?v=M-mtdN6R3bQ'), 'ttps://www.youtube.com/watch?v=M-mtdN6R3bQ')
        
    def test_get_admin_list(self):
        self.assertEqual(get_admin_list_with_parameter('[2932997985419264]', False), [2932997985419264])
        self.assertEqual(get_admin_list_with_parameter('[2932997985419264, 2932997985419265]', False), [2932997985419264, 2932997985419265])
        self.assertEqual(get_admin_list_with_parameter('[]', False), [])
        self.assertEqual(get_admin_list_with_parameter('[123, abc]', False), [123])

if __name__ == '__main__':
    unittest.main()
